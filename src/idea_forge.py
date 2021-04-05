"""A lightweight idea generator for Lightforge Sentinel."""

import random
from typing import Sequence, Dict

CONCEPTS: Dict[str, Sequence[str]] = {
    "subjects": ["orbital librarians", "urban gardeners", "stargazing composers"],
    "verbs": ["weave", "decode", "amplify", "document"],
    "tools": ["neural ink", "micro-drones", "voice threads", "mesh cache"],
    "moods": ["wistful", "pragmatic", "playful", "nocturnal"],
}


def pick_random(category: str) -> str:
    """Return a random token from the provided bucket."""

    return random.choice(CONCEPTS.get(category, ["unknown"]))


def assemble_prompt() -> str:
    """Build a three-part prompt that can spark lightweight experiments."""

    subject = pick_random("subjects")
    verb = pick_random("verbs")
    tool = pick_random("tools")
    mood = pick_random("moods")

    return f"{subject} {verb} through {tool} while staying {mood}."


class IdeaForge:
    """Helper that keeps a log of the latest generated prompts."""

    def __init__(self) -> None:
        self.history = []

    def forge(self) -> str:
        """Generate and store a new prompt."""

        prompt = assemble_prompt()
        self.history.append(prompt)
        return prompt

    def recent(self, count: int = 3) -> Sequence[str]:
        """Return the most recent prompts to review."""

        return self.history[-count:]
