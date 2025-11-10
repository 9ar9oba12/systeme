"""Core gameplay engine for the Houssam Ascension prototype."""
from __future__ import annotations

import datetime as _dt
from collections import defaultdict
from typing import List

from .models import GameState, Quest, QuestStatus
from .state import award_xp, quest_templates, save_game_state

DIVIDER = "═" * 72


class GameEngine:
    """Facade that orchestrates the life-RPG loop."""

    def __init__(self, state: GameState) -> None:
        self.state = state

    # ------------------------------------------------------------------
    # Morning startup
    # ------------------------------------------------------------------
    def morning_briefing(self) -> str:
        today = self.state.current_day
        quests = self.state.quests_due_today(today)
        overdue = self.state.overdue_quests(today)
        banner = self._rank_banner()
        lines = [banner, DIVIDER, f"DAWN REPORT · {today.isoformat()}".center(72), DIVIDER]
        if overdue:
            lines.append("⚠ URGENT QUESTS FROM YESTERDAY ⚠")
            for quest in overdue:
                lines.append(self._format_quest_line(quest))
            lines.append(DIVIDER)
        if quests:
            lines.append("TODAY'S ACTIVE MISSIONS")
            for quest in quests:
                lines.append(self._format_quest_line(quest))
        else:
            lines.append("No quests scheduled. Use night planning to prime the next assault.")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Quest interactions
    # ------------------------------------------------------------------
    def complete_quest(self, quest_id: str) -> str:
        quest = self._find_quest(quest_id)
        if not quest:
            return "Quest not found."
        if quest.status == QuestStatus.COMPLETED:
            return "Quest already completed."
        quest.status = QuestStatus.COMPLETED
        quest.urgency = False
        quest.failure_count = 0
        titles = award_xp(self.state, quest.xp_reward)
        track = self.state.player.ensure_track(quest.skill)
        track.register_completion(self.state.current_day)
        save_game_state(self.state)
        response = [
            f"✔ Mission Cleared: {quest.title}",
            f"XP +{quest.xp_reward}",
            f"Track streak → {track.streak} days",
        ]
        if titles:
            response.append("Unlocked titles: " + ", ".join(titles))
        return "\n".join(response)

    def fail_quest(self, quest_id: str) -> str:
        quest = self._find_quest(quest_id)
        if not quest:
            return "Quest not found."
        if quest.status == QuestStatus.FAILED:
            return "Quest already marked as failed."
        quest.status = QuestStatus.FAILED
        quest.escalate_failure()
        track = self.state.player.ensure_track(quest.skill)
        track.break_streak()
        save_game_state(self.state)
        return (
            "✖ Mission Failed. Difficulty escalated, XP doubled."
            f" New difficulty: {quest.difficulty.value}, XP: {quest.xp_reward}."
        )

    def schedule_quest(self, template_index: int, due_days_from_now: int = 1) -> str:
        templates = list(quest_templates())
        if template_index < 0 or template_index >= len(templates):
            return "Invalid template selection."
        blueprint = templates[template_index]
        deadline = self.state.current_day + _dt.timedelta(days=due_days_from_now)
        quest = Quest(
            title=blueprint["title"],
            tree=blueprint["tree"],
            skill=blueprint["skill"],
            difficulty=blueprint["difficulty"],
            estimated_effort=blueprint["estimated_effort"],
            xp_reward=blueprint["xp_reward"],
            streak_impact=1,
            deadline=deadline,
        )
        self.state.quests.append(quest)
        save_game_state(self.state)
        return f"Planned: {quest.title} → due {deadline.isoformat()}"

    def list_templates(self) -> str:
        lines = ["Available Quest Blueprints:"]
        for idx, blueprint in enumerate(quest_templates()):
            lines.append(
                f"[{idx}] {blueprint['title']} ({blueprint['tree'].value} · {blueprint['skill']})"
                f" — {blueprint['estimated_effort']} / {blueprint['difficulty'].value} / {blueprint['xp_reward']} XP"
            )
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Day transitions
    # ------------------------------------------------------------------
    def advance_day(self) -> str:
        today = self.state.current_day
        tomorrow = today + _dt.timedelta(days=1)
        summary: List[str] = [DIVIDER, f"MIDNIGHT ROLLOVER → {tomorrow.isoformat()}".center(72), DIVIDER]
        failed = []
        for quest in self.state.quests:
            if quest.deadline <= today and quest.status == QuestStatus.PENDING:
                quest.status = QuestStatus.FAILED
                quest.escalate_failure()
                quest.reset_for_new_day(tomorrow)
                failed.append(quest)
        if failed:
            summary.append("The dungeon punished hesitation. These quests returned angrier:")
            for quest in failed:
                summary.append(self._format_quest_line(quest))
        else:
            summary.append("All missions resolved. Tomorrow awaits fresh orders.")
        self.state.current_day = tomorrow
        save_game_state(self.state)
        return "\n".join(summary)

    def status_overview(self) -> str:
        state = self.state
        player = state.player
        lines = [DIVIDER, "ASCENSION STATUS".center(72), DIVIDER]
        lines.append(f"Name: {player.name} · Rank: {player.rank}-Rank · Level {player.level}")
        lines.append(f"XP in reserve: {player.xp}")
        lines.append("")
        lines.append("Streak Flames:")
        for track_name, track in sorted(player.skill_tracks.items()):
            ember = self._streak_flame(track.streak)
            lines.append(f"  {track_name}: {track.streak}d streak {ember}")
        lines.append("")
        lines.append("Quest Ledger:")
        ledger = defaultdict(list)
        for quest in state.quests:
            ledger[quest.status].append(quest)
        for status in (QuestStatus.PENDING, QuestStatus.COMPLETED, QuestStatus.FAILED):
            lines.append(f" {status.value.upper()} ::")
            if ledger[status]:
                for quest in ledger[status]:
                    lines.append("  " + self._format_quest_line(quest))
            else:
                lines.append("  — none —")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _streak_flame(self, streak: int) -> str:
        if streak >= 30:
            return "🔥🔥🔥"
        if streak >= 14:
            return "🔥🔥"
        if streak >= 7:
            return "🔥"
        if streak >= 3:
            return "⚡"
        if streak > 0:
            return "✦"
        return "□"

    def _format_quest_line(self, quest: Quest) -> str:
        urgency = " !!" if quest.urgency else ""
        return (
            f"[{quest.id[:6]}] {quest.title}"
            f" — {quest.tree.value}/{quest.skill}"
            f" — {quest.difficulty.value}"
            f" — {quest.xp_reward} XP"
            f" — due {quest.deadline.isoformat()}{urgency}"
        )

    def _rank_banner(self) -> str:
        player = self.state.player
        return f"◈ {player.rank}-Rank Ascendant · Level {player.level} ◈".center(72)

    def _find_quest(self, quest_id: str) -> Quest | None:
        for quest in self.state.quests:
            if quest.id.startswith(quest_id) or quest.id == quest_id:
                return quest
        return None


__all__ = ["GameEngine"]
