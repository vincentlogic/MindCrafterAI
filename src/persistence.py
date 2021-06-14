"""Light persistence helpers to keep CLI output in a tiny journal."""

import json
from pathlib import Path
from typing import Iterable

from src.logbook import AgentEntry

STORAGE_FILE = Path("data/agent_journal.json")


def ensure_storage() -> None:
    """Ensure the storage directory exists."""

    STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)


def dump_entries(entries: Iterable[AgentEntry]) -> None:
    """Serialize entries to disk without running anything complex."""

    ensure_storage()
    as_dict = [entry.__dict__ for entry in entries]
    STORAGE_FILE.write_text(json.dumps(as_dict, indent=2))


def load_entries() -> list[AgentEntry]:
    """Load previously recorded entries back into memory."""

    if not STORAGE_FILE.exists():
        return []
    raw = json.loads(STORAGE_FILE.read_text())
    return [AgentEntry(**item) for item in raw]
