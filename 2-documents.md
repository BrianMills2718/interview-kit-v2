# 2. Documents

Normative documents say what must be true; the code is checked against them.

## Always
| Document | What it holds | Type |
|---|---|---|
| `docs/PRD.md` (product requirements) | Goal with one example; requirements R1.. quoting the task; assumptions A1..; risks ranked | `Write docs/PRD.md: Goal with one example "input -> result"; Requirements R1.. quoting the task; Assumptions A1..; Risks ranked, riskiest first.` |
| Use cases (in the PRD) | Who does what and what they get, including failures | `Add Use cases UC1..: actor, trigger, steps, expected result. Normal first, then every failure and alternative (bad input, a "no", a retry, a limit).` |
| `PLAN.md` | Done-when checklist and small steps | see [1-workflow.md](1-workflow.md) |
| `README.md` | How to run it and why it is built this way | `README with headings: Run it (command and real output), Approach (with the diagrams), Design decisions, Assumptions, How I used the AI, Limitations, Next steps.` |

## When to use what
| Situation | Write | Type |
|---|---|---|
| You chose between real options (library, shape, threshold) | ADR (architecture decision record) in `docs/DECISIONS.md` | `Add an ADR: context, decision, consequences, rejected alternative, what would show it wrong.` (the last two are this kit's additions to the standard ADR) |
| The task is vague or numbers are unstated | Assumptions table, each tied to a requirement | `List each assumption with the requirement it affects and how we'd notice it is wrong.` |
| Rules must always hold (no write before approval, thresholds) | Business rules / invariants list | `List the rules that must always be true, each as one testable sentence.` |
| The output format is fixed by the task | Output contract | `Quote the exact output format the task requires, field by field, with one example.` |
| Data comes in | Data dictionary | see [3-models.md](3-models.md) |
| Something is measured | Evaluation plan | see [6-evaluation.md](6-evaluation.md) |

## Skip
Long prose specs, project charters, Gantt charts, stakeholder lists: no question in a take-home needs them.
