# Phase 5: NLP — Foundations to Advanced

> Language is the interface to intelligence. Master every layer.

## Why this phase exists

Language is how humans encode almost everything they know, and it is how we talk
to machines. If you want to build systems that read, answer, translate, search,
or converse, you have to teach a computer to turn messy human text into something
it can compute with — and back again.

This phase walks the whole ladder, from the oldest tricks to the ones shipping in
2026. You start by counting words, then learn to place them in geometric space,
then build the classic NLP tasks (sentiment, entities, translation, summarization),
then arrive at attention — the idea that everything modern is built on. From there
you go deep: retrieval, chunking, embeddings, evaluation, and the plumbing that
makes real language systems work. Nothing here is a black box. You build the core
of each idea before you reach for the library.

## What you need first

You should have finished **Phase 3 (Deep Learning)** — you'll train neural
networks, run backprop, and use PyTorch throughout the second half of this phase.
A little of **Phase 1 (Math Foundations)** helps too: dot products, matrices, and
gradients show up constantly. Several lessons also lean on **Phase 2** classics
like Naive Bayes and linear regression.

If that sounds like a lot, don't worry. Each lesson names its exact prerequisites
at the top, and every idea is rebuilt from scratch before it's used. You are never
expected to already know the answer — you read, run, verify, and move on.

## What you'll be able to do after this phase

- Turn raw text into numbers a model can learn from — tokenization, TF-IDF, and
  subword tokenizers built by hand
- Train and use word and passage embeddings, and understand *why* they place
  related meanings close together
- Build the classic NLP tasks: sentiment, named entities, translation,
  summarization, and question answering
- Explain attention from the ground up and see why it replaced RNNs
- Assemble the pieces of a modern retrieval system — search, chunking, embeddings,
  and reranking
- Evaluate language systems honestly, including LLM-as-judge and long-context tests

## The lessons

Do them in order — this phase builds a ladder, and later lessons lean hard on
earlier ones.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Text Processing — Tokenization, Stemming, Lemmatization** | Get preprocessing wrong and the model learns from garbage. This is the bridge from continuous language to discrete tokens. | ~45 min |
| 02 | **Bag of Words, TF-IDF, and Text Representation** | The dumbest thing that works — and it still beats embeddings on narrow tasks in 2026. | ~75 min |
| 03 | **Word Embeddings — Word2Vec from Scratch** | Train a shallow net on "a word is the company it keeps" and geometry falls out. | ~75 min |
| 04 | **GloVe, FastText, and Subword Embeddings** | Three follow-ups to Word2Vec that fixed its blind spots and bridged toward transformers. | ~45 min |
| 05 | **Sentiment Analysis** | The canonical NLP task — most of classical text classification shows up here. | ~75 min |
| 06 | **Named Entity Recognition** | Pulling names out of text; harder than it sounds once boundaries and jargon get involved. | ~75 min |
| 07 | **POS Tagging and Syntactic Parsing** | Grammar came back the moment LLM pipelines needed to validate structured extraction. | ~45 min |
| 08 | **CNNs and RNNs for Text** | Convolutions learn n-grams, recurrences remember — both superseded by attention, both still useful on constrained hardware. | ~75 min |
| 09 | **Sequence-to-Sequence Models** | Two RNNs pretending to be a translator; the bottleneck they hit is the reason attention exists. | ~75 min |
| 10 | **Attention Mechanism — The Breakthrough** | The decoder stops squinting at a summary and looks at the whole source. Everything after is attention plus engineering. | ~45 min |
| 11 | **Machine Translation** | The task that funded NLP research for thirty years and keeps paying now. | ~75 min |
| 12 | **Text Summarization** | Extractive tells you what the document said; abstractive tells you what the author meant. Different tasks, different pitfalls. | ~75 min |
| 13 | **Question Answering Systems** | Extractive, retrieval-augmented, and generative QA — every modern assistant is a mix of the three. | ~75 min |
| 14 | **Information Retrieval and Search** | BM25 is precise but brittle, dense casts a wide net but misses keywords; hybrid is the 2026 default. | ~75 min |
| 15 | **Topic Modeling — LDA and BERTopic** | Two ways to find the themes in a pile of documents — same goal, different decompositions. | ~45 min |
| 16 | **Text Generation Before Transformers — N-gram Language Models** | Perplexity turns "how surprising was that word" into a number, and smoothing keeps it finite. | ~45 min |
| 17 | **Chatbots — Rule-Based to Neural to LLM Agents** | From ELIZA's pattern matches to tool-running agents; each era fixed the previous one's worst failure. | ~75 min |
| 18 | **Multilingual NLP** | One model, 100+ languages, near-zero training data for most — cross-lingual transfer is the practical miracle of the 2020s. | ~45 min |
| 19 | **Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece** | Word tokenizers choke on unseen words, character ones blow up length; subwords split the difference, and every LLM ships on one. | ~60 min |
| 20 | **Structured Outputs & Constrained Decoding** | Getting JSON "most of the time" is the production problem; constrained decoding edits the logits to make it "always." | ~60 min |
| 21 | **Natural Language Inference — Textual Entailment** | Predicting entailment / contradiction / neutral — boring on the surface, load-bearing in production. | ~60 min |
| 22 | **Embedding Models — The 2026 Deep Dive** | Modern embeddings give a vector per passage; pick the wrong one and your RAG retrieves the wrong thing. | ~60 min |
| 23 | **Chunking Strategies for RAG** | Chunking affects retrieval quality as much as the embedding model — get it wrong and no reranking saves you. | ~60 min |
| 24 | **Coreference Resolution** | Figuring out who "she," "him," and "the doctor" all refer to when nobody is named. | ~60 min |
| 25 | **Entity Linking & Disambiguation** | NER found "Paris"; linking decides *which* Paris, so your knowledge graph stops being ambiguous. | ~60 min |
| 26 | **Relation Extraction & Knowledge Graph Construction** | NER found the nodes; relation extraction finds the edges between them. | ~60 min |
| 27 | **LLM Evaluation — RAGAS, DeepEval, G-Eval** | Exact-match misses meaning and humans don't scale — LLM-as-judge is the production answer, if you calibrate it. | ~75 min |
| 28 | **Long-Context Evaluation — NIAH, RULER, LongBench, MRCR** | Advertised context length is not usable context length; these tests tell you the model's real capacity. | ~60 min |
| 29 | **Dialogue State Tracking** | Keeping the slot-value dict in sync across a multi-turn conversation so the booking actually works. | ~75 min |

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

Go straight down, 01 → 29. This phase is deliberately ordered: representation
(01–04) comes before the classic tasks (05–07), which come before the sequence
models and attention (08–11), which come before the generation and retrieval work
(12–23), which comes before the specialized extraction and evaluation topics
(24–29).

If you're short on time and heading toward LLMs and RAG, the must-do spine is
**01 → 02 → 03 → 10 → 13 → 14 → 19 → 22 → 23 → 27**. But the tasks in between are
where the intuition is built, so come back for them.

When you can build language systems from tokens to attention to retrieval, the
later LLM and agent phases will feel like assembling parts you already understand.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
