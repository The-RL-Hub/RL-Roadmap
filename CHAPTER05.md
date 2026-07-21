# Chapter 5 release map

Chapter 5 is the point where the curriculum moves from one-step decisions to trajectories. This file records the contract shared by the lesson, labs, and tests.

## Learning contract

A learner who completes the chapter should be able to:

- choose an agent-environment boundary and defend it;
- test whether a state representation keeps enough predictive information;
- define a finite joint kernel $p(s',r\mid s,a)$ and an initial distribution $\mu_0$;
- distinguish episodic, continuing, and finite-horizon tasks;
- keep termination separate from external truncation;
- compute returns plus exact $V^\pi$ and $Q^\pi$ for a small model;
- check Bellman residuals and discounted occupancy;
- estimate a tabular model from transition samples;
- report uncertainty when values are estimated from rollouts.

Dynamic programming algorithms are Chapter 6 material. Chapter 5 may solve linear systems for policy analysis, but it does not introduce policy iteration or value iteration.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| Core MDP definitions | Chapter 5 lesson | `MDP_Foundations.ipynb` |
| State sufficiency | State and Markov sections | `State_Design_and_Aliasing.ipynb` |
| Time-dependent values | Finite-horizon section | `Finite_Horizon_Values.ipynb` |
| State visitation | Occupancy section | `Occupancy_Measures.ipynb` |
| Models from samples | Empirical-model section | `Empirical_Model_Estimation.ipynb` |
| End-of-run semantics | Termination section | `Termination_and_Truncation.ipynb` |
| Independent practice | Chapter exercises | `EXERCISES.md` and `SOLUTIONS.md` |

The executable paths above live in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter05). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/5-MDP/mdp.md).

## Required invariant checks

| Area | Release check |
|---|---|
| Transition kernel | Every required state-action row exists and sums to one |
| Policy | Every nonterminal state has a normalized distribution over valid actions |
| Initial state | $\mu_0$ is nonnegative and sums to one |
| Exact evaluation | Linear solve satisfies the Bellman equation within tolerance |
| Rollout | Recorded transitions preserve reward and end-of-run cause |
| Empirical model | Counts reproduce probabilities and expose unseen state-action pairs |
| Finite horizon | The terminal boundary is zero and the result contains $H+1$ value tables |
| Project rubric | Seven artifacts total 100 points and blocking errors are enforced |
| Notebook | A clean-kernel execution finishes without an exception |

## Diagnostic utility map

| Question | RLH-Material evidence |
|---|---|
| What is the value under the declared start distribution? | `initial_distribution_value` |
| How random are transition and reward outcomes? | `model_metrics.py` |
| Is a recorded path possible under the model and policy? | `trajectory_probability.py` |
| How much discounted weight lies in the first $H$ steps? | `discounting.py` |
| Where does a continuing policy spend time? | `steady_state.py` |
| Which communicating classes are closed? | `policy_classes.py` |
| How different are two candidate models? | `model_comparison.py` |
| Which valid state-action pairs lack data? | `coverage.py` |
| In which states do two policies disagree? | `policy_comparison.py` |

Each diagnostic has deterministic unit tests. A lesson claim that depends on one of these quantities should link to the matching implementation or reproduce its calculation.

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Model | Specify a finite MDP from a concrete task | Boundary, state, actions, kernel, rewards, and start distribution are valid |
| Calculate | Evaluate one fixed policy | Exact values and residual checks agree |
| Audit | Test state sufficiency and data coverage | Aliasing evidence and unseen valid actions are reported |

Passing requires a valid model plus an independent check of at least one analytical quantity. A normalized transition table alone is insufficient.

## Verification questions

Use these questions to verify the artifacts:

1. Does the state contain information that changes the next-step distribution?
2. Is a time limit part of the task or only part of the runner?
3. Can every stated terminal condition be reached under the policies being discussed?
4. Do analytical values match the executable result?
5. Are random seeds and sample counts visible where simulation is used?
6. Does each exercise test a stated learning outcome?

## Completion status

Status: **Complete**

Present evidence:

- published lesson with a declared scope and primary sources;
- six focused notebooks plus tested diagnostic modules;
- exercises, solutions, clean-kernel execution, and deterministic invariant checks;
- explicit handoff to dynamic programming.
