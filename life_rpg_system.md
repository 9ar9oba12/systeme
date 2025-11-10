# Houssam Ascension Protocol

> _"You awaken at E-Rank. Your stats are dust. The dungeon you face is life itself."_

This document defines a modern, serious, atmospheric life-RPG system that shepherds **Houssam** from **E-Rank Level 1** to **S-Rank 70+** through slow, meaningful progression. The experience blends discipline-building mechanics, gamified feedback, and consequences that make every habit feel like a mission inside a real-world dungeon.

---

## 1. Core Identity
- **Name:** Houssam
- **Current Rank:** E-Rank Level 1
- **Level Cap:** 70+ (S-Rank ultra mastery)
- **Initial Stats:** All skills at 0 across every tree.
- **Tone:** Serious, motivating, elegant, slightly dark. Mentor voice is cold but encouraging.
- **Primary Pillars:** Slow growth, hard consequences, sacred streaks, and a full-life skill tree.

---

## 2. Design Principles

| Principle | Implementation |
| --- | --- |
| Slow, realistic leveling | ~1 week of consistent execution to gain early levels, with exponential growth in required XP. |
| Failure has weight | Quests auto-fail at midnight, return with doubled difficulty & reward, and trigger visual/audio alerts. |
| Consistency > intensity | Streak system influences XP multipliers, quest generation, and achievement gates. |
| Life as skill trees | Every domain has clear skill tracks, tiers, and specialized quests. |
| Immersive presentation | Deep colors, atmospheric UI, subtle particles, and narrator-grade messaging reinforce the journey. |

---

## 3. Rank & Level Progression

### 3.1 Level Bands
| Rank | Level Range | Identity |
| --- | --- | --- |
| **E-Rank** | 1–9 | Initiate — building bare-minimum discipline |
| **D-Rank** | 10–18 | Apprentice — juggling consistency across domains |
| **C-Rank** | 19–27 | Challenger — endures discomfort, embraces hardship |
| **B-Rank** | 28–36 | Hunter — lives with deliberate intensity |
| **A-Rank** | 37–45 | Vanguard — mastery evident, streaks ironclad |
| **S-Rank** | 46–70+ | Ascendant — dominant across all pillars |

### 3.2 XP Curve
- **Base XP requirement (Level 1 → 2):** 120 XP
- **Growth factor:** 1.45 per level (rounded to nearest 5 XP)
- **Rank Gates:** Unlocking a new rank requires completing a "Rank Trial" (multi-quest boss encounter) in addition to XP.
- **Streak Influence:** Active streaks (>7 days) apply +10% XP gain; broken streaks incur −15% until rebuilt.

| Level | XP to Next | Cumulative XP |
| --- | --- | --- |
| 1 | 120 | 0 |
| 2 | 175 | 120 |
| 3 | 255 | 295 |
| 4 | 370 | 550 |
| 5 | 535 | 920 |
| 6 | 775 | 1,455 |
| 7 | 1,125 | 2,230 |
| 8 | 1,635 | 3,355 |
| 9 | 2,375 | 4,990 |
| ... | ... | ... |
| 45 | 67,365 | 583,010 |
| 60 | 259,140 | 1,378,905 |
| 70 | 1,084,780 | 3,664,450 |

> By S-Rank, a single level may take months of flawless execution.

---

## 4. Skill Trees
Three overarching trees contain tracks that climb from Tier 0 (Novice) to Tier 6 (Mythic). Each tier gates advanced quests, tools, and titles.

### 4.1 Dev Tree
| Track | Tier 0 | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 | Tier 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Math Fundamentals** | Count & basic arithmetic | Fractions & decimals | Algebra basics | Functions & graphs | Calculus intro | Probability & statistics | Proofs & abstract math |
| **Programming Basics** | Syntax drills | Control structures | Modular design | Object/function patterns | Debugging mastery | System design | Production architectures |
| **Algorithms** | Understand steps | Classic sorts/search | Recurrence solving | Graph theory | Dynamic programming | Optimization strategies | Advanced paradigms & competitions |
| **Data Structures** | Arrays & lists | Stacks/queues | Hash maps | Trees | Heaps & priority queues | Graphs | Custom & memory-optimized structures |
| **Problem Solving** | Solve guided tasks | Small practice sets | Daily coding problems | Timed challenges | Competitive scenarios | Multi-week projects | Multi-domain architectural problem solving |

