"""One Line, One Laugh.

One original funny line, at most 200 characters.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the joke at CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import hashlib
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


def validate_entry(joke: str) -> None:
    """Check the selected joke against the gate with explicit failures.

    Explicit SystemExit checks are used instead of assert so the gate
    still holds when Python runs with -O (which strips asserts).
    """
    if "\n" in joke or "\r" in joke:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(joke) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    if not joke.strip():
        raise SystemExit("entry must not be only whitespace")
    if joke != joke.strip():
        raise SystemExit("entry must not have edge whitespace")


def write_entry(joke: str) -> str:
    """Write the joke plus one newline, then read it back and verify.

    The read-back bytes must equal the intended UTF-8 bytes exactly and
    hash to the same sha256 digest. Returns the digest.
    """
    validate_entry(joke)
    intended = (joke + "\n").encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    with open(path, "rb") as handle:
        written = handle.read()
    if written != intended:
        raise SystemExit("entry.txt bytes differ from the intended entry")
    return hashlib.sha256(written).hexdigest()


def main() -> None:
    joke = CANDIDATES[SELECTED].strip()
    digest = write_entry(joke)
    print(f"{joke} [sha256 {digest}]")


if __name__ == "__main__":
    main()
