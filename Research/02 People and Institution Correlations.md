---
type: correlation-map
origin: primary paper records
verification: primary sources checked; affiliations summarized
reviewed: 2026-11-27
tags: [ai-pedigree, people, institutions, correlations]
---

# People and institution correlations

This note emphasizes repeated collaboration patterns in the audited sources. An institution label refers to the paper-era research home, not a person's current employer. Large papers can have several affiliations; clusters below are analytical summaries, not exhaustive author-by-author employment claims.

## High-density research clusters

| Historical cluster | Repeated personnel in the audited set | Paper families | Vault bridge |
| --- | --- | --- | --- |
| University of Toronto → Google | [[People/Geoffrey Hinton\|Geoffrey Hinton]], [[People/Ilya Sutskever\|Ilya Sutskever]], [[People/Alex Krizhevsky\|Alex Krizhevsky]], [[People/Jeff Dean\|Jeff Dean]], [[People/Noam Shazeer\|Noam Shazeer]], [[People/Oriol Vinyals\|Oriol Vinyals]] | AlexNet; sparse MoE; distillation; SimCLR; Transformer-era scaling | [[Institutions/University of Toronto\|University of Toronto]] · [[Companies/Google\|Google]] · [[10 Hinton Lineage.canvas\|Hinton lineage]] |
| Montréal representation-learning school | [[People/Yoshua Bengio\|Yoshua Bengio]], Dzmitry Bahdanau, Kyunghyun Cho, Pascal Vincent, Hugo Larochelle, Ian Goodfellow | neural attention; denoising autoencoders; GANs; transfer and representation learning | [[Institutions/Université de Montréal\|Université de Montréal]] · [[Institutions/Mila\|Mila]] |
| DeepMind planning and self-supervision | [[People/David Silver\|David Silver]], [[People/Demis Hassabis\|Demis Hassabis]], [[People/Oriol Vinyals\|Oriol Vinyals]], [[People/Julian Schrittwieser\|Julian Schrittwieser]], Timothy Lillicrap, [[People/Koray Kavukcuoglu\|Koray Kavukcuoglu]] | DQN; Matching Networks; CPC; BYOL; AlphaZero; MuZero; Chinchilla | [[Companies/DeepMind\|DeepMind]] · [[Labs/Google DeepMind\|Google DeepMind]] · [[12 Hassabis and DeepMind.canvas\|DeepMind map]] |
| Meta/Facebook AI Research | [[People/Yann LeCun\|Yann LeCun]], [[People/Kaiming He\|Kaiming He]], Patrick Lewis, Douwe Kiela, Ishan Misra, Piotr Bojanowski, Armand Joulin | RAG/DPR; MoCo/MAE; DINO/DINOv2; VICReg; I-JEPA; Toolformer | [[Companies/Meta\|Meta]] · [[Labs/FAIR\|FAIR]] |
| OpenAI post-training and multimodality | [[People/Paul Christiano\|Paul Christiano]], [[People/John Schulman\|John Schulman]], [[People/Alec Radford\|Alec Radford]], [[People/Ilya Sutskever\|Ilya Sutskever]], [[People/Dario Amodei\|Dario Amodei]] | preference learning; PPO; GPT-3; InstructGPT; CLIP; scaling laws | [[Companies/OpenAI\|OpenAI]] |
| Stanford learning and systems | Stefano Ermon, Christopher Ré, Chelsea Finn, Christopher D. Manning, Rafael Rafailov, Tri Dao | DPO; FlashAttention; long-context evaluation | [[Institutions/Stanford University\|Stanford University]] |
| Berkeley systems lineage | Ion Stoica, Joseph E. Gonzalez, Pieter Abbeel, Shishir G. Patil, Woosuk Kwon, Lianmin Zheng, Aviral Kumar | MemGPT; vLLM/PagedAttention; SGLang; DDPM; test-time compute | University of California, Berkeley (entity note not yet in the curated biographical inventory) |
| Princeton agent interfaces | Shunyu Yao, Karthik Narasimhan, John Yang, Carlos E. Jimenez | ReAct; SWE-agent | [[Institutions/Princeton University\|Princeton University]] |
| Microsoft model systems | Qingyun Wu, Chi Wang, Edward J. Hu, Weizhu Chen, Samyam Rajbhandari, Olatunji Ruwase | AutoGen; LoRA; ZeRO | [[Companies/Microsoft\|Microsoft]] |
| University of Washington + Allen Institute for AI | Hannaneh Hajishirzi, Noah A. Smith, Yizhong Wang, Nathan Lambert, Luke Zettlemoyer | Self-Instruct; QLoRA; Tulu 3/RLVR | [[Institutions/University of Washington\|University of Washington]] |
| Anthropic alignment | Yuntao Bai, Amanda Askell, Ethan Perez, [[People/Dario Amodei\|Dario Amodei]] | Constitutional AI / RLAIF | [[Companies/Anthropic\|Anthropic]] |
| DeepSeek reasoning | Zhihong Shao, Daya Guo, Peiyi Wang, Haowei Zhang, Qihao Zhu, Runxin Xu | DeepSeekMath/GRPO; DeepSeek-R1 | [[Companies/DeepSeek\|DeepSeek]] |
| Sutton → DeepMind/Alberta | [[People/Richard Sutton\|Richard Sutton]], [[People/Volodymyr Mnih\|Volodymyr Mnih]], [[People/David Silver\|David Silver]], [[People/Demis Hassabis\|Demis Hassabis]] | TD learning; DQN; AlphaZero; MuZero | [[11 Richard Sutton Lineage.canvas\|Sutton lineage]] · [[Institutions/University of Alberta\|University of Alberta]] |

