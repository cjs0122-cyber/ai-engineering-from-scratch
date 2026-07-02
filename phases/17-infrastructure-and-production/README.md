# Phase 17: Infrastructure & Production

> Ship AI to the real world. Scale, monitor, optimize.

## Why this phase exists

A model that works in your notebook is not a product. The moment real users hit
it, a whole new set of problems shows up: it has to be fast enough that people
don't leave, cheap enough that you don't go broke, reliable enough to survive a
bad night, and observable enough that you can tell *why* it broke at 3am.

This phase is the bridge from "the model runs" to "the model runs in production,
for thousands of people, without you babysitting it." You'll learn how inference
actually gets served (vLLM, SGLang, TensorRT-LLM), how to make it faster and
cheaper (quantization, caching, batching, routing), how to keep it up (autoscaling,
multi-region, chaos engineering, SRE), and how to stay out of trouble (security,
compliance, FinOps). This is the least glamorous and most valuable engineering in
the whole stack — it's the difference between a demo and a business.

## What you need first

- **Phase 11 (LLM Engineering)** — you should already know how to call, prompt,
  and evaluate an LLM. This phase is about running one at scale, not using one.
- **Phase 0 (Setup & Tooling)**, especially the **Docker** lesson — most of
  production is containers and Kubernetes. If Docker is fuzzy, do that lesson first.
- **The model-building phases broadly** (roughly 10 and 13) — quantization,
  serving internals, and tools/protocols all lean on ideas introduced earlier.

You do not need a GPU or a cloud account to learn from these lessons. Most of the
value is in the decision frameworks and the "why," which read fine on a laptop.
When a lesson has hands-on code, it says so, and it's built to run small.

## What you'll be able to do after this phase

- Choose an inference platform or serving engine (vLLM, SGLang, TensorRT-LLM,
  llama.cpp, Ollama) with the tradeoffs written down, not guessed
- Cut latency and cost with quantization, prompt/semantic caching, batch APIs,
  speculative decoding, and model routing — and measure the wins honestly
- Scale serving on Kubernetes with GPU-aware autoscaling and multi-region routing
- Instrument the metrics that actually matter (TTFT, TPOT, goodput, P99) and pick
  an observability stack
- Roll out new models safely with shadow traffic, canaries, and A/B tests, and
  roll back in seconds when something's wrong
- Keep a production LLM secure, compliant, and financially accountable

## The lessons

Do them roughly in order — the serving-internals lessons (04, 06, 07) are the
technical spine that later cost and reliability lessons build on.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI** | The three hyperscaler options and how to choose by model catalog and cost surface, not vibes. | ~60 min |
| 02 | **Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale** | The 2026 inference market decoded into a matrix you can actually decide from. | ~60 min |
| 03 | **GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling** | How to scale GPU nodes without killing running jobs or waiting on partial allocations. | ~75 min |
| 04 | **vLLM Serving Internals: PagedAttention, Continuous Batching, Chunked Prefill** | The three defaults that make vLLM the production standard — the technical spine of the phase. | ~75 min |
| 05 | **EAGLE-3 Speculative Decoding in Production** | Free tokens from a draft model — but only if you measure the acceptance rate first. | ~60 min |
| 06 | **SGLang and RadixAttention for Prefix-Heavy Workloads** | Cache-aware scheduling that wins big on RAG and repeated-prefix traffic. | ~75 min |
| 07 | **TensorRT-LLM on Blackwell with FP8 and NVFP4** | NVIDIA's closed stack that trades portability for a large throughput and cost edge. | ~75 min |
| 08 | **Inference Metrics — TTFT, TPOT, ITL, Goodput, P99** | The four numbers that decide if a deployment works — and the measurement traps that hide the truth. | ~60 min |
| 09 | **Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4** | Which quantization format to use is a function of hardware, engine, and workload — not one answer. | ~75 min |
| 10 | **Cold Start Mitigation for Serverless LLMs** | Stopping a 5-20 minute model load from becoming a serverless outage. | ~60 min |
| 11 | **Multi-Region LLM Serving and KV Cache Locality** | Why round-robin routing is harmful for cached inference, and what to do instead. | ~60 min |
| 12 | **Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson** | Running models on-device where memory bandwidth, not compute, is the real limit. | ~60 min |
| 13 | **LLM Observability Stack Selection** | Choosing between dev platforms and gateway/telemetry tools for tracing production LLMs. | ~60 min |
| 14 | **Prompt Caching and Semantic Caching Economics** | When caching pays off and how to reason about the economics before you quote a number. | ~60 min |
| 15 | **Batch APIs — the 50% Discount as Industry Standard** | If a workload isn't interactive, it belongs on batch — this is money left on the table until it moves. | ~45 min |
| 16 | **Model Routing as a Cost-Reduction Primitive** | Send easy queries to cheap models and hard ones to frontier models, without quality regression. | ~60 min |
| 17 | **Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d** | Splitting compute-bound prefill from memory-bound decode onto separate GPU pools for big gains. | ~75 min |
| 18 | **vLLM Production Stack with LMCache KV Offloading** | The reference Kubernetes deployment plus KV offloading to reuse cache across queries and engines. | ~60 min |
| 19 | **AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost** | The layer between your apps and model providers: routing, fallback, secrets, guardrails, observability. | ~60 min |
| 20 | **Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs** | Shipping new models safely when there are no unit tests and failure modes are diffuse. | ~60 min |
| 21 | **A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem** | Evals ask "can the model do it?"; A/B tests ask "do users care?" — you need both. | ~60 min |
| 22 | **Load Testing LLM APIs — Why k6 and Locust Lie** | Traditional load testers mislead on streaming and token metrics — how to load test LLMs correctly. | ~75 min |
| 23 | **SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection** | Using LLMs grounded in your infra to investigate and coordinate incidents, with humans on judgment calls. | ~60 min |
| 24 | **Chaos Engineering for LLM Production** | Deliberately breaking things — provider outages, KV eviction storms — to prove your system survives. | ~60 min |
| 25 | **Security — Secrets, API Key Rotation, Audit Logs, Guardrails** | Killing secret sprawl, rotating keys, and locking down egress so a leaked credential isn't game over. | ~60 min |
| 26 | **Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001** | The frameworks enterprise deals require, and what the EU AI Act actually means for shipping to EU users. | ~60 min |
| 27 | **FinOps for LLMs — Unit Economics and Multi-Tenant Attribution** | Attributing token spend per user, task, and tenant so cost is a metric you control, not a surprise. | ~60 min |
| 28 | **Self-Hosted Serving Selection — llama.cpp, Ollama, TGI, vLLM, SGLang** | The capstone decision: which engine to run where, based on hardware, scale, and ecosystem. | ~45 min |

## How each lesson is built

Every lesson in this whole curriculum follows the same rhythm, so once you learn the
shape you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

**Start with the spine.** Do **04 (vLLM Internals)**, **06 (SGLang)**, and
**08 (Inference Metrics)** early — almost every later lesson assumes you understand
serving internals and how to measure them.

**Then follow your goal.** If you're optimizing cost, pull in **09 (Quantization)**,
**14 (Caching)**, **15 (Batch APIs)**, **16 (Model Routing)**, and **27 (FinOps)**.
If you're optimizing reliability, focus on **03 (Autoscaling)**, **11 (Multi-Region)**,
**20 (Progressive Deployment)**, **23 (SRE)**, and **24 (Chaos Engineering)**.

**Finish with 28 (Self-Hosted Serving Selection)** as the capstone — it ties the
serving-engine tradeoffs together into one decision. Don't rush the platform and
economics lessons (01, 02, 19); a good choice there saves you months later.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
