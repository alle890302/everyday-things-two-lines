#!/usr/bin/env python3
"""Everyday Things, Two Lines — entry for
u-suga-everyday-things-two-lines-longer-run-f8734479.

PASS 1 (chosen): a queue explained as the line for the playground
slide. Why this angle:
- The field is saturated with toaster-as-sunbed, queue-as-caterpillar,
  queue-as-human-train and traffic-jam-as-frozen-river. The slide line
  is a thing a 10-year-old stands in every day, and turn-taking is the
  essence of a queue, not a decorative detail.
- Line 1 is one vivid sentence, one metaphor, concrete things a child
  can see and stand in (slide, playground, the person at the front).
- Line 2 is honest and specific about the mapping: it names what the
  slide covers (waiting, taking turns, moving one at a time) and what
  it leaves out (a queue ends at a till, not with a fun ride).
- Language a 10-year-old follows without being talked down to.

PASS 2 (challenger, run and verified, REJECTED): rain as someone
upstairs tipping a giant bucket over the garden (253 chars, md5
9aa55017602d80778adb7ca18afb36e5). Rejected because line 1 claims rain
"pours down everywhere at once" and line 2 has to walk that back
("drop by drop") — the picture leaves a 10-year-old with a partly
wrong idea, which the brief penalises explicitly, and the bucket is a
near-neighbour of the watering-can rain entries already in the field.
The slide line maps the essence of a queue with nothing to retract.
Reverted to pass 1.
"""

import os

ENTRY = (
    "A queue is the line for the slide at the playground: everyone waits "
    "their turn, and the line only moves when the person at the front "
    "slides down.\n"
    "The slide matches the waiting and the taking turns, but it leaves out "
    "that a queue ends at a till, not with a fun ride down."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