### 4.2 Faith Tree
| Track | Tier 0 | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 | Tier 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Prayer Consistency** | Track obligatory prayers | Daily punctual prayer | Masjid attendance | Additional Sunnah | Qiyam integration | Leadership/Imam practice | Mastery & teaching |
| **Qur’an Recitation** | 5-min readings | Daily juz tracking | Tajwid focus | Hour-long recitations | Recitation circles | Certified proficiency | Leading taraweeh |
| **Qur’an Understanding** | Transliteration | Vocabulary building | Tafsir summaries | Thematic studies | Deep Tafsir | Scholarly discourse | Teach tafsir |
| **Qur’an Memorization** | Single verses | Short Surahs | Juz memorization | Retention routines | Half Qur’an | Full memorization | Lifetime revision mastery |
| **Voluntary Fasting** | Awareness | One fast/month | Weekly (Mon/Thu) | Consecutive sets | Ramadan optimization | Frequent fasts | Routine extended fasts |
| **Behavior & Discipline** | Daily check-ins | Trigger awareness | Habit replacement | Self-audits | Character development | Mentorship | Exemplary conduct |

### 4.3 Body Tree
| Track | Tier 0 | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 | Tier 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Strength** | Assisted movements | Bodyweight mastery | Weighted basics | Progressive overload | Compound lifts | Advanced periodization | Elite strength metrics |
| **Endurance** | 5-min walks | Daily steps | Jogging blocks | 5K timed runs | Half-marathon level | Competitive endurance | Ultra-conditioning |
| **Mobility & Flexibility** | Joint circles | Static stretches | Dynamic flow | Mobility routines | Yoga/pilates integration | Athletic mobility | Mobility coaching |
| **Nutrition Discipline** | Logging | Balanced plates | Macro awareness | Meal prepping | Periodized nutrition | Advanced fueling | Performance nutrition |
| **Physical Form** | Posture awareness | Core activation | Body recomposition | Lean physique | Athletic build | Low body-fat maintenance | Peak aesthetic form |

---

## 5. Daily Cycle

### 5.1 Morning Startup Popup
- Launches at OS boot; full-screen overlay with ambient dark gradient.
- Displays:
  - Date, rank badge, and level progress ring.
  - **Today’s Quests** sorted by urgency, with streak flames beside each track.
  - Audio cue: low hum rising to a subtle chime when acknowledged.
- Only dismissible after Houssam acknowledges the mission for the day.

### 5.2 Quest Flow
1. **Single Mission Focus:** Interface surfaces one quest at a time with a countdown timer.
2. **Card Anatomy:**
   - Title, skill tree icon, targeted skill tier.
   - Difficulty crest (EASY / STANDARD / HARD / BOSS / URGENT).
   - Estimated effort (time & physical/mental load).
   - XP value and streak impact.
   - Deadline indicator.
3. **Interactions:**
   - Start: Initiates timer, plays subtle whoosh animation.
   - Complete: Trigger gold pulse, XP particles, streak flame grows.
   - Fail: Red lightning strike, screen shake, low rumble sound.

### 5.3 Night Planning Ritual
- Accessible after 9 PM local time.
- Calm UI: deep blues, candle-like particle effects, subdued strings.
- Steps:
  1. **Reflect:** Auto-generated summary of completed/failed quests, streaks, XP, and mentor commentary.
  2. **Recommend:** System suggests quests based on weak skills, streak health, and upcoming boss requirements.
  3. **Plan:** Houssam selects tomorrow’s quests, limited to 6 major and 4 micro quests.
  4. **Lock-In:** Confirmation animation with faint voiceover: “The path is set. Do not falter.”

### 5.4 Midnight Rollover
- All pending quests fail automatically.
- Failure triggers the Doubling Rule (see §6).
- Streak penalties apply immediately and are reflected in the next morning popup.

---

## 6. Quest Mechanics

### 6.1 Quest Schema
```json
{
  "title": "string",
  "skillTree": "Dev | Faith | Body",
  "skillTrack": "string",
  "tier": 0-6,
  "difficulty": "Easy | Standard | Hard | Boss | Urgent",
  "estimatedEffort": "time + intensity description",
  "xp": integer,
  "streakImpact": "Breaks | Maintains | Builds",
  "deadline": "HH:MM",
  "status": "Pending | Active | Done | Failed",
  "urgencyTags": ["FailedYesterday", "CriticalStreak", ...],
  "doublingCount": integer
}
```

