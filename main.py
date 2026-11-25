#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single original roast line about the entrant's own smart
fridge to /output/entry.txt. Deterministic: the same bytes on every
run, no randomness, no clock, no network, stdlib only.
"""

import os

ROAST = (
    "My smart fridge texts me that I'm out of eggs while I'm "
    "standing in front of it holding the eggs."
)


def main() -> None:
    # One line, no trailing newline: the file holds exactly the roast,
    # nothing else, so the gate sees a single line of 97 characters.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
