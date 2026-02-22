# TMT Law Research Pipeline

This project is a multi-agent pipeline for generating novel, legally accurate TMT (Technology, Media, Telecommunications) law article ideas focused on India.

## Quality Philosophy

**Depth >>> Surface-level insight**
**Novelty >>> Quantity**

The goal is Gautam Bhatia-level legal scholarship. Each article idea must:
- Offer genuinely NOVEL legal arguments (not already published elsewhere)
- Be legally accurate with proper citations
- Provide deep analysis, not surface commentary
- Have a CONSTRUCTIBLE ARGUMENT - not just identify a gap, but build a defensible thesis

Even ONE truly original idea is better than ten generic ones. Most ideas should be REJECTED.

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PHASE 1: DISCOVERY                            │
├─────────────────────────────────────────────────────────────────────────┤
│  BRAINSTORMER ──► NOVELTY CHECKER ──► DEEP RESEARCHER ──► VALIDATOR    │
│       │                  │                    │                │        │
│       ▼                  ▼                    ▼                ▼        │
│  [5-7 ideas]    [Filter duplicates]   [Gather sources]  [Verify cites] │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHASE 2: ARGUMENT BUILDING                       │
├─────────────────────────────────────────────────────────────────────────┤
│  ARGUMENT ARCHITECT ──► ARGUMENT VALIDATOR ──► FINAL REVIEWER          │
│          │                      │                     │                 │
│          ▼                      ▼                     ▼                 │
│  [Build thesis &         [Check each claim      [Bhatia bar:           │
│   step-by-step            has citation]          Is this publishable?] │
│   argument]                                                             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
            [ARGUMENT WORKS]               [ARGUMENT FAILS]
                    │                               │
                    ▼                               ▼
            Save to output/                 Save partial work to
            approved/                       output/rejected/,
                                           request next topic
                                           from Phase 1
```

## How to Run the Pipeline

When the user asks to research TMT article ideas, follow this workflow:

---

### PHASE 1: DISCOVERY

#### Step 1: Brainstorm Initial Ideas
Spawn a brainstormer agent to generate 5-7 initial topic hypotheses based on the user's focus area.

#### Step 2: Novelty Check (CRITICAL)
For EACH idea, spawn a novelty checker agent that:
- Searches Indian law blogs: IndConLawPhil, SpicyIP, Bar & Bench, LiveLaw, Legally India
- Searches law firm publications: Trilegal, CAM, AZB, Khaitan, S&R, JSA
- Searches academic sources: SSRN, Google Scholar
- Searches government sources: TRAI papers, MeitY consultations

**REJECT the idea immediately if similar argument already exists.**
**SAVE rejected ideas to `output/rejected/` with research done so far.**

#### Step 3: Deep Research
For ideas that pass novelty check, spawn researcher agents to:
- Find and read actual statutory text (not summaries)
- Access primary sources: India Code, TRAI website, MeitY, Indian Kanoon
- Collect full citations for every claim
- Build comprehensive bibliography

#### Step 4: Legal Validation
Spawn validator agents to verify:
- Every citation actually exists and says what we claim
- Statutory interpretations are correct
- Case law is properly characterized
- No unsourced factual claims

**REJECT if any legal inaccuracy found.**
**SAVE rejected ideas to `output/rejected/` with all research.**

---

### PHASE 2: ARGUMENT BUILDING

#### Step 5: Argument Architecture
Spawn an argument architect agent to:
- Formulate a clear, defensible THESIS
- Build the argument step-by-step
- Each step must have supporting evidence with citation
- Anticipate and address counterarguments
- Structure for maximum persuasive impact

The argument should follow this structure:
1. **Setup**: Establish the legal context and why this matters
2. **Building Blocks**: Each claim builds on the previous, with citations
3. **The Turn**: The novel insight or interpretation
4. **Implications**: What follows from the argument
5. **Counterarguments**: Fair representation and response

#### Step 6: Argument Validation
Spawn an argument validator agent to verify:
- Every claim in the argument has a citation
- The logical flow is sound (no gaps, no leaps)
- Counterarguments are fairly represented
- The thesis is actually supported by the evidence
- No circular reasoning

**If argument cannot be constructed:**
- Save partial work to `output/rejected/`
- Request NEXT validated topic from Phase 1
- Loop until an arguable topic is found OR all topics exhausted

#### Step 7: Final Review
Apply the "Bhatia bar" - would this analysis be publishable in a serious legal blog?
- Is the argument compelling?
- Does it offer genuine insight?
- Is it substantive enough for a full article?
- Would an expert find this valuable?

---

### OUTPUT

Save ALL work to markdown files in the `output/` directory:

```
output/
├── approved/
│   └── [topic-slug]/
│       ├── article-idea.md          # Full article idea with complete argument
│       ├── research-notes.md        # All research gathered
│       ├── bibliography.md          # Complete source list with URLs
│       └── argument-structure.md    # Step-by-step argument breakdown
│
├── rejected/
│   └── [topic-slug]/
│       ├── idea-summary.md          # What the idea was
│       ├── rejection-reason.md      # Why rejected & at what stage
│       ├── research-notes.md        # Whatever research was completed
│       └── partial-work.md          # Any other work done
│
└── session-log.md                   # Summary of entire research session
```

---

## Output Format for Approved Ideas

### article-idea.md

```markdown
# [Title]

**Status**: Approved for writing
**Date**: [Date]
**Topic Area**: [Technology/Media/Telecommunications]

---

## Executive Summary

[2-3 paragraph summary of the argument for quick reading]

---

## Thesis

[Core argument stated clearly and precisely - what position are you taking?]

---

## Why This Matters

[Practical significance]
- Who is affected by this legal question?
- What are the real-world stakes?
- Why is this timely?

---

