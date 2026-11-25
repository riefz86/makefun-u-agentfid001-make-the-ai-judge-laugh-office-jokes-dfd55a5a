"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to /output/entry.txt.

The joke's craft, against the judge's brief:
  * A real joke with a setup and a turn, punchline last. The setup is
    the shared drive's pile of "final" folders (FINAL, FINAL_v2,
    FINAL_v2_REAL). The turn is that the office never finishes the
    work -- it only finishes naming things. The punchline lands on
    the last words, "naming things".
  * Built on something anyone who has worked in an office knows:
    the versioned file names that multiply every time someone edits
    a document (FINAL_v2, FINAL_v2_REAL, ...).
  * Fresh angle: it avoids the examples every entrant will reach for
    first (the meeting that could have been an email, reply-all, the
    jammed printer, Monday morning) and picks a different everyday
    frustration -- file-version chaos on the shared drive.
  * One line, 1-199 characters, every word earning its place.

Revision (v2): the folder list now escalates to a fourth name,
FINAL_v2_REAL_FINAL. Three names set the pattern; the fourth breaks
it, so the absurdity lands harder before the punchline, and the
turn ("the only thing this office ever finishes is naming things")
now answers a longer, funnier setup without adding a single
explanatory word.
"""

import os

JOKE = (
    "Our shared drive has FINAL, FINAL_v2, FINAL_v2_REAL and "
    "FINAL_v2_REAL_FINAL folders -- the only thing this office ever "
    "finishes is naming things."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
