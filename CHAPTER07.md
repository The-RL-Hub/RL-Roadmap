# Chapter 7 release map

Chapter 7 estimates policy values from complete sampled episodes without a transition model. This map ties each Monte Carlo estimate to its visit convention, data source, and uncertainty report.

## Learning contract

A learner who completes the chapter should be able to:

- compute discounted returns from a completed episode;
- distinguish first-visit and every-visit Monte Carlo prediction;
- update sample means incrementally without retaining every return;
- explain why basic Monte Carlo prediction waits for episode completion;
- compare estimates across independent runs with uncertainty summaries;
- handle externally truncated data without treating it as a true terminal return;
- state the coverage condition needed for Monte Carlo control.

Bootstrapped one-step targets belong to Chapter 8. On-policy control has a separate epsilon-soft lab; off-policy correction remains outside this chapter.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| Episode return | Prediction section | `Monte_Carlo_Prediction.ipynb` |
| Visit convention | First versus every-visit section | `monte_carlo.py` |
| Incremental mean | Update section | `monte_carlo.py` |
| Prediction experiment | Worked random-walk audit | Notebook outputs |
| Convergence behavior | Prediction discussion | `test_monte_carlo.py` |
| On-policy control | Control section | `Monte_Carlo_Control.ipynb` |
| Incomplete episodes | Dedicated lesson section | `monte_carlo_control.py` |
| Control regression safety | Control lab checks | `test_monte_carlo_control.py` |
| Uncertainty | Dedicated lesson sections | Chapter exercises |

The executable paths live in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter07). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/7-MC/mc.md).

## Required invariant checks

| Area | Release check |
|---|---|
| Return | Rewards, discount powers, and episode boundary use one indexing convention |
| First visit | A state contributes only its earliest return in each episode |
| Every visit | Every occurrence contributes its own suffix return |
| Mean update | Count increments before the reciprocal step size is applied |
| Episode end | External truncation is not silently treated as a terminal return |
| Uncertainty | Independent episodes or runs define the reported sampling unit |
| Coverage | Control claims state how every relevant action remains selectable |
| Notebook | A clean-kernel run finishes without an exception |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Calculate | Compute suffix returns for one episode | Discounting and visit positions are correct |
| Implement | Compare first-visit and every-visit prediction | Counts and estimates follow each convention |
| Evaluate | Report error and uncertainty over independent episodes | Sampling unit and episode handling are explicit |

Passing requires correct return bookkeeping and a data interpretation. Reusing correlated visits as independent runs is not accepted.

## Verification questions

1. Does the return start with the reward following the state-action pair?
2. Are first-visit and every-visit counts inspectable in the implementation?
3. Does the lesson state why a complete episode is required for its basic estimator?
4. Are truncated episodes excluded or handled with a declared estimator?
5. Are prediction and control coverage requirements kept separate?

## Completion status

Status: **Complete**

Present evidence:

- published Monte Carlo prediction and control explanations;
- tested first-visit and every-visit prediction module;
- clean-kernel prediction notebook and uncertainty guidance.
- clean-kernel on-policy control notebook with epsilon-soft action coverage;
- tested discard and strict-error decisions for externally truncated episodes.