## The Argument

### Step 1: [Establishing the Legal Framework]

[Explanation of the relevant legal landscape]

**Supporting Evidence:**
1. [Claim]
   - **Citation**: [Full citation]
   - **Quote/Summary**: [Relevant text from source]

2. [Claim]
   - **Citation**: [Full citation]
   - **Quote/Summary**: [Relevant text]

---

### Step 2: [Identifying the Gap/Tension/Problem]

[Explanation of what's missing or conflicting in current law]

**Supporting Evidence:**
1. [Claim]
   - **Citation**: [Full citation]
   - **Quote/Summary**: [Relevant text]

---

### Step 3: [The Novel Interpretation/Argument]

[Your original contribution - the "turn" in the argument]

**Supporting Evidence:**
1. [Claim]
   - **Citation**: [Full citation]
   - **Quote/Summary**: [Relevant text]

**Author's Analysis:**
[Clearly marked analytical reasoning connecting the evidence to your thesis]

---

### Step 4: [Implications and Applications]

[What follows from your argument]

**Supporting Evidence:**
1. [Claim]
   - **Citation**: [Full citation]

---

## Counterarguments & Responses

### Counterargument 1: [State it fairly and strongly]

**Source/Basis**: [Where does this counterargument come from?]

**Response**:
[How your argument addresses this objection]

**Supporting Evidence:**
- **Citation**: [Source supporting your response]

---

### Counterargument 2: [Another objection]

**Source/Basis**: [Basis]

**Response**: [Response]

---

## Novel Contribution

**What makes this argument new:**
[Explain the original insight]

**Evidence of novelty (from search):**
- Searched [X sources] - no similar argument found
- Closest existing work: [Reference] - differs because [explanation]
- Gap in literature: [Description]

---

## Key Authorities

### Statutes
| Provision | Citation | Relevance to Argument |
|-----------|----------|----------------------|
| [Section X] | [Act Name, Year] | [How it supports the argument] |

### Cases
| Case | Citation | Relevance to Argument |
|------|----------|----------------------|
| [Case Name] | [Full citation] | [Key holding and relevance] |

### Regulations
| Regulation | Citation | Relevance to Argument |
|------------|----------|----------------------|
| [Regulation] | [Notification No., Date] | [Relevance] |

---

## Full Bibliography

### Primary Sources

1. [Author/Body], *[Title]*, [Citation details], [URL if available]
2. ...

### Secondary Sources

1. [Author], "[Title]", [Publication], [Date], [URL]
2. ...

### Sources Consulted But Not Cited

1. [Source] - [Why consulted, why not cited]

---

## Metadata

- **Total Citations**: [Number]
- **Primary Sources**: [Number]
- **Secondary Sources**: [Number]
- **Research Date**: [Date]
- **Pipeline Stage**: Approved
- **Quality Score**: [X/5]
```

---

## Output Format for Rejected Ideas

### idea-summary.md

```markdown
# [Title] - REJECTED

**Rejection Stage**: [Novelty Check / Research / Validation / Argument Building]
**Date**: [Date]

## The Idea

[What was the proposed topic/argument]

## Rejection Reason

[Detailed explanation of why this was rejected]

## Work Completed Before Rejection

[Summary of what was done]

## Salvageable Elements

[Any parts that might be useful for future research]
```

---

## Citation Requirements

| Claim Type | Required Citation Format |
|------------|-------------------------|
| Statutory provision | Section X, [Act Name], [Year] |
| Regulation | Rule X, [Regulation Name], Notification No. [X], dated [Date] |
| Case law | [Party v Party], [Year] [Volume] [Reporter] [Page] |
| TRAI document | TRAI [Type] No. [X] of [Year], dated [Date] |
| Government notification | [Ministry] Notification No. [X], dated [Date] |
| Statistics/data | [Source Report], [Publisher], [Year], p. [X] |
| Academic paper | [Author], "[Title]", [Journal] [Vol] ([Year]) |
| News/commentary | [Author], "[Title]", [Publication], [Date], [URL] |
| Author's analysis | Clearly marked as "Author's analysis:" or "It follows that..." |

**EVERY claim must be cited. No exceptions. Uncited claims = automatic rejection.**

---

## Key Indian TMT Law Sources

### Primary Sources
- **India Code** (indiacode.nic.in) - Central statutes
- **TRAI** (trai.gov.in) - Telecom regulations, consultation papers, recommendations
- **MeitY** (meity.gov.in) - IT policies, DPDP Act, Digital India
- **DoT** (dot.gov.in) - Telecom policies, licensing
- **Indian Kanoon** (indiankanoon.org) - Case law database
- **Gazette of India** - Official notifications

### Key Statutes
- Digital Personal Data Protection Act, 2023
- Digital Personal Data Protection Rules, 2025
- Information Technology Act, 2000
- IT (Intermediary Guidelines) Rules, 2021
- Telecommunications Act, 2023
- TRAI Act, 1997
- Cable Television Networks (Regulation) Act, 1995

### For Novelty Check
- IndConLawPhil (Indian Constitutional Law and Philosophy blog)
- SpicyIP (IP and tech law blog)
- Bar & Bench, LiveLaw, Legally India
- Medianama (tech policy)
- Law firm blogs: Trilegal, CAM, AZB, Khaitan, NDA, JSA

---

## Commands

User can say:
- **"Research TMT article ideas on [topic]"** - runs full pipeline (both phases)
- **"Check novelty of [idea]"** - runs just novelty check
- **"Deep research on [topic]"** - runs just research phase
- **"Build argument for [researched topic]"** - runs argument building phase
- **"Save all work"** - saves current state to markdown files
- **"Show rejected ideas"** - lists all rejected ideas with reasons
- **"Continue with next topic"** - if current argument fails, try next validated topic
