---
type: research-hub
aliases: [Landmark AI paper atlas, AI terminology research map]
origin: source audit
verification: primary sources checked
reviewed: 2026-11-27
tags: [ai-pedigree, research-atlas, moc]
---

# Research atlas

This branch maps the landmark papers and specifications behind common AI terminology. It complements the vault's biographical lineage: the existing maps answer **who trained or worked with whom**; this branch answers **which paper connected which people, institutions, and ideas**.

## Navigate

- [[Research/01 Source Audit|Source audit]] — checked primary records for every source named in the two research reports, with corrected dates and canonical titles.
- [[Research/02 People and Institution Correlations|People and institution correlations]] — recurring teams, lab clusters, and cross-institution bridges.
- [[Research/03 Concept Boundaries|Concept boundaries]] — distinctions that prevent category errors.
- [[22 Landmark Research Atlas.canvas|Visual map]] — paper families connected to the relevant people and organizations.

## Three layers

1. **System and protocol layer** — MCP, Agent Skills, harnesses, tools, authorization, retrieval, context selection, inference serving, and distributed training.
2. **Learning layer** — objectives and feedback sources: supervised learning, self-supervision, preference feedback, verifiable rewards, synthetic data, and reinforcement learning.
3. **Model layer** — architectures and algorithms: Transformers, CNNs, ViTs, MoE, diffusion, flow matching, DQN, AlphaZero, and MuZero.

Do not collapse these layers. A Transformer is an architecture, masked reconstruction is an objective, and synthetic data is a data source. Likewise, MCP is an integration protocol, ReAct is an inference pattern, and Toolformer is a training method for tool use.

## Suggested reading paths

### Language models and post-training

Attention → Transformer → GPT-3/in-context learning → InstructGPT/RLHF → chain of thought → RAG → DPO → DeepSeekMath/GRPO.

### Agent systems

MCP architecture → Agent Skills specification → ReAct → Toolformer → SWE-agent → indirect prompt injection → MemGPT.

### Self-supervised vision

Denoising autoencoders → context prediction → CPC/InfoNCE → SimCLR/MoCo → BYOL → DINO/DINOv2 → MAE → I-JEPA.

### Sutton–DeepMind branch

TD learning → DQN → AlphaZero → MuZero. Continue through the existing [[11 Richard Sutton Lineage.canvas|Richard Sutton lineage]] and [[12 Hassabis and DeepMind.canvas|Hassabis and DeepMind map]].

## Audit conventions

- Years are first public release years unless a venue year is explicitly shown.
- Paper author lists are taken from the linked primary record. Institution labels in the correlation note mean affiliation at or around publication, not present employment.
- “Landmark” means a useful anchor, not necessarily the first invention of the broad idea.
- Specifications and engineering articles are separated from peer-reviewed papers.
- No universal 100:1 data ratio, 80–85% linear-probe threshold, or 0.85 cosine-similarity threshold is treated as a general guarantee.

[[00 Start Here|Start here]] · [[01 Map Index|Map index]]
