# TMT Law Research Pipeline

A Claude Code-powered pipeline for generating novel, legally accurate TMT (Technology, Media, Telecommunications) law article ideas focused on India.

## Quality Philosophy

**Depth >>> Surface-level insight**
**Novelty >>> Quantity**

The pipeline aims for Gautam Bhatia-level legal scholarship. Most ideas are REJECTED — that's by design. Only truly original, well-researched ideas pass through.

## How It Works

Open Claude Code in this project directory. The `CLAUDE.md` file is loaded automatically and defines the full pipeline:

```
Research TMT article ideas on [your topic]
```

Claude runs a multi-stage pipeline with specialized sub-agents:

1. **Brainstorm** — Generate 5-7 topic hypotheses
2. **Novelty Check** — Search Indian law blogs, law firms, academic sources — REJECT if already covered
3. **Deep Research** — Gather primary sources, build citation base
4. **Validation** — Verify all citations and legal accuracy
5. **Argument Building** — Construct thesis, step-by-step argument, counterarguments
6. **Final Review** — Apply the "Bhatia bar" — is this publishable scholarship?

Approved ideas are saved to `output/approved/`. Rejected ideas (with all research preserved) go to `output/rejected/`.

## Results

Across 6 sessions (Feb 2026): 52 ideas brainstormed, 25 approved, average quality score 4.04/5. See `output/session-log.md` for the full decision guide.

## Project Structure

```
claude-tmt-researcher/
├── CLAUDE.md                           # Pipeline instructions (auto-loaded by Claude Code)
├── src/tmt_researcher/config/prompts/  # Agent prompt templates
│   ├── brainstormer.md
│   ├── novelty_checker.md
│   ├── researcher.md
│   ├── validator.md
│   ├── argument_architect.md
│   ├── argument_validator.md
│   └── reviewer.md
└── output/                             # Research output (gitignored)
    ├── approved/                       # Passed all stages
    ├── rejected/                       # Failed with research preserved
    └── session-log.md                  # Decision guide for all articles
```

## Requirements

- [Claude Code](https://claude.ai/code) (uses Claude Max subscription — no API key needed)

## License

MIT
