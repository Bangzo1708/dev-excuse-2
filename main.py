#!/usr/bin/env python3
"""Round-2 entry: Make the AI Judge Laugh — Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. Deterministic, no network, no randomness.

Winner of 3 drafted candidates (judged on the brief's own criteria):
  1. "The AI wrote the code, I approved the PR in four seconds, and now
     we're both calling it a learning opportunity."  <-- CHOSEN
     Most on-theme, freshest (2026 AI-coding reality, not a worn excuse),
     twist a developer recognises (the PR was approved unread), sounds
     like something a dev would actually say, lands fast.
  2. "The bug had a test. The test was skipped in 2021. Nobody asked
     why until today."  (strong twist, but drier; less of a laugh)
  3. "I fixed it by reverting my fix, which undid the bug my fix
     introduced - so my original code was the bug all along."
     (clever loop, but takes a second read to land; weaker first hit)
"""

import os

LINE = (
    "The AI wrote the code, I approved the PR in four seconds, "
    "and now we're both calling it a learning opportunity."
)


def main() -> None:
    # Gate guard: the entry must be 1-200 chars, one line, no newline.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be single-line"
    assert LINE.strip() == LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
