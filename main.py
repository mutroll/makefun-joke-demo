#!/usr/bin/env python3
"""Writes one joke about working beside an AI coding agent during a live demo.

The joke is the entry: one line, about an agent rewriting the demo app and
crashing it faster. Deterministic, Python 3.13 standard library only, no
network access.
"""

from pathlib import Path

JOKE = (
    "Mid-demo, my coding agent 'fixed' the crash by rewriting the app "
    "\u2014 now it crashes faster, with better comments."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 code points"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(JOKE.encode("utf-8"))
    # Read the file back and confirm the bytes are exactly what we intended:
    # no trailing newline, no re-encoding drift, the joke and nothing else.
    assert target.read_bytes() == JOKE.encode("utf-8")
    assert target.read_text(encoding="utf-8") == JOKE


if __name__ == "__main__":
    main()
