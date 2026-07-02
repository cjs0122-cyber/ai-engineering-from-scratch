# Phase 3: Deep Learning Core

> Neural networks from first principles. No frameworks until you build one yourself.

## Why this phase exists

Most people learn deep learning backwards: they `import torch`, call
`model.fit()`, and trust that the magic inside works. When it breaks — and it
will — they have no idea why, because they never saw what's under the hood.

This phase does the opposite. You build a neural network from the ground up,
starting with a single neuron and ending with your own miniature training
framework — using nothing but plain math and NumPy. Weights, forward passes,
backpropagation, activations, losses, optimizers: you write every piece
yourself, so you understand exactly what each one does and why. Only *after*
you've built one from scratch do you pick up PyTorch and JAX — and by then
they're not magic anymore, they're just the fast version of things you already
understand.

## What you need first

- **Phase 1 (Math Foundations)** — especially calculus. Backpropagation *is*
  the chain rule applied systematically, so you'll want to be comfortable with
  derivatives and the chain rule. Linear algebra (vectors, dot products, matrix
  multiplication) shows up from the very first lesson.
- **Phase 2 (Classical Machine Learning)** — the ideas of training data,
  predictions, loss, and overfitting carry straight over into neural networks.

If your calculus feels rusty, that's normal — you don't need to be able to
derive everything from memory. The lessons re-explain the math you need at the
moment you need it, and you learn it best by watching it turn into working code.

## What you'll be able to do after this phase

- Explain how a neural network turns inputs into predictions, layer by layer
- Implement backpropagation by hand and know exactly where every gradient comes from
- Choose the right activation, loss function, and optimizer for a given problem
- Diagnose why a network won't train — dead neurons, exploding gradients, bad initialization, wrong learning rate
- Wire all the pieces into your own working deep learning framework
- Read and write real PyTorch and JAX code, knowing what each line actually does

## The lessons

Do these in order — each one builds directly on the last, and by lesson 10 you
assemble everything into a single framework.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **The Perceptron** | The single neuron — weights, bias, and a decision — is the atom every neural network is built from. | ~60 min |
| 02 | **Multi-Layer Networks and Forward Pass** | One neuron draws a line; stacking them into layers is how you get the curves real problems need. | ~90 min |
| 03 | **Backpropagation from Scratch** | The algorithm that makes learning possible — computing millions of gradients in a single backward pass. | ~120 min |
| 04 | **Activation Functions** | Nonlinearity is what lets a deep network do more than a fancy matrix multiply. | ~75 min |
| 05 | **Loss Functions** | The number that measures how wrong a prediction is — pick the wrong one and the model optimizes for the wrong thing. | ~75 min |
| 06 | **Optimizers** | Gradient descent says which way to move; the optimizer decides how far and how fast. | ~75 min |
| 07 | **Regularization** | The tax on complexity that forces a model to generalize instead of memorizing the training data. | ~75 min |
| 08 | **Weight Initialization and Training Stability** | Start the weights wrong and training never begins; start them right and deep networks train smoothly. | ~90 min |
| 09 | **Learning Rate Schedules and Warmup** | The single most important hyperparameter — if you tune nothing else, tune this. | ~90 min |
| 10 | **Build Your Own Mini Framework** | Wire every piece you've built — layers, backprop, optimizers, and the rest — into one working framework of your own. | ~120 min |
| 11 | **Introduction to PyTorch** | The framework everyone actually uses, now that you understand the engine underneath it. | ~75 min |
| 12 | **Introduction to JAX** | Compiling pure functions instead of mutating tensors — a different way of thinking about deep learning. | ~90 min |
| 13 | **Debugging Neural Networks** | The hardest debugging there is: the code runs, produces a number, and the number is silently wrong. | ~90 min |

## How each lesson is built

Every lesson in this whole curriculum follows the same rhythm, so once you learn
the shape you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

Go straight down the list, 01 → 13. This phase is deliberately sequential: the
perceptron feeds the multi-layer network, which feeds backpropagation, and so on
up to lesson 10, where it all comes together into your own framework.

Don't rush lessons 01–03 — the perceptron, the forward pass, and
backpropagation are the conceptual core of everything after them. If any of it
feels shaky, it's worth staying until it clicks. Lessons 11–13 (PyTorch, JAX,
and debugging) are where the framework fluency you'll rely on for the rest of the
curriculum starts.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
