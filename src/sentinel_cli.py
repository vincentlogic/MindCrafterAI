"""A light CLI wrapper for the Lightforge Sentinel modules."""

import argparse
import textwrap
from datetime import datetime
from typing import List

from src.idea_forge import IdeaForge
from src.logbook import AgentEntry, record_entry


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

    return parser


def main(argv: List[str] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    forge = IdeaForge()
    entries: List[AgentEntry] = []
    board = SignalBoard()

    if args.command == "prompt":
        for _ in range(args.count):
            prompt = forge.forge()
            print(prompt)
    elif args.command == "log":
        entry = record_entry(entries, args.name, args.focus, args.mood)
        board.add_entry(entry)
        print(textwrap.fill(entry.focus, width=60))
    elif args.command == "board":
        print(board.snapshot(limit=args.limit))
