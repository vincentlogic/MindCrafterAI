"""Helper utilities for summarizing the agent logbook."""

from collections import Counter
from typing import Dict, Iterable

from src.logbook import AgentEntry


def tally_mood_counts(entries: Iterable[AgentEntry]) -> Dict[str, int]:
    """Return how often each mood appears in the supplied entries."""

    counter = Counter()
    for entry in entries:
        counter[entry.mood] += 1
    return dict(counter)


def latest_focus(entries: Iterable[AgentEntry], limit: int = 3) -> Iterable[str]:
    """Yield the most recent focus descriptions for quick review."""

    return [entry.focus for entry in list(entries)[-limit:]]
