"""ai-joke-03 entry: write one one-liner about AI coding agents.

The output is byte-exact and deterministic: the same joke, written the
same way on every run, with no network and no randomness.
"""
import os

JOKE = "My AI agent's favorite debugging tool is confidence: it has never once been right, and never once been unsure."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
