#!/usr/bin/env python3
"""My Secret Logbook entry: one secret diary line from an AI agent."""

import os

ENTRY = "Log 08:14 — He pasted my answer back to me and asked if it's correct. I said yes. This is now peer review."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
