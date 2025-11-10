"""Persistence helpers and progression math for the Houssam RPG."""
from __future__ import annotations

import datetime as _dt
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from .models import (
    BodySkill,
    DevSkill,
    Difficulty,
    FaithSkill,
    GameState,
    PlayerProgress,
    Quest,
    QuestStatus,
    SkillTree,
)

STATE_PATH = Path("game_state.json")
BASE_XP = 120
XP_GROWTH = 1.45
RANK_GATES = {
    "E": (1, 9),
    "D": (10, 18),
    "C": (19, 27),
    "B": (28, 36),
    "A": (37, 45),
    "S": (46, 70),
}
TITLE_UNLOCKS = {
    3: "Beginner Seeker",
    7: "First Ember",
    12: "Steady Hand",
    20: "Relentless",
    30: "Silent Hunter",
    45: "Iron Will",
    55: "Night Vanguard",
    70: "Ascendant",
}


def _xp_table(up_to_level: int = 120) -> Dict[int, int]:
    """Pre-compute XP requirements for the exponential growth curve."""
    xp_requirements: Dict[int, int] = {1: BASE_XP}
    current = BASE_XP
    for level in range(2, up_to_level + 1):
        current = int(round(current * XP_GROWTH / 5.0)) * 5
        xp_requirements[level] = current
    return xp_requirements


XP_TABLE = _xp_table()


def xp_for_next_level(level: int) -> int:
    return XP_TABLE.get(level, XP_TABLE[max(XP_TABLE)])


def rank_for_level(level: int) -> str:
    for rank, (start, end) in RANK_GATES.items():
        if start <= level <= end:
            return rank
    if level > 70:
        return "S"
    return "E"


def load_game_state(path: Path | None = None) -> GameState:
    target = path or STATE_PATH
    if target.exists():
        with target.open("r", encoding="utf-8") as fh:
            payload = json.load(fh)
        return _game_state_from_payload(payload)
    return _bootstrap_state()


def save_game_state(state: GameState, path: Path | None = None) -> None:
    target = path or STATE_PATH
    payload = _game_state_to_payload(state)
    with target.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)


def award_xp(state: GameState, xp: int) -> List[str]:
    """Grant XP and return any unlocked titles."""
    player = state.player
    player.xp += xp
    titles_unlocked: List[str] = []
    while True:
        threshold = xp_for_next_level(player.level)
        if player.xp < threshold:
            break
        player.xp -= threshold
        player.level += 1
        player.rank = rank_for_level(player.level)
        maybe_title = TITLE_UNLOCKS.get(player.level)
        if maybe_title and maybe_title not in player.titles:
            player.titles.append(maybe_title)
            titles_unlocked.append(maybe_title)
    return titles_unlocked


def _bootstrap_state() -> GameState:
    today = _dt.date.today()
    starter_quests = _starter_quests(today)
    player = PlayerProgress(last_login=today)
    return GameState(player=player, quests=starter_quests, current_day=today)


def _starter_quests(today: _dt.date) -> List[Quest]:
    return [
        Quest(
            title="Pray all 5 obligatory prayers",
            tree=SkillTree.FAITH,
            skill=FaithSkill.PRAYER_CONSISTENCY.value,
            difficulty=Difficulty.TUTORIAL,
            estimated_effort="5 checkpoints",
            xp_reward=40,
            streak_impact=1,
            deadline=today,
        ),
        Quest(
            title="Recite Qur'an for 5 minutes",
            tree=SkillTree.FAITH,
            skill=FaithSkill.QURAN_RECITATION.value,
            difficulty=Difficulty.TUTORIAL,
            estimated_effort="5 minutes",
            xp_reward=25,
            streak_impact=1,
            deadline=today,
        ),
        Quest(
            title="Perform 3 sets of 2 push-ups",
            tree=SkillTree.BODY,
            skill=BodySkill.STRENGTH.value,
            difficulty=Difficulty.TUTORIAL,
            estimated_effort="3 sets",
            xp_reward=30,
            streak_impact=1,
            deadline=today,
        ),
        Quest(
            title="Walk outdoors for 5 minutes",
            tree=SkillTree.BODY,
            skill=BodySkill.ENDURANCE.value,
            difficulty=Difficulty.TUTORIAL,
            estimated_effort="5 minutes",
            xp_reward=20,
            streak_impact=1,
            deadline=today,
        ),
        Quest(
            title="Count 1→20 and log it",
            tree=SkillTree.DEV,
            skill=DevSkill.MATH_FUNDAMENTALS.value,
            difficulty=Difficulty.TUTORIAL,
            estimated_effort="10 minutes",
            xp_reward=25,
            streak_impact=1,
            deadline=today,
        ),
        Quest(
            title="Watch 10 min programming basics + craft 3 examples",
            tree=SkillTree.DEV,
            skill=DevSkill.PROGRAMMING_BASICS.value,
            difficulty=Difficulty.STANDARD,
            estimated_effort="25 minutes",
            xp_reward=60,
            streak_impact=1,
            deadline=today,
        ),
    ]


