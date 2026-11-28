---
type: source-audit
origin: two supplied research reports + primary-source verification
verification: primary sources checked
reviewed: 2026-11-27
tags: [ai-pedigree, sources, landmark-papers]
---

# Source audit

Every distinct source named in the supplied reports was checked against its primary publisher, official specification repository, conference record, or arXiv record. The reports are broadly reliable. Corrections and qualifications appear first; the registry then provides stable links and canonical names.

## Corrections and qualifications

1. **MCP version:** `2025-11-25` is now a legacy, handshake-based revision. The current revision is [2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/index.mdx): it removes protocol-level sessions and the initialization handshake, puts version and capabilities in per-request metadata, and adds `server/discover`. The host–client–server distinction and tools/resources/prompts distinction remain valid.
2. **MCP is not a sandbox:** the current specification explicitly leaves consent, authorization, access controls, and isolation to implementations. Tool visibility and permission enforcement remain different controls.
3. **Agent Skills:** the current [open specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) defines a directory containing a required `SKILL.md` plus optional scripts, references, and assets. A skill packages procedure and context; it is not by itself a deterministic executor or security boundary.
4. **Publication years:** ResNet and several other papers use first-public-release years in the reports; venue years may be one year later. SGLang is a 2023 preprint/2024 systems paper. DINO and VICReg were first posted in 2021 and published later.
5. **Names:** use **Dzmitry Bahdanau**, **Aaron van den Oord**, **Diederik P. Kingma**, **Mahmoud Assran**, and **Ilia Shumailov**. Preserve initials in the DeepSeekMath arXiv author list where the primary record does not expand them. “RLFH” is a typo for **RLHF**.
6. **DQN:** the 2013 arXiv paper is distinct from the expanded 2015 *Nature* article. The reports correctly use the 2013 paper as the named source.
7. **Self-supervision terminology:** CPC, MoCo, and context prediction use “unsupervised” in their own titles or framing. Treat SSL and unsupervised learning as overlapping historical vocabularies, not a clean division based on backpropagation.

