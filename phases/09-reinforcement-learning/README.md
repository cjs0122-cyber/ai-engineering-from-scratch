# Phase 9: Reinforcement Learning

> Agents that learn by doing. The foundation of RLHF.

## Why this phase exists

Every other kind of learning in this curriculum needs an answer key. Supervised
learning hands you `(input, correct output)` pairs. Reinforcement learning throws
that away. Instead you get an agent dropped into a world, allowed to act, and given
nothing but a reward — a single number that says "that was good" or "that was bad,"
often long after the action that caused it.

Learning from that thin signal is a genuinely different problem, and it's the one
behind chess bots, robots, trading agents, and — the reason it's on every AI
engineer's radar in 2026 — RLHF. When ChatGPT learned to be a helpful assistant, it
learned by reinforcement: humans compared answers, a reward model scored them, and
the language model was optimized to earn more reward. Every technique that turned a
raw text predictor into something you'd actually talk to lives in this phase.

This phase builds the whole ladder, from the five-part math object underneath all of
RL up to the exact loops (PPO, RLHF, GRPO) that train modern models.

## What you need first

Two earlier phases carry most of the weight:

- **Phase 1 (Math Foundations)** — especially probability and distributions. RL is
  built on expectations over random outcomes, so you'll want to be comfortable with
  "the average result if I did this many times."
- **Phase 3 (Deep Learning)** — backpropagation in particular. The first four
  lessons here are pure tables and need no neural networks. From lesson 05 onward,
  the value functions and policies become networks you train by gradient descent.

If those feel shaky, that's fine — the early lessons re-derive what they need from
scratch, and each lesson names its exact prerequisites so you can patch a gap
before you hit it rather than getting stuck mid-lesson.

## What you'll be able to do after this phase

- Model any decision problem as a Markov Decision Process — the shape every RL
  algorithm optimizes over
- Solve small environments exactly with dynamic programming, and use those answers
  to debug everything else
- Implement the classic model-free family from scratch: Monte Carlo, Q-learning,
  SARSA, and policy gradients
- Train deep-RL agents — DQN on pixels, actor-critic, and PPO — and know why each
  trick is there
- Build the RLHF pipeline: fit a reward model to human comparisons and optimize a
  language model against it
- Understand the frontier — multi-agent RL, sim-to-real transfer, and the
  AlphaZero-to-reasoning-model lineage

## The lessons

Do these in order — this phase is a ladder, and most lessons depend directly on the
ones before them.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **MDPs, States, Actions & Rewards** | The five-part object — states, actions, transitions, rewards, discount — that every RL algorithm optimizes over. Learn it once, read the rest for free. | ~45 min |
| 02 | **Dynamic Programming — Policy Iteration & Value Iteration** | When you know the environment's model, iterating the Bellman equation solves it exactly. The gold standard every sampling method is measured against. | ~75 min |
| 03 | **Monte Carlo Methods — Learning from Complete Episodes** | Drop the model entirely: run the policy, watch the returns, average them. The simplest way to learn from experience alone. | ~75 min |
| 04 | **Temporal Difference — Q-Learning & SARSA** | Update after every step instead of waiting for the episode to end. Q-learning and SARSA are one line each and underpin every deep-RL method here. | ~75 min |
| 05 | **Deep Q-Networks (DQN)** | Q-learning with a neural network reading raw pixels — the 2013/2015 Atari results that launched the deep-RL era, plus the three tricks that make it stable. | ~75 min |
| 06 | **Policy Gradient — REINFORCE from Scratch** | Skip value estimation and optimize the policy directly by stepping uphill on expected return. The theorem behind PPO, GRPO, and every LLM RL loop. | ~75 min |
| 07 | **Actor-Critic — A2C and A3C** | Add a critic that learns a value baseline to cut the variance of policy gradients. The mental model behind every modern deep-RL algorithm. | ~75 min |
| 08 | **Proximal Policy Optimization (PPO)** | A clipped importance ratio lets you reuse each rollout for many updates without the policy exploding. Still the default policy-gradient algorithm in 2026. | ~75 min |
| 09 | **Reward Modeling & RLHF** | Humans can't write a reward for "good answer," but they can pick the better of two. Fit a reward model to those choices and RL against it — the recipe that made ChatGPT. | ~45 min |
| 10 | **Multi-Agent RL** | Put two learning agents in one world and the environment stops being stationary. The tricks for making learning converge when the Markov assumption breaks. | ~45 min |
| 11 | **Sim-to-Real Transfer** | A policy that only works in the simulator memorized the simulator. Domain randomization, domain adaptation, and system identification close the reality gap. | ~45 min |
| 12 | **RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era** | From TD-Gammon to AlphaGo to AlphaZero to DeepSeek-R1: games are the benchmark that drove every breakthrough in this phase, up to RL for reasoning. | ~120 min |

## How each lesson is built

Every lesson in this curriculum follows the same rhythm, so once you learn the shape
you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

Go straight down 01 → 12. This phase is a genuine dependency chain: the tabular core
(01–04) has to be solid before the deep-RL methods (05–08) make sense, and those in
turn are what RLHF (09) and everything after are built on.

**If you're here mainly for LLMs and RLHF:** you still can't skip the ladder — but
know that 01–08 are the "why" and 09 is the payoff. Don't jump straight to 09; PPO
(08) is exactly the loop RLHF runs.

**Lessons 10–12** (multi-agent, sim-to-real, games) are the frontier and the
applications. They build on the core but stand somewhat on their own, so pull them in
based on what you're building.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
