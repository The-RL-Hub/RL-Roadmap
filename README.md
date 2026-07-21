# The RL Hub curriculum roadmap

This repository is the canonical map of what The RL Hub teaches, in what order, and which artifacts make a chapter complete. The Persian book lives in **The-RL-Hub.github.io**; executable companions live in **RLH-Material**.

## Current learning path

| Chapter | Topic | Main prerequisite | Website | Executable companion | Learner outcome |
|---:|---|---|---|---|---|
| 1 | Introduction to reinforcement learning | Basic ML vocabulary | Available | Not required | Identify agent, environment, action, reward, policy, value, and model |
| 2 | Stochastic multi-armed bandits | Expectation and sample means | Available | MAB notebook | Implement exploration strategies and measure expected regret |
| 3 | Contextual bandits | Chapter 2, vectors, linear regression | Available | LinUCB and Linear Thompson notebook | Select actions from context and evaluate contextual regret |
| 4 | Probability foundations | Basic algebra | Available | Probability notebook | Use distributions, conditioning, expectation, variance, LLN, and CLT |
| 5 | Markov decision processes | Chapters 1 and 4 | Available | Six tested MDP labs | Define and validate states, transition models, policies, returns, termination, values, and occupancy |
| 6 | Bellman equations and dynamic programming | Chapter 5, linear algebra | Available | DP notebook | Evaluate and improve policies when the full MDP model is known |
| 7 | Monte Carlo methods | Chapters 5 and 6 | Available | First/every-visit prediction lab | Estimate policy values from complete episodes |
| 8 | Temporal-difference learning | Chapters 5-7 | Available | TD(0) prediction lab | Learn policy values online with bootstrapping |

## Dependency logic

Probability supports the mathematical language used throughout the book. Chapter 5 is the formal bridge from one-step bandit decisions to sequential decisions. Chapter 6 assumes that bridge and introduces model-based planning. Chapters 7 and 8 remove the requirement that the transition model be known.

## Chapter release maps

Release maps connect each chapter outcome to its lesson, executable evidence, required checks, assessment plan, verification questions, and completion status.

| Chapter | Release map |
|---:|---|
| 1 | [Introduction to RL](CHAPTER01.md) |
| 2 | [Stochastic multi-armed bandits](CHAPTER02.md) |
| 3 | [Contextual bandits](CHAPTER03.md) |
| 4 | [Probability foundations](CHAPTER04.md) |
| 5 | [Markov decision processes](CHAPTER05.md) |
| 6 | [Dynamic programming](CHAPTER06.md) |
| 7 | [Monte Carlo methods](CHAPTER07.md) |
| 8 | [Temporal-difference learning](CHAPTER08.md) |

See [COMPLETION.md](COMPLETION.md) for the cross-chapter status table and the evidence required before any chapter is labeled complete.

## Definition of done for a chapter

A chapter is ready for release when:

- its learning objectives and prerequisites are explicit;
- terminology and notation agree with previous chapters;
- mathematical claims state their assumptions and cite primary sources;
- it contains a worked example, limitations, summary, and exercises;
- navigation and local links pass automated checks;
- a companion notebook exists when computation adds learning value;
- notebook algorithms have deterministic tests for key invariants;
- the notebook executes from a clean kernel;
- automated repository checks pass.

## Planned continuation

The next coherent sequence after Chapter 8 is:

9. SARSA and Q-learning
10. Eligibility traces and n-step methods
11. Function approximation
12. Policy-gradient methods
13. Actor-critic methods
14. Model-based reinforcement learning
15. Offline RL, evaluation, and safety

These are proposed curriculum slots, not promises of completion. Each should be scoped in an issue before implementation.

## External resources

See [RESOURCES.md](RESOURCES.md) for verified official courses, books, and implementation references and how they align with the curriculum.

## Contribution workflow

Curriculum changes should update this repository in the same contribution series as the website and material changes. Keep the roadmap, lesson, notebook, and tests aligned so the repository checks can verify the declared scope.
