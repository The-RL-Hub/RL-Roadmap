# Chapter completion registry

Each chapter is complete when its release map names the lesson, assessment, executable work when needed, and the automated checks that protect its central claims.

## Current status

| Chapter | Status | Completion evidence | Release map |
|---:|---|---|---|
| 1 | Complete | Lesson structure, navigation, and release checks | [Chapter 1](CHAPTER01.md) |
| 2 | Complete | Tested bandit rules, notebook execution, and seeded evaluation | [Chapter 2](CHAPTER02.md) |
| 3 | Complete | Tested contextual algorithms and logged-policy checks | [Chapter 3](CHAPTER03.md) |
| 4 | Complete | Probability notebook and tested uncertainty functions | [Chapter 4](CHAPTER04.md) |
| 5 | Complete | Six MDP labs, diagnostic modules, and invariant checks | [Chapter 5](CHAPTER05.md) |
| 6 | Complete | Planning notebook, tested solvers, and residual checks | [Chapter 6](CHAPTER06.md) |
| 7 | Complete | Prediction and control labs with end-signal tests | [Chapter 7](CHAPTER07.md) |
| 8 | Complete | TD(0) notebook, shared helpers, and target tests | [Chapter 8](CHAPTER08.md) |

All eight published chapters meet the repository definition of done. Chapter 1 does not need a numerical notebook because it teaches problem framing rather than an algorithm.

## Evidence rules

A status changes only when the linked artifact exists and its check passes.

- **Executable gap** closes when the named module or notebook runs in CI and deterministic tests cover its central invariants.
- **Test gap** closes when deterministic checks cover each named algorithm update and invalid-input path.
- **Assessment gap** closes when the learner task, expected evidence, and automated or rubric-based check are all present.
- **Scope gap** closes when the lesson claim and executable scope agree. Narrowing an unsupported claim is valid when a new lab is not yet planned.
- **End-semantics gap** closes when task termination and external truncation produce separately tested targets.
- **Complete** means the release map names its evidence and every repository check passes.

## Update procedure

When a contribution closes a gap:

1. update the relevant chapter release map;
2. update this table in the same contribution series;
3. link the website, material, and test evidence;
4. run the roadmap check;
5. reopen the matching gap if the evidence or its check is removed.

The registry records evidence, not a percentage. A chapter with more pages is not necessarily closer to release than a shorter chapter with verified outcomes.
