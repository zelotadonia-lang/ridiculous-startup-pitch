"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea to /output/entry.txt.

The pitch: pigeons carry encrypted USB sticks between air-gapped offices,
and law firms pay per flight — because the bird is the only delivery no
hacker can intercept, the absurdity itself is the revenue engine.
"""

import os

PITCH = (
    "We train pigeons to carry encrypted USB sticks between air-gapped "
    "offices, so law firms pay per flight for the only delivery no hacker "
    "can intercept."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-200 characters, not whitespace
    # only. Check here so a bad pitch fails loudly at build time instead
    # of silently scoring 0 after submission.
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(
            f"pitch must be 1-200 characters, got {len(PITCH)}"
        )
    if not PITCH.strip():
        raise ValueError("pitch must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
