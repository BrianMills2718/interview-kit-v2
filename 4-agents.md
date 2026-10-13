# 4. LangChain and LangGraph

LangChain gives the parts (model, tools, an agent loop). LangGraph runs your program as steps and
arrows, and adds human pauses, memory between turns and step limits.

## Always
- Tools: `@tool` on a typed function. The docstring is what the model reads, so write it as an
  instruction. Return short structured data; raise a clear error on bad input.
- Typed answers: Pydantic model as the result, never regex on the model's text.
- Bound the loop: `config={"recursion_limit": 10}`.
- One function builds the model; tests use a fake model with scripted replies, so they run offline.
- Log each step: node, tool, arguments, result size.

## When to use what
| Situation | Use | Why |
|---|---|---|
| Steps are fixed and known | Plain Python functions (no LLM, or one LLM call) | Simplest; easiest to test and explain |
| Fixed steps with one LLM judgement | One structured LLM call: `llm.with_structured_output(Model)` | Typed answer, no loop to bound |
| The model should choose which tools to call | `from langchain.agents import create_agent` with `tools=[...]`, `system_prompt=` | Standard agent loop |
| Agent must return a typed result | `create_agent(..., response_format=ToolStrategy(Model))`, read `out["structured_response"]` | Validated output |
| Fixed order with branches, retries or a pause | LangGraph `StateGraph` with `TypedDict` state and conditional edges | You control every arrow; matches your state diagram |
| A human must approve before a write | `interrupt(...)` plus a checkpointer (`InMemorySaver()`), resume with `Command(resume=...)` on the same `thread_id` | Built-in pause and resume |
| Different request types need different handling | Router node (one LLM classification) then separate branches | Cheaper and more testable than one big agent |
| Several specialist agents | Supervisor graph over sub-agents | Only if the task names separate roles; otherwise one agent |
| Tools live in another service | MCP (Model Context Protocol) client tools | Standard tool interface across processes |
| Agents in different systems talk | A2A (Agent2Agent) | Mention as next step; rarely needed in a take-home |

## Traps (the AI gets these wrong)
- `create_react_agent` is old; use `create_agent` and `system_prompt=`.
- On resume after `interrupt()`, the tool or node runs again from its first line. Do the write
  (record the flag, issue the refund) only after `interrupt()` returns; on "no", write nothing.
- No checkpointer means no resume.
- Two pauses in one turn come back together; answer them by interrupt id.
- Mermaid breaks on `;` in sequence messages and on parentheses in labels; quote them.

## Type
`For each requirement, which LangChain/LangGraph piece does it? Exact import. Write a ten-line probe of the pause-and-resume behaviour and print which lines ran twice.`