## Protocols and agent systems

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| MCP | Model Context Protocol maintainers; current revision 2026-07-28 | [Specification](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/index.mdx) · [architecture](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/architecture/index.mdx) · [changelog](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx) |
| Agent Skills | Agent Skills open-format maintainers | [Format specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) |
| Workflows and agents | Erik S. and Barry Zhang, “Building Effective Agents” (2024) | [Anthropic engineering article](https://www.anthropic.com/research/building-effective-agents) |
| ReAct | Shunyu Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models” (2022) | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| Toolformer | Timo Schick et al., “Toolformer: Language Models Can Teach Themselves to Use Tools” (2023) | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) |
| Agent–computer interface | John Yang et al., “SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering” (2024) | [arXiv:2405.15793](https://arxiv.org/abs/2405.15793) |
| Multi-agent orchestration | Qingyun Wu et al., “AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation” (2023) | [arXiv:2308.08155](https://arxiv.org/abs/2308.08155) |
| Indirect prompt injection | Kai Greshake et al., “Not what you've signed up for…” (2023) | [arXiv:2302.12173](https://arxiv.org/abs/2302.12173) |

## Memory, retrieval, and inference systems

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| Persistent vs active context | Charles Packer et al., “MemGPT: Towards LLMs as Operating Systems” (2023) | [arXiv:2310.08560](https://arxiv.org/abs/2310.08560) |
| Word embeddings | Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean (2013) | [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) |
| Dense retrieval | Vladimir Karpukhin et al., “Dense Passage Retrieval…” (2020) | [arXiv:2004.04906](https://arxiv.org/abs/2004.04906) |
| HNSW | Yu. A. Malkov and D. A. Yashunin (2016) | [arXiv:1603.09320](https://arxiv.org/abs/1603.09320) |
| RAG | Patrick Lewis et al., “Retrieval-Augmented Generation…” (2020) | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) |
| Effective long-context use | Nelson F. Liu et al., “Lost in the Middle…” (2023) | [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) |
| Prefill, decoding, KV cache | Reiner Pope et al., “Efficiently Scaling Transformer Inference” (2022) | [arXiv:2211.05102](https://arxiv.org/abs/2211.05102) |
| PagedAttention / vLLM | Woosuk Kwon et al. (2023) | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180) |
| Prefix caching / model programs | Lianmin Zheng et al., “SGLang…” (2023) | [arXiv:2312.07104](https://arxiv.org/abs/2312.07104) |

## Architecture, scale, and distributed computation

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| Subword units / BPE | Rico Sennrich, Barry Haddow, Alexandra Birch (2015) | [arXiv:1508.07909](https://arxiv.org/abs/1508.07909) |
| Neural attention | Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio (2014) | [arXiv:1409.0473](https://arxiv.org/abs/1409.0473) |
| Transformer | Ashish Vaswani et al., “Attention Is All You Need” (2017) | [[Sources/R22\|R22]] · [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) |
| RoPE | Jianlin Su et al., “RoFormer…” (2021) | [arXiv:2104.09864](https://arxiv.org/abs/2104.09864) |
| FlashAttention | Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré (2022) | [arXiv:2205.14135](https://arxiv.org/abs/2205.14135) |
| Tensor parallelism | Mohammad Shoeybi et al., “Megatron-LM…” (2019) | [arXiv:1909.08053](https://arxiv.org/abs/1909.08053) |
| Pipeline parallelism | Yanping Huang et al., “GPipe…” (2018) | [arXiv:1811.06965](https://arxiv.org/abs/1811.06965) |
| ZeRO | Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, Yuxiong He (2019) | [arXiv:1910.02054](https://arxiv.org/abs/1910.02054) |
| FSDP | Yanli Zhao et al., “PyTorch FSDP…” (2023) | [arXiv:2304.11277](https://arxiv.org/abs/2304.11277) |
| Scaling laws | Jared Kaplan et al. (2020) | [arXiv:2001.08361](https://arxiv.org/abs/2001.08361) |
| Compute-optimal training | Jordan Hoffmann et al., “Training Compute-Optimal Large Language Models” (2022) | [arXiv:2203.15556](https://arxiv.org/abs/2203.15556) |
| Sparse MoE | Noam Shazeer et al. (2017) | [arXiv:1701.06538](https://arxiv.org/abs/1701.06538) |

## Representation learning and vision

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| Backpropagation landmark | David E. Rumelhart, [[People/Geoffrey Hinton\|Geoffrey E. Hinton]], Ronald J. Williams (1986) | [Nature DOI 10.1038/323533a0](https://www.nature.com/articles/323533a0) |
| AlexNet | [[People/Alex Krizhevsky\|Alex Krizhevsky]], [[People/Ilya Sutskever\|Ilya Sutskever]], [[People/Geoffrey Hinton\|Geoffrey E. Hinton]] (2012) | [NeurIPS proceedings](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c-Abstract.html) |
| ResNet | [[People/Kaiming He\|Kaiming He]], Xiangyu Zhang, Shaoqing Ren, Jian Sun (2015; CVPR 2016) | [arXiv:1512.03385](https://arxiv.org/abs/1512.03385) |
| Denoising autoencoder | Pascal Vincent, Hugo Larochelle, [[People/Yoshua Bengio\|Yoshua Bengio]], Pierre-Antoine Manzagol (2008) | [ICML paper](https://icml.cc/2008/papers/592.pdf) · [DOI record](https://mlanthology.org/icml/2008/vincent2008icml-extracting/) |
| Context prediction | Carl Doersch, Abhinav Gupta, Alexei A. Efros (2015) | [arXiv:1505.05192](https://arxiv.org/abs/1505.05192) |
| BERT / masked LM | Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova (2018) | [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) |
| CPC / InfoNCE | Aaron van den Oord, Yazhe Li, [[People/Oriol Vinyals\|Oriol Vinyals]] (2018) | [arXiv:1807.03748](https://arxiv.org/abs/1807.03748) |
| SimCLR | Ting Chen, Simon Kornblith, Mohammad Norouzi, [[People/Geoffrey Hinton\|Geoffrey Hinton]] (2020) | [arXiv:2002.05709](https://arxiv.org/abs/2002.05709) |
| MoCo | [[People/Kaiming He\|Kaiming He]], Haoqi Fan, Yuxin Wu, Saining Xie, Ross Girshick (2019) | [arXiv:1911.05722](https://arxiv.org/abs/1911.05722) |
| BYOL | Jean-Bastien Grill et al. (2020) | [arXiv:2006.07733](https://arxiv.org/abs/2006.07733) |
| DINO | Mathilde Caron et al. (2021) | [arXiv:2104.14294](https://arxiv.org/abs/2104.14294) |
| DINOv2 | Maxime Oquab et al. (2023) | [arXiv:2304.07193](https://arxiv.org/abs/2304.07193) |
| VICReg / collapse | Adrien Bardes, Jean Ponce, [[People/Yann LeCun\|Yann LeCun]] (2021) | [arXiv:2105.04906](https://arxiv.org/abs/2105.04906) |
| Vision Transformer | Alexey Dosovitskiy et al. (2020) | [arXiv:2010.11929](https://arxiv.org/abs/2010.11929) |
| MAE | [[People/Kaiming He\|Kaiming He]] et al. (2021) | [arXiv:2111.06377](https://arxiv.org/abs/2111.06377) |
| I-JEPA | Mahmoud Assran et al. (2023) | [arXiv:2301.08243](https://arxiv.org/abs/2301.08243) |
| CLIP | [[People/Alec Radford\|Alec Radford]] et al. (2021) | [arXiv:2103.00020](https://arxiv.org/abs/2103.00020) |
| Transferability / linear probes | Jason Yosinski, Jeff Clune, [[People/Yoshua Bengio\|Yoshua Bengio]], Hod Lipson (2014) | [arXiv:1411.1792](https://arxiv.org/abs/1411.1792) |

## Prompting, feedback, and model adaptation

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| Few-shot prompting / GPT-3 | Tom B. Brown et al. (2020) | [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) |
| Few-shot learning | [[People/Oriol Vinyals\|Oriol Vinyals]] et al., “Matching Networks…” (2016) | [arXiv:1606.04080](https://arxiv.org/abs/1606.04080) |
| Instruction tuning / FLAN | Jason Wei et al. (2021) | [arXiv:2109.01652](https://arxiv.org/abs/2109.01652) |
| Human-preference RL | [[People/Paul Christiano\|Paul Christiano]], [[People/Jan Leike\|Jan Leike]], Tom B. Brown, Miljan Martic, [[People/Shane Legg\|Shane Legg]], [[People/Dario Amodei\|Dario Amodei]] (2017) | [arXiv:1706.03741](https://arxiv.org/abs/1706.03741) |
| InstructGPT / RLHF | Long Ouyang et al. (2022) | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) |
| PPO | [[People/John Schulman\|John Schulman]] et al. (2017) | [arXiv:1707.06347](https://arxiv.org/abs/1707.06347) |
| DPO | Rafael Rafailov et al. (2023) | [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) |
| Constitutional AI / RLAIF | Yuntao Bai et al. (2022) | [arXiv:2212.08073](https://arxiv.org/abs/2212.08073) |
| GRPO | Zhihong Shao et al., “DeepSeekMath…” (2024) | [arXiv:2402.03300](https://arxiv.org/abs/2402.03300) |
| RLVR | Nathan Lambert et al., “Tulu 3…” (2024) | [arXiv:2411.15124](https://arxiv.org/abs/2411.15124) |
| Reasoning RL | DeepSeek-AI et al., “DeepSeek-R1…” (2025) | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) |
| Chain of thought | Jason Wei et al. (2022) | [arXiv:2201.11903](https://arxiv.org/abs/2201.11903) |
| Self-consistency | Xuezhi Wang et al. (2022) | [arXiv:2203.11171](https://arxiv.org/abs/2203.11171) |
| Test-time compute | Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (2024) | [arXiv:2408.03314](https://arxiv.org/abs/2408.03314) |
| LoRA | Edward J. Hu et al. (2021) | [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) |
| QLoRA | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer (2023) | [arXiv:2305.14314](https://arxiv.org/abs/2305.14314) |
| Knowledge distillation | [[People/Geoffrey Hinton\|Geoffrey Hinton]], [[People/Oriol Vinyals\|Oriol Vinyals]], [[People/Jeff Dean\|Jeff Dean]] (2015) | [arXiv:1503.02531](https://arxiv.org/abs/1503.02531) |

## Synthetic data and generative modeling

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| Self-Instruct | Yizhong Wang et al. (2022) | [arXiv:2212.10560](https://arxiv.org/abs/2212.10560) |
| Domain randomization | Josh Tobin et al. (2017) | [arXiv:1703.06907](https://arxiv.org/abs/1703.06907) |
| Deduplication / contamination | Katherine Lee et al. (2021) | [arXiv:2107.06499](https://arxiv.org/abs/2107.06499) |
| Recursive model collapse | Ilia Shumailov et al. (2023) | [arXiv:2305.17493](https://arxiv.org/abs/2305.17493) |
| VAE | Diederik P. Kingma and [[People/Max Welling\|Max Welling]] (2013) | [arXiv:1312.6114](https://arxiv.org/abs/1312.6114) |
| GAN | Ian J. Goodfellow et al. (2014) | [arXiv:1406.2661](https://arxiv.org/abs/1406.2661) |
| Diffusion foundation | Jascha Sohl-Dickstein et al. (2015) | [arXiv:1503.03585](https://arxiv.org/abs/1503.03585) |
| DDPM | Jonathan Ho, Ajay Jain, Pieter Abbeel (2020) | [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) |
| Latent diffusion | Robin Rombach et al. (2021; CVPR 2022) | [arXiv:2112.10752](https://arxiv.org/abs/2112.10752) |
| Flow matching | Yaron Lipman et al. (2022) | [arXiv:2210.02747](https://arxiv.org/abs/2210.02747) |
| Rectified flow | Xingchao Liu, Chengyue Gong, Qiang Liu (2022) | [arXiv:2209.03003](https://arxiv.org/abs/2209.03003) |

## Reinforcement learning and planning

| Anchor | Canonical source and personnel | Checked primary source |
| --- | --- | --- |
| Temporal-difference learning | [[People/Richard Sutton\|Richard S. Sutton]] (1988) | [Machine Learning DOI record](https://mlanthology.org/mlj/1988/sutton1988mlj-learning/) |
| DQN | [[People/Volodymyr Mnih\|Volodymyr Mnih]] et al. (2013) | [arXiv:1312.5602](https://arxiv.org/abs/1312.5602) |
| AlphaZero | [[People/David Silver\|David Silver]] et al. (2017) | [arXiv:1712.01815](https://arxiv.org/abs/1712.01815) |
| MuZero | [[People/Julian Schrittwieser\|Julian Schrittwieser]] et al. (2019) | [arXiv:1911.08265](https://arxiv.org/abs/1911.08265) |

[[Research/00 Research Atlas|Research atlas]] · [[Research/02 People and Institution Correlations|People and institutions]] · [[Research/03 Concept Boundaries|Concept boundaries]]
