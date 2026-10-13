# 3. Models and diagrams

A model answers one question about the system. Pick by question, not by habit. Draw in Mermaid
inside `docs/MODEL.md`, each with one bold **Answer:** line saying what it shows.
Six questions (the Zachman grid): what, how, where, who, when, why.

## Always (every agentic or data task)
| Question | Model | Type |
|---|---|---|
| What are the things? | Domain model (`classDiagram`) plus a Rules list | `classDiagram of the things in the use cases and their fields, plus a Rules list of what must always be true.` |
| When can things happen? | State machine (`stateDiagram-v2`) plus a Forbidden list | `stateDiagram-v2 of one run, with the human pause and resume, plus a Forbidden list written "A --> B".` |
| How does the riskiest case run? | Sequence diagram (`sequenceDiagram`) | `sequenceDiagram of UC___ between user, agent, each tool, the LLM and the human, using the real library calls.` |
| Which test proves each claim? | Tests-from-the-model table | `Table Claim / From / Test: one test per state arrow, forbidden move, rule and exact quoted output.` |

## When to use what
| Situation | Model | Answers | Type |
|---|---|---|---|
| Input is a dataset | Data dictionary (table) | What is in each column, and what is allowed? | `Table of every input column: type, unit, allowed values, nulls, and the rule we enforce. Same for the outputs.` |
| Work is a chain of transforms | Pipeline / activity diagram (`flowchart`) | How does data flow, and where do bad rows go? | `flowchart: load, validate, clean, features, detect, human review, report. Mark where bad rows go.` |
| Several actors or outside systems | Context diagram (`flowchart`) | Who uses it, and what is outside it? | `flowchart with the system as one box and the people, files, LLM and other systems around it, labelled with what flows.` |
| Tools change or return things | Operation contracts (table) | What does each tool promise? | `For each tool: inputs, preconditions, what it changes, what it returns, the error it raises.` |
| More than three files or modules | Component diagram (`flowchart`) | Where does code live, and who calls whom? | `flowchart of the files and functions we will write and what each calls.` |
| Records link to each other (tables, joins) | ER diagram (`erDiagram`) | How are records keyed and related? | `erDiagram of the tables with keys and cardinality.` |
| Several agents or a router | Agent graph (`flowchart`) | Which node runs next, and when does it stop? | `flowchart of the graph nodes and conditional edges, with the stop condition and step limit.` |
| Something runs on a schedule or deadline | Timeline / state with timers | What happens when time passes? | `Add timeout transitions to the state machine and say what each does.` |
| Classifier or detector output | Evaluation design | How do we know it is right? | see [6-evaluation.md](6-evaluation.md) |

## Skip unless asked
Deployment diagrams (hosts, networks), object diagrams, full UML class design, use-case
stick-figure diagrams (the use-case table says the same thing).

## Then
`Walk UC___ through the state machine and the pipeline. Which arrow fires, and what stops a forbidden one?`
Never change a diagram just to make the code pass: if the model is wrong, change the diagram and its test together.
