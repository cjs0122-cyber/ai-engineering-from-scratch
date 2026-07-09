# Phase 2: ML Fundamentals

> Classical machine learning — still the backbone of most production AI.

## Why this phase exists

"Machine learning" sounds like it should mean giant neural networks and chatbots.
It doesn't — not at first. The core idea is simpler and older: instead of writing
rules by hand ("if the email says FREE MONEY, mark it spam"), you show a computer
lots of examples and let it *find the rules itself*. That shift — from programming
rules to learning from data — is what this whole phase is about.

The algorithms here are the "classical" ones: straight lines, flowcharts, nearest
neighbors, forests of decision trees. They came before deep learning, and they never
went away. A huge share of real production AI — fraud detection, demand forecasting,
credit scoring, recommendation ranking — still runs on exactly these methods, because
they are fast, cheap, easy to explain, and often just as accurate as anything fancier.

Just as importantly, every idea you learn here — training, cost functions, overfitting,
evaluation — reappears later when you get to neural networks and large language models.
Learn the pattern once, in its simplest form, and you will recognize it everywhere.

## What you need first

You need **Phase 0 (Setup & Tooling)** finished, so Python, your notebook, and your
libraries all run. You also want **Phase 1 (Math Foundations)** — the linear algebra,
calculus, probability, and statistics these algorithms are built on.

Don't panic if the math still feels shaky. Each lesson reintroduces what it needs and
shows you the idea in code before the equations. You are here to build working models,
not to pass a math exam.

## What you'll be able to do after this phase

- Take a raw dataset and train a model that makes real predictions from it
- Pick the right algorithm for a problem — regression vs. classification, and which
  one fits your data
- Turn messy real-world data into useful inputs through feature engineering and selection
- Measure a model honestly, and know when good accuracy is actually a lie
- Diagnose and fix overfitting, underfitting, and imbalanced data
- Package the whole flow — data in, prediction out — into a reproducible pipeline

## The lessons

Do them roughly in order — this phase builds on itself more than Phase 0 did. The early
lessons establish the training loop that every later lesson reuses.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **What Is Machine Learning** | The core shift from writing rules to learning patterns from data — the foundation everything else stands on. | ~45 min |
| 02 | **Linear Regression** | The "hello world" of ML: fit the best line through data, and learn the training loop every algorithm reuses. | ~90 min |
| 03 | **Logistic Regression** | Bend that line into an S-curve to answer yes-or-no questions with real probabilities. | ~90 min |
| 04 | **Decision Trees and Random Forests** | A decision tree is just a flowchart; a forest of them is one of the most powerful tools in ML. | ~90 min |
| 05 | **Support Vector Machines** | Separate two classes by finding the widest possible street between them. | ~90 min |
| 06 | **K-Nearest Neighbors and Distances** | Predict by looking at your closest neighbors — the simplest algorithm that actually works. | ~90 min |
| 07 | **Unsupervised Learning** | Find structure in data that has no labels and no teacher. | ~90 min |
| 08 | **Feature Engineering & Selection** | Shape raw data into good inputs — a good feature is worth a thousand data points. | ~90 min |
| 09 | **Model Evaluation** | A model is only as good as the way you measure it; learn to measure it right. | ~90 min |
| 10 | **Bias-Variance Tradeoff** | Understand where model error comes from, and which parts you can actually control. | ~75 min |
| 11 | **Ensemble Methods** | Combine many weak models into one strong one — not a metaphor, a theorem. | ~120 min |
| 12 | **Hyperparameter Tuning** | Turn the knobs set before training well — the gap between a mediocre model and a great one. | ~90 min |
| 13 | **ML Pipelines** | Wire raw data to deployed prediction as one reproducible flow — a model is not a product, a pipeline is. | ~120 min |
| 14 | **Naive Bayes** | A "wrong" assumption that works anyway, and stays fast and simple doing it. | ~75 min |
| 15 | **Time Series Fundamentals** | Predict the future from the past — once you check for stationarity first. | ~90 min |
| 16 | **Anomaly Detection** | Define what normal looks like so you can flag whatever doesn't fit. | ~75 min |
| 17 | **Handling Imbalanced Data** | When 99% of your data is "normal," accuracy lies — learn what to do instead. | ~90 min |
| 18 | **Feature Selection** | More features is not better; keeping the right ones is. | ~75 min |

## How each lesson is built

Every lesson in this curriculum follows the same rhythm, so once you learn the shape
you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses, like scikit-learn)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

**Start with the foundation, in order: 01 → 02 → 03.** These three teach the entire ML
training loop (model → cost function → optimize) that every other lesson assumes. Don't
skip them, even if you've heard the terms before.

**Then work through the core algorithms and skills: 04 → 09.** Trees, SVMs, KNN,
unsupervised learning, feature engineering, and evaluation are the everyday toolkit —
these are the ones you'll reach for most in real work.

**Lessons 10 → 13 are the "make it good and make it real" block:** diagnosing errors,
combining models, tuning, and building a proper pipeline. Foundational for anyone
heading toward production.

**Lessons 14 → 18 are specialist tools** — Naive Bayes, time series, anomaly detection,
imbalanced data, and feature selection. Each is self-contained; pull them in when a
problem calls for them, or read them straight through if you're being thorough.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
