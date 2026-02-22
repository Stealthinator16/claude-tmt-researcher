# TMT Research Pipeline - Quick Start

## How to Run

### Option 1: Direct Command (Recommended)
Open Claude Code in this project directory and say:
```
Research TMT article ideas on [your topic]
```

Claude will automatically follow the CLAUDE.md instructions.

### Option 2: Skill Command
```
/tmt-research [your topic]
```

### Option 3: Step-by-Step Manual Control
If you want more control over each phase:

**Phase 1: Discovery**
```
1. Brainstorm ideas on [topic] - use the brainstormer prompt
2. Check novelty of [idea] - for each promising idea
3. Deep research on [idea] - for ideas that pass novelty
4. Validate citations for [idea]
```

**Phase 2: Argument Building**
```
5. Build argument for [researched idea]
6. Validate argument structure
7. Final review - apply Bhatia bar
```

**Save Work**
```
Save all work to output folder
```

## Project Structure

```
claude-tmt-researcher/
├── CLAUDE.md                           # Main pipeline instructions (AUTO-LOADED)
├── src/tmt_researcher/config/prompts/  # Detailed agent prompts
│   ├── brainstormer.md
│   ├── novelty_checker.md
│   ├── researcher.md
│   ├── validator.md
│   ├── argument_architect.md
│   ├── argument_validator.md
│   └── reviewer.md
├── output/
│   ├── approved/                       # Successful articles
│   └── rejected/                       # Failed ideas (with research preserved)
└── .claude/skills/                     # Skill definitions
```

## Quality Reminders

- **Depth >>> Surface-level insight**
- **Novelty >>> Quantity**
- **Every claim must be cited**
- Most ideas SHOULD be rejected
- Even ONE truly original idea is a success
