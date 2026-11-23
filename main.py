#!/usr/bin/env python3
"""The Vacuum's Alibi entry (make.fun program/v1).

Writes one original line — the excuse a robot vacuum gives for
missing a spot — to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``).
"""

import os

LINE = (
    "Charging dock records show I was plugged in from 22:00 to 06:00 "
    "\u2014 the dust under the sofa can testify I never left."
)


def main() -> None:
    # Gate guard: the entry must be UTF-8 text of 1 to 200 characters,
    # on a single line and not only white space. Refuse rather than
    # write an invalid entry.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or not LINE.strip():
        raise SystemExit("entry fails the 1-200 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