### 6.2 Difficulty Calibration
| Difficulty | Effort Window | Description |
| --- | --- | --- |
| Easy | 5–10 minutes | Micro habits to maintain streaks. |
| Standard | 15–30 minutes | Primary daily quests. |
| Hard | 45–90 minutes | Demanding focus/physical push. |
| Boss | 120+ minutes | Multi-step mission or combined questline. |
| Urgent | Previous failure(s) | Doubled effort & XP, mandatory priority. |

### 6.3 Doubling Rule
- Upon failure:
  - `doublingCount += 1`
  - Difficulty tier increases one step (capped at Boss unless already Boss).
  - XP reward doubles per failure (XP × 2^doublingCount).
  - Quest flagged URGENT with red lightning animation and alarm-like audio.
- Accumulating **3 concurrent urgent quests** triggers **Penalty Mode**:
  - Temporary −25% XP gain.
  - Immediate streak break for associated tracks.
  - Mentor message: “You are slipping. Regain control or descend further.”

### 6.4 Quest Generation Logic
1. **Baseline Quests:** Derived from tier requirements and streak maintenance.
2. **Adaptive Quests:** Triggered when a skill falls behind (no XP in 3 days).
3. **Streak Quests:** Automatically scheduled micro-tasks to preserve streaks.
4. **Boss Quests:** Available at level milestones or rank transition gates.
5. **Side Quests:** Optional flavor tasks that reward cosmetics or achievements.

---

## 7. Streak System
- **Per Track & Global:** Each skill track and each tree maintains its own streak; a global streak aggregates the shortest.
- **Thresholds:**
  - 3 days: unlocks glowing ember effect on quest cards.
  - 7 days: upgrades streak flame; unlocks +10% XP buff.
  - 14 days: adds low roaring flame animation and badge.
  - 30 days: spawns “Unbroken” achievement and +1 daily energy slot.
- **Break Consequences:**
  - Immediate -15% XP modifier on relevant track for 3 days.
  - Quest planner pushes urgent quests in broken domain.
  - Visual: flame extinguishes, ember ash effect, somber audio sting.

---

## 8. Rewards & Penalties

### 8.1 XP & Titles
- Titles unlock at specified milestones (examples):
  - Level 3: **Beginner Seeker**
  - Level 7: **First Ember**
  - Level 12: **Steady Hand**
  - Level 20: **Relentless**
  - Level 30: **Silent Hunter**
  - Level 45: **Iron Will**
  - Level 55: **Night Vanguard**
  - Level 70: **Ascendant**

### 8.2 Achievements
- 7-Day Perfect Run (no failures)
- 30-Day Streak Maintained
- Clear all Urgent Quests within 24h
- Complete Weekly Boss without streak break
- Full Week Balanced (Dev, Faith, Body each receive ≥3 quests completed)

### 8.3 Penalty Mode Escalation
1. **Warning:** 3 urgent quests → penalty mode (XP −25%).
2. **Critical:** 5 urgent quests → freeze level progress until 2 are cleared; mentor voiceover.
3. **Lockdown:** 7 urgent quests → forced “Recovery Week” scenario with limited planning freedom.

---

## 9. Audio & Visual Atmosphere
- **Color Palette:** Deep obsidian, midnight blue, ember orange, muted gold.
- **Typography:** Sharp sans-serif headers (e.g., Exo 2), elegant serif for mentor narration.
- **Animation:**
  - Subtle parallax backgrounds with floating dust particles.
  - Quest completion uses golden ripple + XP shards.
  - Failure triggers red lightning, UI tremor, and bass-heavy rumble.
- **Soundscape:**
  - Ambient low hum on dashboards.
  - Satisfying chime on quest completion.
  - Drum hits on level-ups followed by choir swell.

---

## 10. Onboarding Narrative (Day 1)
**Message:**
> “You have awakened at E-Rank. Your stats are at zero. Your body is weak. Your mind is unfocused. Your discipline is broken. Today you take your first step. Complete your starter quests and begin your ascension.”

**Starter Quest Deck:**
1. **Faith · Prayer Consistency · Easy** — Pray all 5 obligatory prayers (XP 40).
2. **Faith · Qur’an Recitation · Easy** — Recite Qur’an for 5 minutes (XP 25).
3. **Body · Strength · Easy** — Perform 3 sets of 2 push-ups (XP 30).
4. **Body · Endurance · Easy** — Walk for 5 minutes outdoors (XP 20).
5. **Dev · Math Fundamentals · Easy** — Count from 1 to 20 and write it down (XP 25).
6. **Dev · Programming Basics · Standard** — Watch a 10-minute programming basics lesson and create 3 code examples (XP 60).

