# Verified reinforcement-learning resources

This list favors author-hosted books, official university courses, and official project documentation. “Verified” means the link and description were checked against the official page; it does not mean The RL Hub endorses every implementation detail.

## Core foundations

### Reinforcement Learning: An Introduction

Richard Sutton and Andrew Barto’s second-edition textbook is the main reference for the tabular sequence covered by Chapters 1 and 5-8.

- [Author-hosted PDF](http://incompleteideas.net/book/RLbook2020.pdf)
- Best alignment: Chapters 1, 3-6 of the book

### Stanford CS234

Stanford’s official CS234 course covers RL foundations, tabular MDP planning, policy evaluation, Q-learning, function approximation, policy search, offline RL, and imitation learning. It assumes Python, calculus, linear algebra, probability, and basic machine learning.

- [Official course page](https://web.stanford.edu/class/cs234/index.html)
- [Official lecture materials](https://web.stanford.edu/class/cs234/modules.html)
- Best alignment: The RL Hub Chapters 1 and 5-8, followed by the proposed control/function-approximation chapters

## Deep reinforcement learning

### UC Berkeley CS 285

Berkeley’s official CS 285 is an advanced deep-RL course covering imitation learning, policy gradients, value-based methods, actor-critic, model-based RL, exploration, and research topics. It expects prior machine-learning, optimization, and deep-learning experience.

- [Official current course site](https://rail.eecs.berkeley.edu/deeprlcourse/)
- [Official catalog description](https://www2.eecs.berkeley.edu/Courses/CS285/)
- Best alignment: after the proposed function-approximation chapter

### OpenAI Spinning Up

Spinning Up provides a concise terminology/formalism introduction, an algorithm taxonomy, policy-gradient derivations, standalone implementations, and research-practice guidance. Some software dependencies are older, so use it primarily as an educational reference and check current environment APIs separately.

- [Official documentation](https://spinningup.openai.com/en/latest/)
- [Key concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
- Best alignment: Chapter 5 and later deep-RL chapters

## Environment API

### Gymnasium

Gymnasium is the maintained standard interface used by many RL environments and documents the current reset/step API and terminated-versus-truncated distinction.

- [Official documentation](https://gymnasium.farama.org/)
- Best alignment: executable material from Chapter 5 onward

## How to use external resources

External material should complement rather than determine The RL Hub’s structure. Before linking a theorem, copy the assumptions into the Persian explanation. Before adapting code, verify its environment API, random-seed behavior, termination convention, and license.
