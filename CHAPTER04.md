# Chapter 4 release map

Chapter 4 supplies the probability language used by the later value-estimation chapters. This map connects each mathematical idea to an RL interpretation and a checkable calculation.

## Learning contract

A learner who completes the chapter should be able to:

- distinguish a random variable from one observed value;
- compute expectation, variance, and covariance for small distributions;
- apply conditional probability and Bayes' rule with a declared sample space;
- test independence and conditional independence from a joint distribution;
- select Bernoulli, binomial, normal, or categorical models for simple RL quantities;
- explain the roles of the law of large numbers and central limit theorem;
- identify the experimental unit before reporting an uncertainty estimate.

Measure-theoretic probability and formal asymptotic proofs are outside this chapter. The goal is correct use of finite and standard parametric examples.

## Artifact map

| Learning evidence | Website | Executable material |
|---|---|---|
| Distribution calculations | Random-variable section | `Probability.ipynb` |
| Moments and dependence | Expectation and covariance sections | Notebook calculations |
| Conditioning | Conditional-probability section | Notebook calculations |
| Common RL distributions | Distribution sections | `Probability.ipynb` |
| Sampling behavior | LLN and CLT section | Seeded simulation cells |
| Experimental-unit choice | RL experiment section | Worked uncertainty audit |

The executable path lives in [RLH-Material](https://github.com/The-RL-Hub/RLH-Material/tree/main/Chapter04). The published lesson lives in [The-RL-Hub.github.io](https://github.com/The-RL-Hub/The-RL-Hub.github.io/blob/main/content/tutorials/4-Probability/probability.md).

## Required invariant checks

| Area | Release check |
|---|---|
| Probability mass | Every finite distribution is nonnegative and sums to one |
| Expectation | Values and probabilities are paired over the same support |
| Variance | The calculation is nonnegative and uses the declared mean |
| Conditioning | Conditioning events have positive probability |
| Independence | Factorization claims are checked against a joint distribution |
| Sampling | Simulation cells expose seeds and sample sizes |
| CLT | Independence, identical distribution, and finite variance assumptions are named when used |
| Uncertainty | Training runs and evaluation episodes remain distinct units |
| Notebook | A clean-kernel run finishes without an exception |

## Assessment plan

| Stage | Learner task | Evidence |
|---|---|---|
| Calculate | Compute moments and one conditional probability | Arithmetic uses the declared support |
| Simulate | Compare empirical and analytical quantities | Seed, sample count, and deviation are reported |
| Diagnose | Review an invalid uncertainty claim | Experimental unit and missing assumptions are identified |

Passing requires exact finite calculations and a sampling interpretation. Plot shape alone is not evidence that an assumption holds.

## Verification questions

1. Does every probability expression identify its random variables and conditioning information?
2. Are population quantities kept separate from sample estimates?
3. Are covariance and independence not treated as equivalent in general?
4. Does each asymptotic statement name the assumptions used?
5. Do RL examples identify whether states, episodes, seeds, or runs form the sampling unit?

## Completion status

Status: **Complete**

Present evidence:

- published probability lesson connected to RL examples;
- clean-kernel probability notebook execution;
- explicit LLN, CLT, and experimental-unit cautions;
- tested moments, conditioning, and standard-error functions.
