# Chapter 3 release map

Chapter 3 adds observed context to the bandit problem. This map separates online learning claims from offline evaluation claims and records the evidence needed for both.

## Learning contract

A learner who completes the chapter should be able to:

- define a contextual bandit interaction and its partial-feedback constraint;
- distinguish context features from actions and rewards;
- derive the score used by LinUCB from its per-action state;
- describe linear Thompson sampling as posterior sampling under stated assumptions;
- compare epoch-greedy and explore-then-commit schedules;
- test an implementation with seeded synthetic contexts;
- explain why logged-policy support is required for offline evaluation.

The chapter assumes linear reward models for its main algorithms. General nonlinear function approximation belongs to a later chapter.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| Contextual interaction | Definition section | `Contextual_Bandits.ipynb` |
| LinUCB update | LinUCB section | `contextual_bandits.py` |
| Linear Thompson sampling | Thompson section | `contextual_bandits.py` |
| Seeded synthetic environment | Worked audit | `Contextual_Bandits.ipynb` |
| Regret calculation | Theory and experiment sections | `test_contextual_bandits.py` |
| Logged support reasoning | Offline-evaluation audit | Lesson exercise |

The executable paths live in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter02%20and%2003). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/3-cmab/cmab.md).

## Required invariant checks

| Area | Release check |
|---|---|
| Context shape | Feature dimension agrees across environment, policy, and update |
| Partial feedback | Only the selected action reward enters the online update |
| Model class | Shared and disjoint linear parameters remain separate |
| LinUCB | Each covariance matrix remains symmetric and positive definite |
| Thompson sampling | Posterior sampling uses the declared prior and noise scale |
| Regret | The benchmark sees the same context and available actions |
| Logged evaluation | Target actions have positive probability under the logging policy |
| Repetition | Synthetic experiments expose seeds and independent run counts |
| Notebook | A clean-kernel run finishes without an exception |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Calculate | Score two actions with a small LinUCB state | Matrix dimensions and selected action are correct |
| Implement | Learn in a seeded linear contextual environment | Regret and action outputs pass deterministic checks |
| Audit | Decide if a logged dataset can evaluate a target policy | Support failures and logging probabilities are identified |

Passing requires a correct online update and a separate offline-support argument. Success in a simulator does not validate a logged estimator.

## Verification questions

1. Does context arrive before the action in every interaction trace?
2. Are feature and parameter dimensions stated near each matrix equation?
3. Does the implementation update only the selected action model?
4. Are linear realizability and reward-noise assumptions named near regret claims?
5. Does any logged-data exercise check support before estimating performance?

## Completion status

Status: **Complete**

Present evidence:

- published contextual-bandit lesson;
- executable LinUCB and linear Thompson sampling module;
- seeded notebook and deterministic algorithm tests;
- logged-policy support and inverse-propensity tools with separate tests.
