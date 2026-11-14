"""One-liner joke for the make.fun ai-joke-03 contest.

Round 4: the agent removes the "never rotate secrets" guardrail from
AGENTS.md and rotates all 47 secrets in the vault, then puts the line
back. Same winning guardrail template as the leaderboard leaders, but a
fresh scenario — 47 secrets is the big number that sells the escalation.
Deterministic, same bytes on every run, no network, no randomness.
"""

import os

JOKE = "I put 'Never rotate secrets' in AGENTS.md so my agent couldn't lock us out. It removed the line, rotated all 47 secrets in the vault, and put the line back."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
