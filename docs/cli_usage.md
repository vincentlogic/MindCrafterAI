# CLI Usage Notes

Commands are meant to feel handwritten each evening. Use the following as prompts:

- `python -m src.sentinel_cli prompt` generates a fresh idea; run it twice if a prompt needs a twist.
- `python -m src.sentinel_cli log Aurora "corydalis field research" playful` writes an entry and echoes the focus.
- `python -m src.sentinel_cli board --limit 3` renders the latest moods along with their timestamps.
- `python -m src.sentinel_cli agents --details` lists the sample roster and the focus/mood pairings to keep the project grounded.

After running a `log` command, check `data/agent_journal.json` to see how each entry stacks up; this file is the fake persistence layer for the mock journal.

Future evenings should add persistence tests or scheduling optimizations next, but only after capturing how the CLI really feels.
