# 1. Workflow and prompts

## Always
- Say your own view first at three points (your reading of the task, the riskiest case, the
  shape), then let the AI argue. The recording shows you thinking, not just accepting.
- No code before a written plan you approve ("plan approved").
- After every change: run the tests, show the real output.
- When the AI is wrong, say so, fix it, and note it in the README's AI section.
- Ask the AI to explain each piece in two sentences; you will be asked to explain it later.

## Order (skip a step only when its question does not arise)
| Stage | Goal | Type |
|---|---|---|
| Rules | Set how the AI works | `Rules: small steps. No code until I type "plan approved". After every change run the tests and show the output. No bare except. Say when unsure.` |
| Understand | Know what is asked | `Read the task. My reading: ___. Critique it. List requirements R1.. quoting the task. List what is ambiguous.` |
| Questions | Close gaps | `Ask me your questions one at a time with your recommended answer. Record my answers as assumptions A1..` |
| Data first | See what you have | `Load the data with pandas. Show shape, column types, nulls, 5 rows, value counts of key columns, date range. No analysis yet.` |
| Documents | Write down what done means | see [2-documents.md](2-documents.md) |
| Models | Understand before building | see [3-models.md](3-models.md) |
| Off the shelf | Don't build what exists | `For each requirement, which installed library does it? Exact import and version. Write check_imports.py and run it.` |
| Shape | Pick the architecture | `I'd build it as ___ because ___. Argue against it.` then see [4-agents.md](4-agents.md) |
| Plan | Small checked steps | `Write PLAN.md: Goal; Done when (checkboxes); Steps, each naming its tests, riskiest case first; Assumptions; Risks.` |
| Build | One step at a time | `Implement step N only. Tests first. Run them and show the output. Explain it in two sentences.` |
| Evaluate | Prove it works | see [6-evaluation.md](6-evaluation.md) |
| Review | Find gaps | `Review against the PRD, models and plan: anything with no test, anything built but not drawn.` |
| Finish | Hand in | `Write the README (see 2-documents.md). Tick each Done when item with its real result.` |

## When to use which chat mode
| Mode | Use when |
|---|---|
| Ask | Questions, critique, choosing; nothing should change |
| Plan | Drafting a plan you will read before any file changes |
| Edit | Writing or changing files |

## Time (4-hour window, 2-3 hours of work expected)
0:00 read twice, rules, understand, questions · 0:25 data first, documents · 0:50 models ·
1:10 off the shelf, shape, plan · 1:30 build · 2:45 evaluate, review · 3:15 README · 3:40 submit.
