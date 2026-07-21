# Chapter 6 release map

Chapter 6 turns the Bellman relationships from Chapter 5 into planning algorithms for a known finite MDP. This map separates policy evaluation, policy improvement, and optimality claims.

## Learning contract

A learner who completes the chapter should be able to:

- write Bellman expectation equations for a declared policy;
- compute one synchronous policy-evaluation sweep;
- improve a policy greedily with respect to an action-value calculation;
- implement policy iteration and value iteration on a finite model;
- explain the contraction-based stopping rule when the discount is below one;
- recover a deterministic greedy policy with explicit tie handling;
- verify a solution with Bellman residuals rather than iteration count alone.

All algorithms in this chapter assume access to the transition and reward model. Sample-based prediction begins in Chapter 7.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| Bellman expectation equations | Bellman section | `VB_methods_DP.ipynb` |
| Iterative policy evaluation | Dynamic-programming section | Notebook implementation |
| Policy improvement | Policy-improvement section | Notebook implementation |
| Policy iteration | Policy-iteration section | `VB_methods_DP.ipynb` |
| Value iteration | Value-iteration section | `VB_methods_DP.ipynb` |
| Residual and policy audit | Worked planning audit | Notebook outputs |
| Notebook reference link | Worked planning audit | `notebook_adapter.py` |

The executable path lives in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter06). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/6-value-based/value-based.md).

## Required invariant checks

| Area | Release check |
|---|---|
| Model input | Transition and reward rows cover every valid state-action pair |
| Policy evaluation | Synchronous backups use one unchanged previous value table |
| Policy improvement | Greedy actions are computed from the evaluated value function |
| Tie handling | The chosen deterministic or stochastic tie rule is explicit |
| Stopping | Tolerance, discount, and maximum iteration count are recorded |
| Residual | The returned value function satisfies the relevant Bellman equation |
| Terminal state | Continuation value follows the Chapter 5 convention |
| Notebook | A clean-kernel run finishes without an exception |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Calculate | Perform one policy-evaluation and improvement sweep | Backups use the correct source values |
| Implement | Run policy iteration and value iteration | Both return valid policies on the test MDP |
| Verify | Measure Bellman residual and compare solutions | Tolerance and tie handling are reported |

Passing requires algorithm output and residual evidence. Stopping because a loop reached its iteration limit is not a convergence check.

## Verification questions

1. Do all backups use the Chapter 5 reward and transition convention?
2. Is policy evaluation clearly separated from policy improvement?
3. Are synchronous and in-place update orders identified?
4. Is the stopping claim justified for the declared discount and task type?
5. Can the returned policy be checked independently from the final value table?

## Completion status

Status: **Complete**

Present evidence:

- published Bellman and dynamic-programming lesson;
- clean-kernel planning notebook;
- tested policy evaluation and value iteration module;
- notebook audit through the tested adapter and reference solver;
- residual, tie, invalid-input, and terminal-value checks.
