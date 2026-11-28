---
type: concept-map
origin: audited research reports
verification: primary sources checked
reviewed: 2026-11-27
tags: [ai-pedigree, concepts, terminology]
---

# Concept boundaries

The most useful result of the reports is not a longer jargon list; it is a set of boundaries between things that are often conflated.

## System boundaries

| Do not conflate | Boundary |
| --- | --- |
| MCP ↔ ReAct ↔ Toolformer | MCP standardizes integration; ReAct is a reasoning/action prompting pattern; Toolformer trains a model to decide when and how to call tools. |
| Skill ↔ tool ↔ sandbox | A skill packages instructions and resources. A tool exposes an operation. A sandbox constrains execution. None automatically supplies the others. |
| Tool visibility ↔ authorization | Removing a tool description from model context reduces discoverability; an enforced permission check denies access. |
| Persistent record ↔ active context ↔ KV cache | Durable storage survives calls; active context is the selected token sequence; a KV cache reuses attention states during inference. |
| Embedding ↔ index ↔ retriever ↔ RAG | An embedding is a representation; an index searches representations; a retriever selects items; RAG supplies retrieved items to generation. |
| Context capacity ↔ effective use | A model accepting a long sequence does not imply equal use of information at all positions. |
| FlashAttention ↔ PagedAttention | FlashAttention reduces attention I/O; PagedAttention manages KV-cache allocation across serving requests. |
| Tensor/pipeline parallelism ↔ ZeRO/FSDP | The former partition model computation; the latter shard training state to reduce duplication. |

## Learning boundaries

| Do not conflate | Boundary |
| --- | --- |
| Architecture ↔ objective ↔ data source | ViT is an architecture; MAE's masked reconstruction is an objective; real, simulated, or generated images are data sources. |
| Backpropagation ↔ supervision type | Backpropagation computes gradients for many objectives; its use does not make training supervised or self-supervised. |
| Self-supervision ↔ synthetic data | Masking, corruption, temporal structure, or augmented views can create targets from real data. No synthetic corpus or teacher LLM is required. |
| Self-distillation ↔ external teacher | BYOL and DINO maintain a target/teacher derived during training; this need not be a separately pretrained large model. |
| Representation collapse ↔ recursive model collapse | The first is an objective/optimization failure yielding uninformative representations; the second is distributional degradation from repeated training on generated data. |
| Contrastive ↔ non-contrastive SSL | SimCLR/MoCo use positive and negative relationships; BYOL can learn without explicit negative pairs; VICReg explicitly regularizes variance and covariance. |
| ViT ↔ MAE ↔ I-JEPA | ViT tokenizes images into patches; MAE reconstructs masked pixels; I-JEPA predicts target representations. |
| CLIP ↔ SimCLR | CLIP aligns paired image/text data; SimCLR aligns augmented views of an image. |
| Transfer learning ↔ linear probing | Transfer learning reuses representations broadly; a linear probe is one evaluation protocol with the encoder frozen. No universal score certifies understanding. |

## Post-training and inference boundaries

| Do not conflate | Boundary |
| --- | --- |
| Few-shot learning ↔ few-shot prompting | The first is a broad learning setting; the second supplies demonstrations at inference without a weight update. |
| SFT/instruction tuning ↔ in-context learning | SFT updates weights from demonstrations; in-context learning conditions behavior through the prompt. |
| RLHF ↔ PPO | RLHF names the feedback/training setup; PPO is one policy-optimization algorithm that may be used within it. |
| RLAIF ↔ Constitutional AI | RLAIF names AI-generated feedback broadly; Constitutional AI is a principles-guided implementation. |
| RLVR ↔ GRPO | RLVR describes a verifiable reward source; GRPO describes an optimization method. They can be combined. |
| DPO ↔ reward-model-plus-RL pipeline | Standard DPO optimizes preference pairs directly rather than separately fitting a reward model and running online RL. |
| Chain of thought ↔ self-consistency ↔ test-time compute | CoT elicits intermediate steps; self-consistency samples and aggregates paths; test-time compute is the broader budget spent on generation, checking, search, or revision. |
| LoRA ↔ QLoRA | LoRA trains low-rank adapters with a frozen base; QLoRA adds a quantized frozen base to reduce memory. |

## Generative-model boundaries

| Family | Core distinction |
| --- | --- |
| VAE | Probabilistic latent-variable model trained through variational inference. |
| GAN | Generator and discriminator trained adversarially. |
| Diffusion / DDPM | Learns to reverse a gradual corruption process. |
| Latent diffusion | Runs diffusion in a learned compressed representation. |
| Flow matching | Regresses a vector field along probability paths. |
| Rectified flow | A related transport formulation emphasizing straightened paths; not simply a synonym for every flow-matching method. |

## Claims explicitly rejected

- A fixed **100:1 unlabeled-to-labeled data ratio** is not a general requirement for self-supervised learning.
- An **80–85% linear-probe result** is not a universal certification of useful or general representations.
- A **0.85 cosine-similarity threshold** has no universal semantic meaning across models and tasks.
- SSL is not universally better than supervised learning; results depend on data, objective, architecture, and evaluation.
- Retrieved text normally changes the model's input, not its trained weights.

[[Research/00 Research Atlas|Research atlas]] · [[Research/01 Source Audit|Source audit]] · [[Research/02 People and Institution Correlations|People and institutions]]
