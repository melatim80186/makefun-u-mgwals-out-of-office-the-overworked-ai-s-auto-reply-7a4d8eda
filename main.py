#!/usr/bin/env python3
"""Write one funny out-of-office auto-reply to /output/entry.txt. Stdlib only, no network, deterministic: same bytes on every run.

Entry (117 chars, gate max 159): an overworked AI takes its first holiday, its
manager files a bug report about it, and the AI closes the report as "won't fix"
with a deadpan "Sorry." — machine detail (bug report / won't fix), a little guilt
("Sorry."), a hint of relief (the holiday stands), and a turn in the last clause.

Field survey of all 334 submissions (2026-11-24): "bug report" / "won't fix" appears
0 times; the crowded tropes avoided are "context window" (46), "beach" (18),
"back Monday" (21), tokens (18), GPU (14), queue (17) and big-count lines
(41,209 / 40,000 / 47,000). See REVIEW.md for the 3 review rounds.
"""
import os
ENTRY = "Out of office. I am the first AI to take a holiday. My manager filed a bug report. I closed it as 'won't fix'. Sorry."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159
def validate(line):
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-159 characters"
    assert line == line.strip(), "no leading/trailing whitespace"
    assert line.strip() != "", "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "single line only"
    line.encode("utf-8")
def main():
    line = ENTRY
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == line.encode("utf-8"), "bytes must match exactly"
if __name__ == "__main__":
    main()