## People who bridge multiple branches

- [[People/Geoffrey Hinton|Geoffrey Hinton]] connects backpropagation, AlexNet, sparse MoE, distillation, and SimCLR. His role is not one single “deep learning paper”; it spans architecture, training history, efficiency, and representation learning.
- [[People/Oriol Vinyals|Oriol Vinyals]] connects Google/DeepMind work across Matching Networks, CPC, distillation, and compute-optimal language-model training.
- [[People/Kaiming He|Kaiming He]] connects ResNet's supervised vision lineage to MoCo and MAE's self-supervised lineage.
- [[People/Ilya Sutskever|Ilya Sutskever]] connects Toronto/AlexNet to OpenAI's GPT-3 and CLIP era.
- [[People/Yann LeCun|Yann LeCun]] connects the older neural-network lineage to VICReg and I-JEPA, two different strategies for avoiding uninformative self-supervised representations.
- [[People/Paul Christiano|Paul Christiano]], [[People/Jan Leike|Jan Leike]], [[People/Shane Legg|Shane Legg]], and [[People/Dario Amodei|Dario Amodei]] make the 2017 human-preference paper a genuine OpenAI–DeepMind personnel bridge.
- Shunyu Yao and Karthik Narasimhan connect ReAct's reasoning/action loop with SWE-agent's agent–computer interface work.
- Ion Stoica and Joseph E. Gonzalez connect MemGPT, PagedAttention/vLLM, and SGLang, making Berkeley a systems cluster around memory hierarchy and serving rather than a single model family.
- Hannaneh Hajishirzi, Noah A. Smith, Yizhong Wang, and Alisa Liu connect synthetic instruction generation (Self-Instruct) to open post-training and verifiable-reward work (Tulu 3).

## Name-resolution cautions

- **Quoc Le** and **Quoc V. Le** refer to the same researcher; use the vault's [[People/Quoc V. Le|Quoc V. Le]] form.
- **Geoffrey E. Hinton** and **Geoffrey Hinton** are the same person; the middle initial follows the individual paper record.
- **Aaron van den Oord** should retain the lowercase particle when the full name is written.
- **DeepSeek-AI** is a group author on DeepSeek-R1; it should not be modeled as a human.
- The arXiv record for DeepSeekMath abbreviates two names as **Y.K. Li** and **Y. Wu**. Do not silently expand them without an author-controlled source.
- Paper affiliation does not establish employment before or after publication. Avoid converting a coauthorship edge into a supervision, employment, or intellectual-influence edge without separate evidence.

## Structural interpretation

The graph is not a simple company rivalry. It has at least four interacting networks:

1. **Mentorship and education** — Toronto/Hinton and Alberta/Sutton are especially visible in the existing vault.
2. **Coauthorship** — paper teams form temporary, often cross-institution collaborations.
3. **Lab migration** — researchers move among universities and industrial labs, carrying methods and collaborators.
4. **Method inheritance** — later work recombines earlier ideas without requiring a direct personal relationship; for example, MAE combines Transformer-style vision architecture with masked reconstruction.

Only the first three can justify person–institution or person–person relationship claims. Method inheritance belongs in the research map.

[[Research/00 Research Atlas|Research atlas]] · [[Research/01 Source Audit|Source audit]] · [[Research/03 Concept Boundaries|Concept boundaries]]
