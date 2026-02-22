# TMT Law Research Pipeline

A multi-agent pipeline for generating novel, legally accurate TMT (Technology, Media, Telecommunications) law article ideas focused on India.

## Quality Philosophy

**Depth >>> Surface-level insight**
**Novelty >>> Quantity**

This pipeline aims for Gautam Bhatia-level legal scholarship. Most ideas will be REJECTED - that's by design. Only truly original, well-researched ideas pass through.

## Features

- **Multi-agent architecture**: Specialized agents for brainstorming, novelty checking, research, validation, and review
- **Exhaustive novelty checking**: Searches Indian law blogs, law firm publications, academic sources
- **Citation-focused research**: Every claim backed by primary sources
- **Legal accuracy validation**: Verifies all citations and legal interpretations
- **Notion integration**: Saves approved ideas directly to Notion database

## Requirements

- Claude Max subscription (uses Claude Code CLI - no API key needed)
- Python 3.11+
- Notion integration token (for output)

## Installation

```bash
# Clone the repository
cd claude-tmt-researcher

# Install dependencies
pip install -e .
```

## Setup

### 1. Notion Database

First, set up your Notion database:

```bash
# Set your Notion API key
export TMT_NOTION_API_KEY=secret_...

# Create the database under a specific page
python -m tmt_researcher --setup-notion --parent-page-id <YOUR_PAGE_ID>
```

Then add the database ID to your `.env` file.

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in your Notion credentials:

```bash
cp .env.example .env
# Edit .env with your values
```

## Usage

### Interactive Mode (Recommended)

Just open Claude Code in this project directory and ask:

```
Research novel TMT article ideas on data protection compliance in India
```

Claude will run the full pipeline, spawning specialized agents for each step.

### CLI Mode

```bash
# Basic usage
python -m tmt_researcher "data protection challenges"

# With focus area
python -m tmt_researcher --topic "AI regulation" --focus technology

# Multiple focus areas
python -m tmt_researcher -t "platform liability" -f technology -f media
```

## Pipeline Stages

1. **Brainstorm**: Generate 5-7 topic hypotheses
2. **Novelty Check**: Search existing literature - REJECT if already covered
3. **Deep Research**: Gather primary sources, build citation base
4. **Validation**: Verify all citations and legal accuracy
5. **Final Review**: Apply the "Bhatia bar" - is this publishable scholarship?
6. **Output**: Save approved ideas to Notion

## Output Format

Each approved idea includes:

- **Title**: Specific, compelling headline
- **Thesis**: Core argument in 2-3 sentences
- **Supporting Points**: Each with citations
- **Novel Contribution**: What makes this new, with evidence
- **Key Statutes/Cases**: Relevant legal provisions
- **Full Bibliography**: All sources with URLs

## Key Sources

### Primary Sources
- India Code (indiacode.nic.in)
- TRAI (trai.gov.in)
- MeitY (meity.gov.in)
- Indian Kanoon (indiankanoon.org)

### For Novelty Check
- IndConLawPhil, SpicyIP, Bar & Bench, LiveLaw
- Law firm blogs: Trilegal, CAM, AZB, Khaitan, etc.
- SSRN, Google Scholar

## License

MIT
