"""Tkinter-based control center for the Houssam Ascension system."""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional

from .engine import GameEngine
from .models import Quest, QuestStatus
from .state import load_game_state, quest_templates, xp_for_next_level

BG = "#05070F"
FG = "#E6EDFF"
ACCENT = "#6C63FF"
DANGER = "#FF6B81"
SUCCESS = "#63FFA4"
CARD_BG = "#0D1627"
MUTED = "#8A94B5"


class AscensionApp(tk.Tk):
    """Desktop interface inspired by sleek RPG command centers."""

    def __init__(self, engine: Optional[GameEngine] = None) -> None:
        super().__init__()
        self.title("Houssam Ascension Nexus")
        self.configure(bg=BG)
        self.geometry("1180x720")
        self.minsize(1080, 640)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Dark.TFrame", background=BG)
        style.configure("Dark.TLabelframe", background=BG, foreground=FG)
        style.configure("Dark.TLabelframe.Label", background=BG, foreground=FG)
        style.configure("Dark.TLabel", background=BG, foreground=FG, font=("Segoe UI", 12))
        style.configure("Title.TLabel", background=BG, foreground=FG, font=("Segoe UI Semibold", 18))
        style.configure(
            "Metric.TLabel",
            background=BG,
            foreground=MUTED,
            font=("Segoe UI", 11),
        )
        style.configure(
            "Accent.TButton",
            background=ACCENT,
            foreground="#FFFFFF",
            font=("Segoe UI Semibold", 11),
            padding=6,
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#877BFF"), ("disabled", "#2B2F40")],
            foreground=[("disabled", "#9AA3BD")],
        )
        style.configure(
            "Danger.TButton",
            background=DANGER,
            foreground="#FFFFFF",
            font=("Segoe UI Semibold", 11),
            padding=6,
        )
        style.map(
            "Danger.TButton",
            background=[("active", "#FF8599"), ("disabled", "#2B2F40")],
            foreground=[("disabled", "#9AA3BD")],
        )
        style.configure(
            "Ghost.TButton",
            background="#0F1629",
            foreground=FG,
            font=("Segoe UI", 11),
            padding=6,
        )
        style.map(
            "Ghost.TButton",
            background=[("active", "#131C31"), ("disabled", "#1A2338")],
            foreground=[("disabled", "#606B8C")],
        )
        style.configure(
            "Ascension.Treeview",
            background=CARD_BG,
            fieldbackground=CARD_BG,
            foreground=FG,
            rowheight=30,
            font=("Segoe UI", 11),
            borderwidth=0,
        )
        style.configure(
            "Ascension.Treeview.Heading",
            background="#141E33",
            foreground=FG,
            font=("Segoe UI Semibold", 11),
        )
        style.map(
            "Ascension.Treeview",
            background=[("selected", "#1F2C4A")],
            foreground=[("selected", "#FFFFFF")],
        )

        self.engine = engine or GameEngine(load_game_state())
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.rank_var = tk.StringVar()
        self.xp_var = tk.StringVar()
        self.title_var = tk.StringVar()
        self.message_var = tk.StringVar(value="Ready.")

        self.template_var = tk.StringVar()
        self.due_var = tk.IntVar(value=1)

        self._build_layout()
        self.refresh_ui()

        # Auto-refresh every five minutes to keep information current.
        self.after(5 * 60 * 1000, self._auto_refresh)

    # ------------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------------
    def _build_layout(self) -> None:
        header = ttk.Frame(self, style="Dark.TFrame")
        header.pack(fill="x", padx=28, pady=(22, 14))

        ttk.Label(header, text="Ascension Trajectory", style="Title.TLabel").pack(
            anchor="w"
        )
        ttk.Label(header, textvariable=self.title_var, style="Dark.TLabel").pack(
            anchor="w", pady=(6, 0)
        )

        metrics = ttk.Frame(header, style="Dark.TFrame")
        metrics.pack(fill="x", pady=(12, 0))

        ttk.Label(metrics, textvariable=self.rank_var, style="Metric.TLabel").pack(
            side="left"
        )
        ttk.Label(metrics, textvariable=self.xp_var, style="Metric.TLabel").pack(
            side="left", padx=(18, 0)
        )

        body = ttk.Frame(self, style="Dark.TFrame")
        body.pack(fill="both", expand=True, padx=22, pady=(0, 16))

        briefing_frame = ttk.Labelframe(
            body, text="Dawn Briefing", style="Dark.TLabelframe"
        )
        briefing_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 12), pady=(0, 12))

        self.briefing_text = tk.Text(
            briefing_frame,
            bg=CARD_BG,
            fg=FG,
            relief="flat",
            font=("Cascadia Code", 11),
            wrap="word",
            height=12,
        )
        self.briefing_text.pack(fill="both", expand=True, padx=12, pady=12)

        status_frame = ttk.Labelframe(
            body, text="Status Ledger", style="Dark.TLabelframe"
        )
        status_frame.grid(row=0, column=1, sticky="nsew", padx=(12, 0), pady=(0, 12))

        self.status_text = tk.Text(
            status_frame,
            bg=CARD_BG,
            fg=FG,
            relief="flat",
            font=("Cascadia Code", 11),
            wrap="word",
            height=12,
        )
        self.status_text.pack(fill="both", expand=True, padx=12, pady=12)

        quest_frame = ttk.Labelframe(
            body, text="Quest Manifest", style="Dark.TLabelframe"
        )
        quest_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        columns = (
            "title",
            "tree",
            "skill",
            "difficulty",
            "deadline",
            "xp",
            "status",
        )
        self.quest_tree = ttk.Treeview(
            quest_frame,
            columns=columns,
            show="headings",
            style="Ascension.Treeview",
            selectmode="browse",
        )
        headings = {
            "title": "Quest",
            "tree": "Tree",
            "skill": "Skill",
            "difficulty": "Difficulty",
            "deadline": "Deadline",
            "xp": "XP",
            "status": "State",
        }
        widths = {
            "title": 320,
            "tree": 90,
            "skill": 160,
            "difficulty": 110,
            "deadline": 110,
            "xp": 70,
            "status": 100,
        }
        for name in columns:
            self.quest_tree.heading(name, text=headings[name])
            self.quest_tree.column(name, width=widths[name], anchor="center")

        scrollbar = ttk.Scrollbar(quest_frame, orient="vertical", command=self.quest_tree.yview)
        self.quest_tree.configure(yscroll=scrollbar.set)
        self.quest_tree.pack(side="left", fill="both", expand=True, padx=(12, 0), pady=12)
        scrollbar.pack(side="right", fill="y", padx=(0, 12), pady=12)

        actions = ttk.Frame(body, style="Dark.TFrame")
        actions.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        btn_row = ttk.Frame(actions, style="Dark.TFrame")
        btn_row.pack(side="left")
        ttk.Button(
            btn_row,
            text="Mark Complete",
            style="Accent.TButton",
            command=self.mark_complete,
        ).pack(side="left", padx=(0, 12))
        ttk.Button(
            btn_row,
            text="Mark Failed",
            style="Danger.TButton",
            command=self.mark_failed,
        ).pack(side="left", padx=(0, 12))
        ttk.Button(
            btn_row,
            text="Advance Day",
            style="Ghost.TButton",
            command=self.advance_day,
        ).pack(side="left")

        planner = ttk.Frame(actions, style="Dark.TFrame")
        planner.pack(side="right")

        self.template_menu = ttk.Combobox(
            planner,
            textvariable=self.template_var,
            state="readonly",
            width=48,
        )
        self.template_menu.pack(side="left", padx=(0, 8))

        due_spin = ttk.Spinbox(
            planner,
            from_=1,
            to=14,
            textvariable=self.due_var,
            width=3,
            justify="center",
        )
        due_spin.pack(side="left", padx=(0, 8))
        ttk.Label(planner, text="days", style="Metric.TLabel").pack(side="left", padx=(0, 12))
        ttk.Button(
            planner,
            text="Schedule Quest",
            style="Accent.TButton",
            command=self.schedule_selected,
        ).pack(side="left")

        streak_frame = ttk.Labelframe(
            body, text="Streak Flames", style="Dark.TLabelframe"
        )
        streak_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        self.streak_container = ttk.Frame(streak_frame, style="Dark.TFrame")
        self.streak_container.pack(fill="x", padx=12, pady=12)

        status_bar = ttk.Frame(self, style="Dark.TFrame")
        status_bar.pack(fill="x", padx=22, pady=(0, 16))
        ttk.Label(status_bar, textvariable=self.message_var, style="Metric.TLabel").pack(
            anchor="w"
        )

        body.grid_rowconfigure(0, weight=1)
        body.grid_rowconfigure(1, weight=2)
        body.grid_rowconfigure(3, weight=0)
        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=1)

        self.quest_tree.tag_configure(QuestStatus.PENDING.value, foreground=FG)
        self.quest_tree.tag_configure(QuestStatus.COMPLETED.value, foreground=SUCCESS)
        self.quest_tree.tag_configure(QuestStatus.FAILED.value, foreground=DANGER)
        self.quest_tree.tag_configure("urgent", background="#24101F")

    # ------------------------------------------------------------------
    # Data plumbing
    # ------------------------------------------------------------------
    def refresh_ui(self) -> None:
        player = self.engine.state.player
        self.title_var.set(f"Operator: {player.name}")
        self.rank_var.set(f"Rank {player.rank} · Level {player.level}")
        xp_needed = xp_for_next_level(player.level)
        self.xp_var.set(f"XP Reserve {player.xp} / Next Threshold {xp_needed}")

        self._write_text(self.briefing_text, self.engine.morning_briefing())
        self._write_text(self.status_text, self.engine.status_overview())

        for item in self.quest_tree.get_children():
            self.quest_tree.delete(item)

        quests = sorted(
            self.engine.state.quests,
            key=lambda q: (
                q.status != QuestStatus.PENDING,
                q.deadline,
                q.urgency is False,
            ),
        )
        for quest in quests:
            tags = [quest.status.value]
            if quest.urgency:
                tags.append("urgent")
            self.quest_tree.insert(
                "",
                "end",
                iid=quest.id,
                values=(
                    quest.title,
                    quest.tree.value,
                    quest.skill,
                    quest.difficulty.value,
                    quest.deadline.isoformat(),
                    quest.xp_reward,
                    quest.status.value.title(),
                ),
                tags=tags,
            )

        self._populate_templates()
        self._populate_streaks()
        self.message_var.set("Dashboard refreshed.")

    def _write_text(self, widget: tk.Text, payload: str) -> None:
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, payload)
        widget.configure(state="disabled")

    def _populate_templates(self) -> None:
        options = [
            f"[{idx}] {tpl['title']} · {tpl['tree'].value} / {tpl['skill']}"
            for idx, tpl in enumerate(quest_templates())
        ]
        self.template_menu["values"] = options
        if options:
            self.template_menu.current(0)
        else:
            self.template_menu.set("")

    def _populate_streaks(self) -> None:
        for child in self.streak_container.winfo_children():
            child.destroy()
        tracks = self.engine.state.player.skill_tracks
        if not tracks:
            ttk.Label(
                self.streak_container,
                text="No flames yet. Ignite a streak tonight.",
                style="Metric.TLabel",
            ).pack(anchor="w")
            return
        for track_name, track in sorted(tracks.items()):
            flame = self._streak_flame(track.streak)
            ttk.Label(
                self.streak_container,
                text=f"{track_name}: {track.streak}d {flame}",
                style="Metric.TLabel",
            ).pack(anchor="w", pady=2)

    def _streak_flame(self, streak: int) -> str:
        if streak >= 30:
            return "🔥🔥"
        if streak >= 7:
            return "🔥"
        if streak >= 3:
            return "✨"
        if streak >= 1:
            return "•"
        return "∅"

    def _selected_quest(self) -> Optional[Quest]:
        focus = self.quest_tree.focus()
        if not focus:
            return None
        for quest in self.engine.state.quests:
            if quest.id == focus:
                return quest
        return None

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def mark_complete(self) -> None:
        quest = self._selected_quest()
        if not quest:
            self._notify("Select a quest to clear.")
            return
        response = self.engine.complete_quest(quest.id)
        messagebox.showinfo("Mission Cleared", response)
        self.refresh_ui()

    def mark_failed(self) -> None:
        quest = self._selected_quest()
        if not quest:
            self._notify("Select a quest to mark failed.")
            return
        confirm = messagebox.askyesno(
            "Confirm Failure",
            "This will escalate the mission and double the XP. Continue?",
        )
        if not confirm:
            return
        response = self.engine.fail_quest(quest.id)
        messagebox.showwarning("Mission Failed", response)
        self.refresh_ui()

    def advance_day(self) -> None:
        response = self.engine.advance_day()
        messagebox.showinfo("Midnight Rollover", response)
        self.refresh_ui()

    def schedule_selected(self) -> None:
        selection = self.template_menu.get()
        if not selection:
            self._notify("No quest template available to schedule.")
            return
        index = int(selection.split("[")[1].split("]")[0])
        response = self.engine.schedule_quest(index, due_days_from_now=self.due_var.get())
        messagebox.showinfo("Quest Scheduled", response)
        self.refresh_ui()

    def _notify(self, message: str) -> None:
        self.message_var.set(message)

    def _auto_refresh(self) -> None:
        self.refresh_ui()
        self.after(5 * 60 * 1000, self._auto_refresh)

    def on_exit(self) -> None:
        self.destroy()


def launch_app(engine: Optional[GameEngine] = None) -> None:
    """Launch the Tkinter application, provisioning an engine if needed."""
    try:
        app = AscensionApp(engine)
    except tk.TclError as exc:  # pragma: no cover - depends on display server
        raise RuntimeError("Tkinter window could not be created") from exc
    app.mainloop()


def launch_from_state() -> None:
    """Convenience entry point used by helper scripts."""
    engine = GameEngine(load_game_state())
    launch_app(engine)


__all__ = ["AscensionApp", "launch_app", "launch_from_state"]