- Completion triggers a **Level 2** projection (if all done) and unlocks the “Beginner Seeker” title.
- Failure of any quest results in immediate urgent flag for Day 2 with doubled effort/XP.

---

## 11. Long-Term Evolution
- **Scaling Difficulty:** Quests evolve in length, complexity, and combination (e.g., Dev + Body synergy quests like “Build a step-tracking dashboard”).
- **Weekly Boss Quests:**
  - Example: “Faith Trial — Memorize and recite Surat Al-Mulk by Friday.”
  - Example: “Dev Gauntlet — Implement and document a dynamic programming solution to a medium LeetCode problem.”
  - Example: “Body Assault — Complete 5km run under 35 minutes.”
- **Seasonal Challenges:** 90-day arcs that weave narrative lore and unlock cosmetics (rank banners, aura effects).
- **Dungeon Mode (Optional Upgrade):** Chains multiple quests into a timed gauntlet with limited rest windows.
- **Lore Integration:** Periodic mentor entries recounting Houssam’s journey, reinforcing immersion.

---

## 12. System Architecture Notes
- **Platform:** Desktop-first progressive web app with offline-first data persistence.
- **Core Modules:**
  - **Quest Engine:** Generates, schedules, and tracks quest state with doubling logic.
  - **Progress Engine:** Handles XP curve, level checks, rank trials, and titles.
  - **Streak Engine:** Manages streaks, modifiers, visual states, and penalties.
  - **Notification Layer:** OS-level morning popup, urgent alerts, night planning reminders.
  - **Atmospheric Layer:** Orchestrates animations, sound cues, and theming across states.
- **Data Storage:** Local encrypted DB + optional cloud sync; full audit trail of quests.
- **Analytics:** Streak heatmaps, XP trends, quest failure analysis, penalty mode history.

---

## 13. Mentor Voice Samples
- **Daily Greeting:** “Hunter in training, the dungeon opens. Face your quests.”
- **Quest Completion:** “One strike lands. Keep carving the path.”
- **Failure:** “You hesitated. The dungeon tightens. Return stronger.”
- **Level Up:** “Power surges. Level +1. Do not squander the momentum.”
- **Penalty Mode:** “Your discipline fractures. Regain control or be consumed.”

---

## 14. Extensibility Hooks
- **Upgrade Pack (on request):** Adds boss fights, dungeon mode, weekly summaries, deeper lore, and social leaderboards.
- **Customization:** Rank banner skins, soundtrack variations, and configurable voice intensity.
- **Automation:** Optional integrations with calendars, fitness trackers, coding platforms for automatic quest verification.

---

## 15. Summary
The Houssam Ascension Protocol is a deliberate, atmospheric life-RPG framework. It respects the difficulty of transformation, punishes failure, and rewards relentless consistency. The path from E-Rank Level 1 to S-Rank 70+ is brutally long, but every completed quest feeds the flame. The dungeon is always open. The choice to ascend belongs to Houssam.

---

## 16. Prototype CLI Implementation
To begin materializing the experience, a console-based prototype (`main.py`) now ships with the repository. It leans on the rules above while keeping the tone sharp and modern even without a browser-based UI.

- **Morning Briefing (`python main.py morning`):** Displays a dawn popup-like report with urgent quests, active missions, and the current rank banner.
- **Quest Flow Controls:**
  - `python main.py complete <quest_id>` — Clears a mission, awards XP, and fuels streak flames.
  - `python main.py fail <quest_id>` — Applies the doubling rule instantly and shatters the related streak.
  - `python main.py advance` — Triggers the midnight rollover, auto-failing unfinished quests and pushing them to the next day with red-alert status.
- **Planning Tools:**
  - `python main.py templates` — Lists atmospheric quest blueprints inspired by Solo Leveling’s hunter briefings.
  - `python main.py plan <index> [--due N]` — Schedules a quest card for an upcoming day.
- **Status Dashboard (`python main.py status`):** Shows level, XP reserve, streak flames, and a ledger of pending/completed/failed quests in one atmospheric snapshot.

The prototype persists progress locally (`game_state.json`) so every command matters. It is intentionally strict—failure escalates difficulty, streaks extinguish on misses, and the presentation keeps the hunter mindset alive even in a terminal.
