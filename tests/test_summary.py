from src.logbook import AgentEntry
from src.summary import latest_focus, tally_mood_counts


def make_entry(name: str, focus: str, mood: str) -> AgentEntry:
    return AgentEntry(name=name, focus=focus, mood=mood)


def test_tally_mood_counts_basic():
    entries = [make_entry("A", "Focus 1", "calm"), make_entry("B", "Focus 2", "calm"), make_entry("C", "Focus 3", "tense")]
    counts = tally_mood_counts(entries)
    assert counts["calm"] == 2
    assert counts.get("tense") == 1


def test_latest_focus_respects_limit():
    entries = [make_entry(str(i), f"Focus {i}", "playful") for i in range(5)]
    recent = latest_focus(entries, limit=2)
    assert recent == ["Focus 3", "Focus 4"]