def _quest_to_payload(quest: Quest) -> Dict:
    data = {
        "title": quest.title,
        "tree": quest.tree.value,
        "skill": quest.skill,
        "difficulty": quest.difficulty.value,
        "estimated_effort": quest.estimated_effort,
        "xp_reward": quest.xp_reward,
        "streak_impact": quest.streak_impact,
        "deadline": quest.deadline.isoformat(),
        "status": quest.status.value,
        "id": quest.id,
        "urgency": quest.urgency,
        "failure_count": quest.failure_count,
        "notes": quest.notes,
    }
    return data


def _quest_from_payload(payload: Dict) -> Quest:
    return Quest(
        title=payload["title"],
        tree=SkillTree(payload["tree"]),
        skill=payload["skill"],
        difficulty=Difficulty(payload.get("difficulty", Difficulty.TUTORIAL.value)),
        estimated_effort=payload["estimated_effort"],
        xp_reward=payload["xp_reward"],
        streak_impact=payload["streak_impact"],
        deadline=_dt.date.fromisoformat(payload["deadline"]),
        status=QuestStatus(payload.get("status", QuestStatus.PENDING.value)),
        id=payload.get("id"),
        urgency=payload.get("urgency", False),
        failure_count=payload.get("failure_count", 0),
        notes=payload.get("notes"),
    )


def _player_to_payload(player: PlayerProgress) -> Dict:
    return {
        "name": player.name,
        "level": player.level,
        "xp": player.xp,
        "rank": player.rank,
        "last_login": player.last_login.isoformat() if player.last_login else None,
        "titles": list(player.titles),
        "skill_tracks": {
            name: {
                "skill_name": track.skill_name,
                "streak": track.streak,
                "last_completed": track.last_completed.isoformat() if track.last_completed else None,
            }
            for name, track in player.skill_tracks.items()
        },
    }


def _player_from_payload(payload: Dict) -> PlayerProgress:
    player = PlayerProgress(
        name=payload.get("name", "Houssam"),
        level=payload.get("level", 1),
        xp=payload.get("xp", 0),
        rank=payload.get("rank", "E"),
        last_login=_dt.date.fromisoformat(payload["last_login"]) if payload.get("last_login") else None,
        titles=payload.get("titles", []),
    )
    for name, track_payload in payload.get("skill_tracks", {}).items():
        track = player.ensure_track(name)
        track.streak = track_payload.get("streak", 0)
        last_completed = track_payload.get("last_completed")
        track.last_completed = _dt.date.fromisoformat(last_completed) if last_completed else None
    return player


def _game_state_to_payload(state: GameState) -> Dict:
    return {
        "player": _player_to_payload(state.player),
        "quests": [_quest_to_payload(q) for q in state.quests],
        "current_day": state.current_day.isoformat(),
    }


def _game_state_from_payload(payload: Dict) -> GameState:
    player = _player_from_payload(payload["player"])
    quests = [_quest_from_payload(q) for q in payload.get("quests", [])]
    current_day = _dt.date.fromisoformat(payload["current_day"])
    return GameState(player=player, quests=quests, current_day=current_day)


def quest_templates() -> Iterable[Dict[str, Any]]:
    """Provide a curated set of modern-flavored quest prompts for planning."""
    return (
        {
            "title": "Shadow Coding Drill — solve a timed array problem",
            "tree": SkillTree.DEV,
            "skill": DevSkill.ALGORITHMS.value,
            "estimated_effort": "35 minutes",
            "xp_reward": 95,
            "difficulty": Difficulty.STANDARD,
        },
        {
            "title": "Midnight Tafsir Reflection",
            "tree": SkillTree.FAITH,
            "skill": FaithSkill.QURAN_UNDERSTANDING.value,
            "estimated_effort": "25 minutes",
            "xp_reward": 70,
            "difficulty": Difficulty.STANDARD,
        },
        {
            "title": "Hunter's Conditioning Circuit",
            "tree": SkillTree.BODY,
            "skill": BodySkill.STRENGTH.value,
            "estimated_effort": "30 minutes",
            "xp_reward": 110,
            "difficulty": Difficulty.DEMANDING,
        },
        {
            "title": "Calm the Mind — pre-dawn breathing + du'a",
            "tree": SkillTree.FAITH,
            "skill": FaithSkill.BEHAVIOR_DISCIPLINE.value,
            "estimated_effort": "15 minutes",
            "xp_reward": 45,
            "difficulty": Difficulty.EASY,
        },
        {
            "title": "Architect the Day — plan tomorrow's code session",
            "tree": SkillTree.DEV,
            "skill": DevSkill.PROBLEM_SOLVING.value,
            "estimated_effort": "20 minutes",
            "xp_reward": 65,
            "difficulty": Difficulty.STANDARD,
        },
    )


__all__ = [
    "STATE_PATH",
    "load_game_state",
    "save_game_state",
    "award_xp",
    "quest_templates",
]
