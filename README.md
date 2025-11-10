# Houssam Ascension CLI Prototype

This repository contains the terminal-first prototype of the life-RPG system described in `life_rpg_system.md`. The program models quests, streaks, XP, and rank progression for Houssam and exposes a command-line interface that delivers the morning briefing, tracks completion, and rolls days forward.

## Prerequisites

- Python 3.10 or later (no external dependencies are required)
- macOS, Linux, or Windows terminal access

## First Run

1. Clone the repository and open a terminal in the project directory.
2. (Optional) Create and activate a virtual environment.
3. Run the morning briefing to generate the initial game state:
   ```bash
   python main.py morning
   ```
   This boots the starter quests for Day 1 and prints the Solo Leveling-inspired briefing text.

The engine persists progress to `game_state.json` in the project root. Delete this file if you ever want to restart from E-Rank Level 1.

## Command Overview

```bash
python main.py --help
```
Shows the available subcommands. The most common flows are listed below:

- `python main.py morning` – display the atmospheric dawn mission briefing for the current day.
- `python main.py status` – inspect current level, rank, XP, streaks, and quest list.
- `python main.py templates` – view the catalog of quest blueprints available for planning.
- `python main.py plan` – list templates, or `python main.py plan <index>` to schedule a quest by its template number (use `--due` to set the due-day offset).
- `python main.py complete <quest_id>` – mark a quest as finished (you can use the ID prefix shown in status output).
- `python main.py fail <quest_id>` – register a failed quest; the engine will double its difficulty/XP for the next day and mark it URGENT.
- `python main.py advance` – trigger the midnight rollover that auto-fails unfinished quests, advances the in-game day, and refreshes the morning slate.

For a guided planning loop, run `python main.py plan` at night to review suggested quests, then lock them in by providing their template indices.

## Automatic Morning Launch

Place one of the helper scripts in `scripts/` on your system's startup routine so the briefing greets you as soon as the machine boots.

### Windows 10/11
1. Edit `scripts\houssam_morning.bat` and point `VENV_PYTHON` to your virtual environment's interpreter if needed.
2. Open **Task Scheduler** → **Create Task...** (not basic task).
3. Under **Triggers**, add a new trigger **At log on** for your account.
4. Under **Actions**, choose **Start a Program** and browse to the `.bat` file.
5. Enable **Run with highest privileges** and **Configure for** your Windows version so the console pops up immediately after sign-in.

### macOS (Ventura and later)
1. Make the script executable: `chmod +x scripts/houssam_morning.sh`.
2. Open **System Settings** → **General** → **Login Items**.
3. Click **+** and add the shell script. macOS will launch Terminal, run the script, and display the morning briefing on each login.

### Linux (systemd-based distros)
1. Ensure the script is executable: `chmod +x scripts/houssam_morning.sh`.
2. Copy the template below to `~/.config/systemd/user/houssam-morning.service`:
   ```ini
   [Unit]
   Description=Houssam Ascension morning briefing

   [Service]
   Type=simple
   WorkingDirectory=/path/to/systeme
   ExecStart=/path/to/systeme/scripts/houssam_morning.sh
   Restart=no

   [Install]
   WantedBy=default.target
   ```
3. Run `systemctl --user daemon-reload` followed by `systemctl --user enable --now houssam-morning.service`.
4. The CLI will appear in a terminal emulator when your desktop session starts. Replace `ExecStart` with a specific terminal command (e.g., `ExecStart=/usr/bin/kitty ...`) if you prefer a particular app.

## Tips

- Run `python main.py status` after each quest update to track your streak flames and see which missions turned URGENT.
- The CLI is deterministic; feel free to script or alias commands if you want to bind them to operating-system automations.
- Keep the terminal window wide enough (≥90 columns) for the best layout of quest cards and banners.

---

If you need richer UI (animations, sound, or a desktop overlay), say “upgrade it” and we can build the next layer on top of this foundation.
