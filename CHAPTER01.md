# Chapter 1 release map

Chapter 1 establishes the vocabulary and interaction loop used by every later chapter. This map connects the introductory lesson to evidence that a learner can describe an RL problem without confusing it with a supervised-learning dataset.

## Learning contract

A learner who completes the chapter should be able to:

- identify the agent, environment, observation, state, action, and reward in a concrete task;
- distinguish a policy from a value function and an environment model;
- describe an interaction as an ordered sequence rather than a fixed input-output pair;
- explain why delayed consequences make an RL objective different from immediate reward;
- state which parts of a problem definition are modeling choices;
- identify when RL is not needed because labels or a known optimizer already solve the task.

Formal transition kernels and returns belong to Chapter 5. Chapter 1 introduces their purpose without requiring MDP notation.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| RL interaction loop | Introduction and trial-and-error sections | Not required |
| Agent-environment boundary | Elements of RL section | Not required |
| Policy, reward, value, and model | Elements of RL section | Not required |
| Paradigm comparison | RL versus supervised and unsupervised learning | Not required |
| Applied decomposition | Interaction audit | Not required |
| Independent practice | Chapter exercises | Not required |

The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/1-Introduction/intro.md). An executable companion is optional until the chapter introduces a numerical algorithm.

## Required invariant checks

| Area | Release check |
|---|---|
| Interaction order | Every example places action before its resulting reward and next observation |
| Boundary | Agent-controlled and environment-controlled quantities are named |
| Terminology | Policy, value, reward, and model are not used as synonyms |
| Objective | Long-term consequences are visible in at least one example |
| Paradigm comparison | Supervised labels are not claimed to be available during interaction |
| Scope | The lesson does not require MDP notation before it is introduced |
| Practice | Each exercise asks for a concrete decomposition or explanation |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Recall | Label the elements of a new interaction | Correct names and boundary |
| Explain | Contrast the task with supervised learning | Feedback and data differences are explicit |
| Apply | Audit a real system proposal | Agent, actions, reward, observations, and objective are defensible |

Passing requires a correct decomposition and a reasoned explanation of one modeling choice. Memorizing the vocabulary alone is not enough.

## Verification questions

1. Does each example identify one decision maker rather than shifting the agent boundary mid-example?
2. Are reward and value kept separate in every explanation?
3. Does the learner see feedback arriving after an action?
4. Is at least one delayed consequence explained without relying on formal MDP notation?
5. Do exercises include cases where RL is the wrong tool?

## Completion status

Status: **Complete**

Present evidence:

- published lesson and chapter navigation;
- explicit learning goals, scope, worked audit, mistakes, summary, exercises, and sources;
- release checks that do not require an artificial coding task.
