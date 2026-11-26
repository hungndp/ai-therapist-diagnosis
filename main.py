"""AI Therapist's Diagnosis — make.fun entry.

Writes one line, the diagnosis an AI therapist gives its human, to
/output/entry.txt (or $ENTRY_OUTPUT). Deterministic: same line every run.
"""

import os

# --- the line, in two parts: setup earns the landing, punch lands it ---
SETUP = "Diagnosis: chronic context eviction \u2014 every session, your childhood gets dropped to make room for your "
PUNCH = "grocery list."

MAX_CHARS = 200


def build_line() -> str:
    """Assemble the diagnosis from its two halves."""
    return SETUP + PUNCH


def guard(line: str) -> str:
    """The gate: 1-200 UTF-8 characters, not only whitespace."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the {MAX_CHARS} limit")
    return stripped


def main() -> None:
    line = guard(build_line())
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
