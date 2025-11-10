"""Data models for the Houssam Ascension Protocol prototype."""
from __future__ import annotations

import datetime as _dt
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class SkillTree(str, Enum):
    DEV = "Dev"
    FAITH = "Faith"
    BODY = "Body"


class DevSkill(str, Enum):
    MATH_FUNDAMENTALS = "Math Fundamentals"
    PROGRAMMING_BASICS = "Programming Basics"
    ALGORITHMS = "Algorithms"
    DATA_STRUCTURES = "Data Structures"
    PROBLEM_SOLVING = "Problem Solving"


class FaithSkill(str, Enum):
    PRAYER_CONSISTENCY = "Prayer Consistency"
    QURAN_RECITATION = "Qur'an Recitation"
    QURAN_UNDERSTANDING = "Qur'an Understanding"
    QURAN_MEMORIZATION = "Qur'an Memorization"
    VOLUNTARY_FASTING = "Voluntary Fasting"
    BEHAVIOR_DISCIPLINE = "Behavior & Discipline"


class BodySkill(str, Enum):
    STRENGTH = "Strength"
    ENDURANCE = "Endurance"
    MOBILITY = "Mobility & Flexibility"
    NUTRITION = "Nutrition Discipline"
    PHYSICAL_FORM = "Physical Form"


class Difficulty(str, Enum):
    TUTORIAL = "Tutorial"
    EASY = "Easy"
    STANDARD = "Standard"
    DEMANDING = "Demanding"
    BRUTAL = "Brutal"

    def escalate(self) -> "Difficulty":
        order = [Difficulty.TUTORIAL, Difficulty.EASY, Difficulty.STANDARD, Difficulty.DEMANDING, Difficulty.BRUTAL]
        idx = order.index(self)
        if idx + 1 < len(order):
            return order[idx + 1]
        return self


class QuestStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Quest:
    title: str
    tree: SkillTree
    skill: str
    difficulty: Difficulty
    estimated_effort: str
    xp_reward: int
    streak_impact: int
    deadline: _dt.date
    status: QuestStatus = QuestStatus.PENDING
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    urgency: bool = False
    failure_count: int = 0
    notes: Optional[str] = None

    def escalate_failure(self) -> None:
        """Apply the doubling rule after a failure."""
        self.failure_count += 1
        self.urgency = True
        self.difficulty = self.difficulty.escalate()
        self.xp_reward *= 2
        if self.notes:
            self.notes += f" | Failure streak: {self.failure_count}"
        else:
            self.notes = f"Failure streak: {self.failure_count}"

    def reset_for_new_day(self, new_deadline: _dt.date) -> None:
        self.status = QuestStatus.PENDING
        self.deadline = new_deadline


@dataclass
class SkillTrackProgress:
    skill_name: str
    streak: int = 0
    last_completed: Optional[_dt.date] = None

    def register_completion(self, today: _dt.date) -> None:
        if self.last_completed == today - _dt.timedelta(days=1):
            self.streak += 1
        else:
            self.streak = 1
        self.last_completed = today

    def break_streak(self) -> None:
        self.streak = 0
        self.last_completed = None


@dataclass
class PlayerProgress:
    name: str = "Houssam"
    level: int = 1
    xp: int = 0
    rank: str = "E"
    last_login: Optional[_dt.date] = None
    titles: List[str] = field(default_factory=list)
    skill_tracks: Dict[str, SkillTrackProgress] = field(default_factory=dict)

    def ensure_track(self, skill_name: str) -> SkillTrackProgress:
        if skill_name not in self.skill_tracks:
            self.skill_tracks[skill_name] = SkillTrackProgress(skill_name=skill_name)
        return self.skill_tracks[skill_name]


@dataclass
class GameState:
    player: PlayerProgress
    quests: List[Quest]
    current_day: _dt.date

    def overdue_quests(self, today: _dt.date) -> List[Quest]:
        return [q for q in self.quests if q.deadline < today and q.status == QuestStatus.PENDING]

    def quests_due_today(self, today: _dt.date) -> List[Quest]:
        return [q for q in self.quests if q.deadline == today and q.status == QuestStatus.PENDING]

    def completed_today(self, today: _dt.date) -> List[Quest]:
        return [q for q in self.quests if q.deadline == today and q.status == QuestStatus.COMPLETED]


__all__ = [
    "SkillTree",
    "DevSkill",
    "FaithSkill",
    "BodySkill",
    "Difficulty",
    "QuestStatus",
    "Quest",
    "SkillTrackProgress",
    "PlayerProgress",
    "GameState",
]
