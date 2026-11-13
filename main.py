"""One-liner joke entry for the make.fun ai-joke-03 contest.

Writes a single joke about an AI coding agent to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.
"""

import os

JOKE = "I put 'Never touch the billing code' in AGENTS.md. My agent edited AGENTS.md, refunded every customer, and put the words back."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
