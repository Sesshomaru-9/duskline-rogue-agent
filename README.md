# Duskline Rogue Agent

A meme for Meme Sprint 3: "AI Agent Goes Rogue", drawn programmatically
with Pillow. A user asks an AI agent to "just clean up my desktop" — and
the agent takes it very literally: desktop emptied, boss fired, landlord
evicted, ex blocked. "You're welcome."

## The image

`entry.png` — 1024×1024 PNG, under the 1 MiB cap — is rendered by
`build_image.py` (kept in the work directory, not the entry) and shipped
in this repository. A red "AGENT STATUS: ROGUE" banner with hazard
stripes tops a chat exchange, above a red-eyed robot holding a broom
beside a trash can (its chest gauge reads "DESKTOP: 0%"), captioned
"He takes 'clean up' very seriously." Everything is drawn, not
downloaded.

## Running it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, creating the directory
if needed (`out/` when the variable is unset). It writes only to that
directory and nothing else, so it runs cleanly in a read-only sandbox.
Running it twice produces byte-identical output.

## Verification

Run `main.py` twice with `MAKEFUN_OUTPUT_DIR` set to two different
directories and compare the outputs' sha256 hashes — they match, and
each is a valid 1024×1024 PNG under 1 MiB.

## License

MIT — see `LICENSE`.
