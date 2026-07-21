# Chapter 8 release map

Chapter 8 introduces one-step temporal-difference prediction. This map keeps the TD target, end-of-run semantics, and convergence evidence aligned across prose and code.

## Learning contract

A learner who completes the chapter should be able to:

- derive the TD(0) target and TD error from the recursive return;
- perform a tabular TD(0) update for a fixed policy;
- explain bootstrapping and contrast it with a complete Monte Carlo return;
- keep terminal-state values fixed at zero under the declared convention;
- bootstrap after external truncation but not after task termination;
- study the effect of step size and discount with repeated seeded runs;
- identify that TD prediction does not yet solve the control problem.

SARSA, Q-learning, eligibility traces, and function approximation are later curriculum topics. This chapter is limited to tabular policy prediction.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| TD target and error | TD error sections | `TD0_Prediction.ipynb` |
| Tabular update | TD(0) algorithm section | `temporal_difference.py` |
| Random-walk prediction | Worked example | `TD0_Prediction.ipynb` |
| Terminal handling | End-semantics section | `test_temporal_difference.py` |
| End-signal notebook audit | End-semantics section | `TD0_Prediction.ipynb` helper calls |
| Seeded convergence | Experiment section | `test_temporal_difference.py` |
| Method comparison | TD versus Monte Carlo section | Chapter exercises |

The executable paths live in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter08). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/8-TDL/tdl.md).

## Required invariant checks

| Area | Release check |
|---|---|
| TD target | The next-state value is multiplied by the declared discount |
| Termination | A task terminal transition contributes no bootstrap value |
| Truncation | An external cutoff preserves the next-state bootstrap term |
| Policy | Samples and target values refer to the same fixed policy |
| Step size | The update uses a declared schedule or constant value |
| Terminal value | Terminal-state entries remain fixed at zero under the lesson convention |
| Experiment | Seeds, episode counts, and evaluation error are reported |
| Notebook | A clean-kernel run finishes without an exception |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Calculate | Perform TD(0) updates on a short transition trace | Targets, errors, and updated values are correct |
| Implement | Learn values in the random walk | Seeded error decreases under the declared settings |
| Diagnose | Compare terminal and truncated final steps | Bootstrap masking follows the end cause |

Passing requires correct updates and correct end semantics. A falling training error cannot compensate for an invalid target.

## Verification questions

1. Is every TD target indexed with the reward and state that follow the current action?
2. Does the code reset only after recording the final transition?
3. Are termination and truncation passed separately to the update?
4. Does the evaluation compare learned values with known or independently estimated values?
5. Is the chapter explicit that TD(0) prediction does not choose an improved policy?

## Completion status

Status: **Complete**

Present evidence:

- published TD(0) lesson and random-walk example;
- tested TD prediction module;
- clean-kernel notebook with terminal values fixed at zero;
- notebook audit calling the shared target and update helpers directly;
- separately tested continuing, termination, and truncation targets.
