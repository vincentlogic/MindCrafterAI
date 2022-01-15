"""A light CLI wrapper for the Lightforge Sentinel modules."""

import argparse
import textwrap
from datetime import datetime
from typing import List

from src.idea_forge import IdeaForge
from src.logbook import AgentEntry, record_entry
from src.ops_notes import OPS_NOTES
from src.persistence import dump_entries, load_entries
from src.sample_agents import load_sample_agents


class SignalBoard:
    """Simple summary builder for recent agent activity."""

    def __init__(self):
        self.entries: List[AgentEntry] = []

    def add_entry(self, entry: AgentEntry) -> None:
        self.entries.append(entry)

    def snapshot(self, limit: int = 5) -> str:
        """Format a short status block that highlights recent moods."""

        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        selection = self.entries[-limit:]
        lines = [f"Signal Snapshot {now}"]
        for item in selection:
            lines.append(f"{item.timestamp} | {item.name} | {item.focus} | {item.mood}")
        return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sentinel",
        description="Play with the Lightforge Sentinel idea forge and logbook",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prompt = subparsers.add_parser("prompt", help="forge a fresh concept")
    prompt.add_argument("-n", "--count", type=int, default=1, help="how many prompts to forge")

    log = subparsers.add_parser("log", help="record a mock agent entry")
    log.add_argument("name", help="agent handle")
    log.add_argument("focus", help="what they are exploring")
    log.add_argument("mood", help="current mood")

    board = subparsers.add_parser("board", help="render the signal board summary")
    board.add_argument("--limit", type=int, default=4, help="how many entries to show")

    agents = subparsers.add_parser("agents", help="view the sample agent roster")
    agents.add_argument("--details", action="store_true", help="show each agent's focus and mood")

    notes = subparsers.add_parser("notes", help="read the ops notes and tiny wins")
    notes.add_argument("--brief", action="store_true", help="list each note on one line")

    return parser


def main(argv: List[str] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    forge = IdeaForge()
    entries: List[AgentEntry] = load_entries()
    board = SignalBoard()

    for entry in entries:
        board.add_entry(entry)

    if args.command == "prompt":
        for _ in range(args.count):
            prompt = forge.forge()
            print(prompt)
    elif args.command == "log":
        entry = record_entry(entries, args.name, args.focus, args.mood)
        board.add_entry(entry)
        dump_entries(entries)
        print(textwrap.fill(entry.focus, width=60))
    elif args.command == "board":
        print(board.snapshot(limit=args.limit))
    elif args.command == "agents":
        roster = load_sample_agents()
        for agent in roster:
            if args.details:
                print(f"{agent.name}: {agent.focus} [{agent.mood}]")
            else:
                print(agent.name)
    elif args.command == "notes":
        for note in OPS_NOTES:
            if args.brief:
                print(f"{note.date} | {note.tactic}")
            else:
                print(f"{note.date} | {note.tactic} -> {note.outcome}")
