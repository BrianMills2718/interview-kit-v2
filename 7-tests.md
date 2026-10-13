# 7. Tests and code quality

## Always
- One test per model claim: each state arrow, each forbidden move, each rule, each exact output
  the task quotes (see [3-models.md](3-models.md)).
- Each test must fail on a wrong version (check it once by breaking the code).
- Test the boundary itself: the exact threshold, a tie, a time one second outside the window.
- Fake LLM with scripted replies so tests run offline and repeat.
- Fail loudly: no bare `except`, no silent fallbacks; bad input raises a clear error.
- One-line docstring on every function; a short comment naming any rejected alternative.

## When to use what
| Situation | Use |
|---|---|
| Same check over many inputs | `@pytest.mark.parametrize` |
| Shared sample data | A `pytest` fixture building a small DataFrame |
| Code calls an LLM | Fake model with fixed replies; assert on the tool calls and the result |
| Code pauses for a human | Test "yes" resumes and writes once; test "no" writes nothing |
| Floating-point results | `pytest.approx` |
| Error paths | `with pytest.raises(ValueError, match="..."):` |
| Run outputs must match a format | Assert the exact string or schema the task quotes |
| Random methods | Fixed `random_state`, then assert exact values |

## Type
`Write the tests the model names for step N, each one a wrong version would fail. Use a fake model. Run them and show the output.`
`Break the code on purpose for one test and show it fails, then restore it.`
