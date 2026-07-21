# Chapter 2 release map

Chapter 2 introduces repeated decisions under partial feedback through stochastic multi-armed bandits. This map keeps algorithm descriptions, regret claims, and experiments tied to the same assumptions.

## Learning contract

A learner who completes the chapter should be able to:

- define actions, rewards, action values, and an optimal arm in a stochastic bandit;
- update a sample-average estimate incrementally;
- explain exploration and exploitation in terms of missing reward information;
- compute cumulative regret from a declared benchmark;
- implement epsilon-greedy, optimistic initialization, UCB, and Thompson sampling;
- compare strategies with repeated seeded runs and uncertainty summaries;
- recognize when nonstationarity invalidates a sample-average interpretation.

Context-dependent actions and rewards belong to Chapter 3. Sequential state transitions belong to Chapter 5.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| Stochastic bandit definition | Problem-definition section | `MAB.ipynb` |
| Incremental estimates | Action-value section | `MAB.ipynb` |
| Exploration strategies | Strategy sections | `MAB.ipynb` |
| Tested action selection | Strategy sections | `standard_bandits.py` |
| Regret measurement | Regret and evaluation sections | Notebook experiment outputs |
| Seeded comparison | Evaluation audit | Notebook simulation |
| Regression safety | Algorithm examples | `test_standard_bandits.py` and `test_mab_notebook.py` |

The executable paths live in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter02%20and%2003). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/2-smab/smab.md).

## Required invariant checks

| Area | Release check |
|---|---|
| Reward model | Stationarity and reward support are declared for each claim |
| Timing | Every $R_{t+1}$ is the outcome of $A_t$ |
| Action values | Counts and sample means agree after every update |
| Exploration | Every compared strategy can sample each intended arm |
| Regret | The oracle benchmark and expected versus realized form are named |
| Repetition | Seeds, horizon, number of runs, and aggregation method are visible |
| Thompson sampling | Prior and observation-noise assumptions are stated |
| Nonstationarity | Constant-step-size results are not described as sample averages |
| Notebook | A clean-kernel run finishes without an exception |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Calculate | Apply incremental value updates to a short reward trace | Counts and estimates match hand calculation |
| Implement | Run two exploration strategies under one seeded environment | Code and experiment settings are visible |
| Evaluate | Compare regret across independent runs | Benchmark, uncertainty, and interpretation are correct |

Passing requires both algorithm behavior and an experiment report. A single favorable reward trace does not establish a comparison.

## Verification questions

1. Are stochastic and adversarial regret claims kept separate?
2. Does each algorithm state what information it stores after a pull?
3. Are ties and unpulled actions handled explicitly?
4. Does the experiment compare strategies on shared environment instances or explain another design?
5. Are uncertainty and practical effect size shown beside average regret?

## Completion status

Status: **Complete**

Present evidence:

- published lesson with several exploration strategies;
- MAB notebook with clean-kernel CI execution and regression checks;
- tested sample-average, epsilon-greedy, optimistic, UCB, KL-UCB, and Thompson rules;
- evaluation protocol with seeded repetitions.
