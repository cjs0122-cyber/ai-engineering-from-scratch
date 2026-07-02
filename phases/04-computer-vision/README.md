# Phase 4: Computer Vision

> From pixels to understanding — image, video, and 3D.

## Why this phase exists

An image is just a grid of numbers — three values of light per pixel. A photo of
a cat and a photo of a dog are, to a computer, two big tables of numbers that look
almost identical. This phase is about the long climb from those raw numbers to
actual understanding: *what* is in the picture, *where* it is, and even what the
scene would look like from a different angle.

You'll go all the way up. First the foundations — how images are stored, and the
convolution operation that reads them. Then the classic tasks: naming what's in an
image, drawing boxes around objects, labelling every pixel. Then generation — teaching
a network to *make* images, not just read them. And finally the frontier: video that
predicts the future, 3D scenes rebuilt from photos, and the vision-language models
that let you simply *ask* an image a question.

Every idea here is built up from the one before it. You won't be pasting library
calls you don't understand — you'll write a convolution, a detector, and a diffusion
model yourself, then see the real tools that do the same thing at scale.

## What you need first

This is not a starting phase. You need the deep-learning machinery from earlier:

- **Phase 3 (Deep Learning Core)** — layers, backprop, optimizers, PyTorch. This is
  the big one. Convolutions, CNNs, and every model here are built on it.
- **Phase 1 (Math Foundations)** — especially tensor operations and a little
  probability. You'll be reshaping and multiplying multi-dimensional arrays constantly.

If you've finished those, you're ready. A few later lessons also lean on
self-attention from Phase 7 and quantization from Phase 10 — those are called out per
lesson, and you can circle back to them. You do **not** need a giant GPU to learn
this; the early lessons run on a laptop, and the heavier ones tell you when a GPU
helps.

## What you'll be able to do after this phase

- Load, normalize, and correctly wrangle image data so your models actually see what
  you think they see
- Build CNNs from the convolution up, and fine-tune pretrained backbones for your own tasks
- Detect, segment, and track objects — boxes, per-pixel masks, and identities across video
- Generate images with GANs and diffusion, and understand how Stable Diffusion really works
- Work with modern vision transformers, CLIP, and vision-language models that connect images to text
- Reconstruct and reason about 3D — NeRFs, Gaussian splatting, and depth from a single photo
- Wire the pieces into a complete, deployable vision pipeline

## The lessons

Do them in order — this phase is unusually sequential, with each lesson leaning on
the ones before it.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Image Fundamentals — Pixels, Channels, Color Spaces** | An image is a tensor of light samples — get the encoding wrong and everything downstream silently breaks. | ~45 min |
| 02 | **Convolutions from Scratch** | The one operation the whole phase is built on: a tiny weight-sharing filter slid across an image. | ~75 min |
| 03 | **CNNs — LeNet to ResNet** | Every modern backbone is the conv–nonlinearity–downsample recipe plus one new idea; learn them in order. | ~75 min |
| 04 | **Image Classification** | The canonical vision task — pixels in, a probability over classes out. Everything else is plumbing on top. | ~75 min |
| 05 | **Transfer Learning & Fine-Tuning** | Borrow features someone trained on millions of images instead of starting from scratch. | ~75 min |
| 06 | **Object Detection — YOLO from Scratch** | Find and box every object at once — classification plus regression across a feature map. | ~75 min |
| 07 | **Semantic Segmentation — U-Net** | Classify every pixel using an encoder–decoder with skip connections. | ~75 min |
| 08 | **Instance Segmentation — Mask R-CNN** | Separate individual objects, not just categories, by adding a mask branch to a detector. | ~75 min |
| 09 | **Image Generation — GANs** | Two networks in a game — one draws, one critiques — until the drawings fool the critic. | ~75 min |
| 10 | **Image Generation — Diffusion Models** | Learn to denoise, run it backwards a thousand steps, and you have an image generator. | ~75 min |
| 11 | **Stable Diffusion — Architecture & Fine-Tuning** | How real text-to-image works: latent diffusion, cross-attention, and guidance, end to end. | ~75 min |
| 12 | **Video Understanding — Temporal Modeling** | Add the time axis — 3D convs, transformers, or pooling — to reason over sequences of frames. | ~45 min |
| 13 | **3D Vision — Point Clouds & NeRFs** | Answer "what is where in space" from sensor point clouds and learned volumetric fields. | ~45 min |
| 14 | **Vision Transformers (ViT)** | Cut an image into patches, treat each as a word, run a standard transformer. | ~45 min |
| 15 | **Real-Time Vision — Edge Deployment** | Trade accuracy for milliseconds so a model runs at 30 fps on a tiny device. | ~75 min |
| 16 | **Build a Complete Vision Pipeline — Capstone** | Wire this phase's models and rules into one end-to-end production system. | ~120 min |
| 17 | **Self-Supervised Vision — SimCLR, DINO, MAE** | Learn strong visual features from unlabelled images, then fine-tune on a few labelled ones. | ~75 min |
| 18 | **Open-Vocabulary Vision — CLIP** | Train image and text encoders together so matching pairs land at the same point in space. | ~45 min |
| 19 | **OCR & Document Understanding** | Detect, recognize, and lay out text — turning pixels of documents into structured data. | ~45 min |
| 20 | **Image Retrieval & Metric Learning** | Rank images by distance in an embedding space, and shape that space so distances mean something. | ~45 min |
| 21 | **Keypoint Detection & Pose Estimation** | Locate ordered keypoints via heatmap regression to recover body and object poses. | ~45 min |
| 22 | **3D Gaussian Splatting from Scratch** | Represent a scene as millions of 3D Gaussians and backprop through their rasterization. | ~90 min |
| 23 | **Diffusion Transformers & Rectified Flow** | Swap the U-Net for a transformer and a straight-line flow — the recipe behind SD3 and FLUX. | ~75 min |
| 24 | **SAM 3 & Open-Vocabulary Segmentation** | Prompt an image with text and get masks for every matching object in one forward pass. | ~60 min |
| 25 | **Vision-Language Models — The ViT-MLP-LLM Pattern** | The ViT-MLP-LLM stack behind every production model that can look at an image and talk about it. | ~75 min |
| 26 | **Monocular Depth & Geometry Estimation** | Predict per-pixel distance from a single RGB frame using a frozen ViT and a light head. | ~60 min |
| 27 | **Multi-Object Tracking & Video Memory** | Keep object identities across frames — detection plus association over time. | ~60 min |
| 28 | **World Models & Video Diffusion** | Predict the next seconds of a scene, condition on actions, and you have a learned simulator. | ~75 min |

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

Go straight down the list. Lessons 01–05 are the non-negotiable foundation —
images, convolutions, CNNs, classification, and transfer learning. Don't skip them
even if you're tempted; almost everything after depends on them.

From lesson 06 onward the tasks branch out (detection, segmentation, generation, 3D,
video, vision-language). You can follow your interest, but the numbering already puts
prerequisites before the lessons that use them, so in-order is the safe default. Lesson
16 is a capstone that pulls the first half together — a good place to consolidate before
pushing into the frontier lessons (17–28).

If a lesson references a Phase 7 (attention) or Phase 10 (quantization) idea you
haven't met yet, that's fine — read that one lesson and come back.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
