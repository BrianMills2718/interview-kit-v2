# 6. Evaluation

## Always
- Compare against a baseline (always predict the common class, or a simple rule). A score means
  nothing alone.
- Show per-case results and the confusion matrix, not only one number.
- Keep the cases you tuned on separate from the cases you report.
- Read the failures and say what kind each is (missing evidence, ignored evidence, or a wrong label).
- Write `evaluate.py` that prints everything, and paste its real output in the README.

## When to use what
| Situation | Measure | Why |
|---|---|---|
| Yes/no labels, classes balanced | Accuracy plus confusion matrix | Fine when classes are similar in size |
| One class is rare (fraud, bots, alerts) | Precision, recall, F1 | Accuracy hides the rare class |
| Missing a positive is costly | Favour recall | Catch them all, accept some false alarms |
| False alarms are costly | Favour precision | Flag only when sure |
| Several classes | Per-class precision/recall plus macro F1 | One weak class can't hide |
| Score or probability output | PR curve / average precision (rare class); ROC AUC (balanced) | Shows the trade-off across thresholds |
| Predicting a number | MAE (average error), RMSE (punishes big errors) | Same units as the target |
| Small labelled set | Cross-validation (`cross_val_score`), say the set is small | One split is noisy |
| Two systems compared | Same cases, paired; report the difference and its uncertainty | Fair comparison |
| An LLM labels data | Score it against hand labels like any classifier | The LLM is a model too |
| An agent does a task | Suite of cases with known answers; pass/fail per case plus the trace of each failure | Shows where it breaks |
| Agent's path matters (right tools, right order) | Check the tool-call sequence against the expected one | Right answer by wrong route still fails |
| No hand labels, open-ended output | LLM-as-judge with a written rubric, checked on a few hand-graded cases | Only after checking the judge |

## scikit-learn
`from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, classification_report`
`print(classification_report(y_true, y_pred))` prints per-class precision, recall and F1 at once.

## Type
`Write evaluate.py: precision, recall, F1 and a confusion matrix against the labels, beside a baseline. Print per-case results. One paragraph on what the errors show.`
