# 5. Data science techniques

## Always
- Look before analysing: shape, types, nulls, duplicates, ranges, date span, value counts.
- State the exact threshold and the tie rule the task gives, and test the boundary value itself.
- Write each method's assumption next to it, and one sentence on why it fits this data.
- Use pandas, numpy, scipy, scikit-learn, networkx; build nothing these already do.
- Fix randomness (`random_state=0`) so results repeat.

## Describe and clean
| Situation | Use | How |
|---|---|---|
| Counts or averages per group | `groupby` | `df.groupby("lang")["shares"].mean()` |
| Events over time | Resample by day/hour | `df.resample("D", on="ts").size()` |
| Smooth a noisy series | Rolling mean | `s.rolling(7).mean()` |
| Messy text or dates | Normalise first | `pd.to_datetime(...)`, `.str.strip().str.lower()` |
| Missing values | Drop if few and random; else fill and say so | `df.isna().mean()` to decide |

## Anomalies
| Situation | Use | Note |
|---|---|---|
| One numeric series, roughly normal | z-score, flag \|z\| > 3 (or the task's cutoff) | `(x - x.mean()) / x.std()` |
| Outliers would distort the mean | Robust z: median and MAD (median absolute deviation) | Spikes don't hide themselves |
| Skewed counts, simple rule wanted | IQR (interquartile range) fence: below Q1 - 1.5 IQR or above Q3 + 1.5 IQR | Easy to explain |
| Many columns together, no labels | Isolation Forest (`sklearn.ensemble.IsolationForest`) | Set `contamination`; say why |
| Same text posted by many accounts within minutes | Group by normalised text, then time gap within window | Coordinated behaviour |

## Compare groups (statistical tests)
| Question | Test | scipy |
|---|---|---|
| Two group means differ? | Welch t-test (doesn't assume equal spread) | `ttest_ind(a, b, equal_var=False)` |
| Two groups, skewed or small | Mann-Whitney U | `mannwhitneyu(a, b)` |
| Counts across categories related? | Chi-square | `chi2_contingency(table)` |
| Two numbers move together? | Pearson (linear) / Spearman (ranked) | `pearsonr`, `spearmanr` |
| Many tests at once | Correct for multiple comparisons (Bonferroni: divide 0.05 by the number of tests) | Say it in the README |
Report the effect size (the actual difference) with the p-value, not the p-value alone.

## Estimate and predict
| Situation | Use |
|---|---|
| Best parameter for observed data | MLE (maximum likelihood): e.g. 30 replies of 100 posts gives rate 0.3 |
| Predict a number | Linear regression (`sklearn.linear_model.LinearRegression`) |
| Predict a label, explainable | Logistic regression |
| Predict a label, stronger | Random forest / gradient boosting |
| Group similar items, no labels | k-means (numbers), DBSCAN (dense groups plus noise) |
| Engineer features | Counts per account, rates, time of day, text length; avoid features computed from the label |

## Text, any language
| Situation | Use |
|---|---|
| Which language? | `langdetect`, or the language column if given |
| Keywords or similarity in one language | TF-IDF (`sklearn TfidfVectorizer`) |
| Meaning across languages | Multilingual embeddings, then cosine similarity |
| Topic or stance labels | An LLM with a structured output, then evaluate it (see [6-evaluation.md](6-evaluation.md)) |

## Networks
| Question | Use (networkx) |
|---|---|
| Who has the most connections? | Degree: `G.degree()` |
| Who bridges groups? | Betweenness: `nx.betweenness_centrality(G)` |
| Which groups exist? | Communities: `nx.community.louvain_communities(G, seed=0)` |
| Who influences whom (direction matters)? | Directed graph, in-degree, PageRank |
