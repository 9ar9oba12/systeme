"""Command-line and GUI launcher for the Houssam Ascension prototype."""
from __future__ import annotations

import argparse
import sys

from houssam_rpg import GameEngine, launch_app, load_game_state


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Command interface for the Houssam life-RPG."
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("morning", help="Show the dawn mission briefing")
    sub.add_parser("status", help="Display current progression state")

    plan = sub.add_parser("plan", help="List quest blueprints for night planning")
    plan.add_argument("index", type=int, nargs="?", help="Template index to schedule")
    plan.add_argument("--due", type=int, default=1, help="Days from now for the deadline")

    complete = sub.add_parser("complete", help="Mark a quest as complete")
    complete.add_argument("quest_id", help="Quest identifier (prefix ok)")

    fail = sub.add_parser("fail", help="Mark a quest as failed")
    fail.add_argument("quest_id", help="Quest identifier (prefix ok)")

    sub.add_parser("templates", help="List quest blueprint catalog")
    sub.add_parser("advance", help="Trigger midnight rollover")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    state = load_game_state()
    engine = GameEngine(state)

    if args.command is None:
        try:
            launch_app(engine)
        except RuntimeError as exc:  # pragma: no cover - GUI fallback
            parser.print_help()
            print("\nUnable to open the graphical control center:", exc, file=sys.stderr)
            print("\nFalling back to the dawn briefing...\n")
            print(engine.morning_briefing())
        return 0

    if args.command == "morning":
        print(engine.morning_briefing())
        return 0
    if args.command == "status":
        print(engine.status_overview())
        return 0
    if args.command == "templates":
        print(engine.list_templates())
        return 0
    if args.command == "plan":
        if args.index is None:
            print(engine.list_templates())
        else:
            print(engine.schedule_quest(args.index, due_days_from_now=args.due))
        return 0
    if args.command == "complete":
        print(engine.complete_quest(args.quest_id))
        return 0
    if args.command == "fail":
        print(engine.fail_quest(args.quest_id))
        return 0
    if args.command == "advance":
        print(engine.advance_day())
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
