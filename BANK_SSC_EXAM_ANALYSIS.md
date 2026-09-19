# SBI Clerk, SSC CGL, and IBPS RRB Clerk Analysis

This package is intentionally separate from the GSSSB tools. It provides **10
dedicated prelims model papers per exam**:

- `bank_ssc_model_papers.py` generates the papers.
- `bank_ssc_exam_blueprints.json` stores the exam-specific pattern and syllabus.
- Generated papers are written to `bank_ssc_model_papers/<exam_key>/`.

## Verified recent patterns

| Exam | Model stage | Sections | Questions | Marks | Time | Negative marking |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| SBI Clerk | Prelims | English 30, Numerical 35, Reasoning 35 | 100 | 100 | 60 min | 0.25 |
| SSC CGL | Tier-I | Reasoning 25, General Awareness 25, Quant 25, English 25 | 100 | 200 | 60 min | 0.50 |
| IBPS RRB Office Assistant | Prelims | Reasoning 40, Numerical 40 | 80 | 80 | 45 min | 0.25 |

The exact notification for the recruitment cycle is the authority. Patterns can
change, so verify the latest notice before attempting the actual exam.

## Syllabus and trend analysis

### SBI Clerk

Prelims preparation is weighted toward arithmetic and DI, puzzle/seating
reasoning, and grammar/vocabulary/RC. Mains additionally requires banking and
financial awareness, computer basics, and broader English/quant/reasoning
coverage. The current blueprint records the recent mains structure separately.

### SSC CGL

Tier-I is balanced across four sections. Recurring preparation priorities are
arithmetic, geometry/mensuration, grammar and vocabulary, series/coding, and
polity/economy/science. Tier-II is post-dependent: Paper-I is common for most
posts, while Statistics and Finance/Economics papers apply only to specified
posts. Do not treat Tier-II as one identical paper for every candidate.

### IBPS RRB Clerk

Prelims is strongly speed-oriented: simplification/arithmetic and
puzzle/seating/inequality are the main scoring areas. Mains adds General
Awareness, banking awareness, language, and computer knowledge. The blueprint
stores the recent mains structure and syllabus additions.

## What the generated papers do

Each exam has 10 deterministic, separately seeded papers. The questions are
organized by the official section counts and draw from recurring syllabus
topics. Every question includes:

- section and topic
- difficulty label
- four options
- answer
- short explanation

The questions are **original practice questions**, not copied previous-paper
questions. Topic recurrence is useful for revision but cannot guarantee that an
exact question will appear in the exam. Current-affairs questions must be
updated from reliable sources near the exam date.

## Generate the papers

```powershell
python bank_ssc_model_papers.py
```

The command creates 60 files:

```text
bank_ssc_model_papers/
  sbi_clerk/
    paper_01.txt ... paper_10.txt
    paper_01.json ... paper_10.json
  ssc_cgl/
    paper_01.txt ... paper_10.txt
    paper_01.json ... paper_10.json
  ibps_rrb_clerk/
    paper_01.txt ... paper_10.txt
    paper_01.json ... paper_10.json
```

Each text paper contains questions, answer key, and solutions in one file.
JSON files are intended for applications or custom analytics.

## Sources

Official sources:

- [SBI Careers](https://sbi.co.in/web/careers/current-openings)
- [SSC](https://ssc.gov.in/)
- [IBPS](https://www.ibps.in/)

Recurring-topic observations were cross-checked against recent previous-paper
reviews from Adda247, BankersAdda, and Testbook. Those reviews are trend
evidence, not official guarantees.
