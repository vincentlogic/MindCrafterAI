"""Sample agents to inspire the Lightforge Sentinel logbook."""

from typing import List

from src.logbook import AgentEntry

SAMPLE_AGENT_DEFS = [
    {
        "name": "NyxByte",
        "focus": "Midnight observatory notes on moss-lit constellations",
        "mood": "pensieve",
    },
    {
        "name": "CinderRun",
        "focus": "Testing signal relays in abandoned transit tunnels",
        "mood": "tense",
    },
    {
        "name": "VelvetNode",
        "focus": "Scribing whispers from kinetic gardens",
        "mood": "calm",
    },
]


def load_sample_agents() -> List[AgentEntry]:
    """Return fresh AgentEntry instances for tomorrow's logbook practice."""

    return [AgentEntry(**entry) for entry in SAMPLE_AGENT_DEFS]
