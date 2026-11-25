"""One Line, One Laugh.

One original funny line, at most 200 characters.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the joke at CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

CANDIDATES = [
    "I bought a standing desk to be healthier; now I sit on it.",
    "My Roomba got stuck under the couch, so now I pay a cleaner to rescue the cleaner.",
    "My phone's screen-time report called me brave for opening the same app 214 times.",
    "My calendar reminded me to relax, so I scheduled a meeting to discuss it.",
    "I keep a list of things to do tomorrow \u2014 it's the only thing I've finished every day for six years.",
    "My GPS said \"recalculating\" in the exact tone my mother uses when I disappoint her.",
    "I told my smart speaker I was lonely; it scheduled me a meeting with myself.",
    "My bank flagged my $4 coffee as suspicious but called my $900 flight to nowhere \"consistent with my spending\".",
    "I asked AI to write my wedding vows; it proposed to my laptop.",
    "My smartwatch congratulated me for standing up, which is the saddest applause I've ever received.",
]

# The sharpest cut: the setup promises virtue ("to be healthier") and the
# punchline defeats the desk's whole purpose in five words — the owner
# sits on the standing desk. It beat the Roomba candidate (same inversion
# shape, but "rescue the cleaner" needs a beat longer and 26 more
# characters) and the calendar candidate (a more familiar productivity
# joke) on economy: at 58 characters it is the shortest finalist, every
# word earns its place, and the turn lands on a first read.
SELECTED = 0


def main() -> None:
    joke = CANDIDATES[SELECTED].strip()
    assert "\n" not in joke, "entry must be a single line"
    assert 1 <= len(joke) <= 200, "entry must be 1 to 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(joke)


if __name__ == "__main__":
    main()
