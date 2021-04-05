"""Simple tracking helpers for the agent logbook."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class AgentEntry:
    """Represents a single entry in the logbook."""

    name: str
    focus: str
    mood: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


def record_entry(entries: List[AgentEntry], name: str, focus: str, mood: str) -> AgentEntry:
    """Add a new entry to the list and return it."""

    entry = AgentEntry(name=name, focus=focus, mood=mood)
    entries.append(entry)
    return entry
