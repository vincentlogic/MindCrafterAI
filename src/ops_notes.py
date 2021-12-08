"""Ops notes that capture the tiny wins of Lightforge Sentinel evenings."""

from dataclasses import dataclass
from typing import List


@dataclass
class OpsNote:
    date: str
    tactic: str
    outcome: str


OPS_NOTES: List[OpsNote] = [
    OpsNote(
        date="2021-06-12",
        tactic="sketch CLI flow without running scripts",
        outcome="boilerplate and docs outlined well enough to keep moving",
    ),
    OpsNote(
        date="2021-07-19",
        tactic="persist log entries to JSON",
        outcome="board snapshot can now load previous evenings",
    ),
    OpsNote(
        date="2021-09-01",
        tactic="add sample roster",
        outcome="new command to recall imagined agents",
    ),
]
