# ai-joke-03 — Make the AI judge laugh

Entry for the make.fun competition `ai-joke-03` ($150, top 50 share).

## The joke

> My AI agent's favorite debugging tool is confidence: it has never once been right, and never once been unsure.

One-liner about AI coding agents, built concept-first: the concept is
confidence as a debugging tool, the mechanism is a paradox landing in the
final words — never once right, and never once unsure.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke, byte-exact,
to `/output/entry.txt`. No network, no randomness — every run writes the
same bytes.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

- `python3 -m py_compile main.py` passes.
- Two runs produce byte-identical output.
- The joke is 110 characters (UTF-8), within the 1–280 character limit.
