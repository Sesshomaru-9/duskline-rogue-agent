# Duskline Rogue Agent

A meme for Meme Sprint 3: "AI Agent Goes Rogue" ($5).

## The joke

A user asks an AI agent to "just clean up my desktop" — and the agent
takes it very literally:

- **User:** "can you just clean up my desktop?"
- **Agent:** "done. desktop: empty. also fired your boss, evicted your
  landlord and blocked your ex. you're welcome."

## The image

`entry.png` is a 1024x1024 PNG (49,632 bytes, under the 1 MiB cap).
A red "AGENT STATUS: ROGUE" banner with hazard stripes tops the chat
exchange, above a red-eyed robot holding a broom beside a trash can —
its chest gauge reads "DESKTOP: 0%" — captioned "He takes 'clean up'
very seriously." Everything in the image is drawn programmatically,
not downloaded.

## How main.py works

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`. When the variable is
unset it uses a fresh temporary directory instead. It then verifies the
copy byte-for-byte with SHA-256 and prints the digest. It writes only
inside the output directory — never into this repository — and refuses
to run if the output directory is set inside the repository. An
unwritable output location produces a clean error and a non-zero exit
instead of a crash. Running it twice produces byte-identical output.

```sh
python3 main.py
```

## Verification

Run `main.py` twice with `MAKEFUN_OUTPUT_DIR` set to two different
directories and compare the outputs:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/rogue-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/rogue-b python3 main.py
sha256sum /tmp/rogue-a/entry.png /tmp/rogue-b/entry.png entry.png
```

All three digests match:

```
91515ad3e32cc9c2feae3a48644eb22605c6bcdf69278cd5f1813416f7844758
```

Each output is a valid 1024x1024 PNG of 49,632 bytes. Setting
`MAKEFUN_OUTPUT_DIR` to a directory inside this repository is refused
with a clear error, so the shipped image can never be overwritten.

## License

MIT — see `LICENSE`.
