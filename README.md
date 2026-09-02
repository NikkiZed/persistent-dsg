# Persistent Scene Graph Memory & Non-Geometric Video Mapping: Reading List & Reference Guide

This repository indexes key literature and architectural frameworks for **spatio-temporal scene graphs, persistent memory, and topological/non-geometric mapping from video streams**.

---

## 📌 Featured Papers

### 1. Spatiotemporal Knowledge Graphs as Persistent Scene Memory for Embodied Question Answering (VL-KnG)
* **Authors:** Mohamad Al Mdfaa, Svetlana Lukina, Timur Akhtyamov, Arthur Nigmatzyanov, Dmitrii Nalberskii, Sergey Zagoruyko, Gonzalo Ferrer
* **Links:** [arXiv:2510.01483](https://arxiv.org/abs/2510.01483) | [HTML Version](https://arxiv.org/html/2510.01483v3)
* **Core Contribution:** 
  * Proposes a training-free framework that constructs queryable spatiotemporal knowledge graphs from monocular egocentric RGB video.
  * Bridges fine-grained local scene graphs and global topological structures **without requiring 3D reconstruction, voxel grids, or depth sensors**.
  * Employs an LLM-driven Spatiotemporal Object Association (STOA) module to preserve entity identities over time, combined with Graph-Enhanced Retrieval (GER) to query persistent memory without re-ingesting raw video frames.

---

### 2. Towards Spatio-Temporal World Scene Graph Generation from Egocentric Video (WSGG / ActionGenome4D)
* **Authors:** Rohith Peddi et al.
* **Links:** [arXiv:2603.13185](https://arxiv.org/abs/2603.13185) | [GitHub Repository](https://github.com/rohithpeddi/WorldSGG)
* **Core Contribution:**
  * Addresses the critical limitation of traditional video scene graphs (VidSGG), which drop objects once they leave the camera frame or become occluded.
  * Formalizes the **World Scene Graph Generation (WSGG)** task: maintaining a world scene graph at every timestamp encompassing both observed and unobserved interacting entities.
  * Introduces the **Persistent World Graph (PWG)** paradigm, implementing object permanence via zero-order feature memory buffers alongside Masked World Auto-Encoder (MWAE) formulations.

---

### 3. Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding
* **Authors:** Yue Fan, Xiaojian Ma, Rongpeng Su, Jun Guo, Rujie Wu, Xi Chen, Qing Li
* **Links:** [arXiv:2501.00358](https://arxiv.org/abs/2501.00358)
* **Core Contribution:**
  * Introduces an LLM-centric agent that builds and maintains persistent structured scene memory over extended embodied sensor trajectories.
  * Decouples long-horizon dynamic reasoning from brute-force context window limits by storing entity states, interactions, and temporal transitions in structured registries.
  * Demonstrates substantial improvements on benchmarks like OpenEQA, Ego4D-VQ3D, and EnvQA.

---

## 🔬 Architectural Comparison

| Dimension | Metric 3D Graphs (e.g., Hydra, Kimera) | Video/Topological Memory (e.g., VL-KnG, WSGG) |
| :--- | :--- | :--- |
| **Input Signals** | RGB-D / LiDAR + Odometry / IMU + Pose | Monocular RGB video stream (chunked / sequential) |
| **Geometry** | Explicit 3D meshes, TSDF voxels, metric centroids | Topological bounding boxes, visual patches, semantic tokens |
| **Association** | 3D Euclidean clearance & ICP registration | Visual Re-ID embeddings (CLIP/DINO) + LLM disambiguation |
| **Permanence** | Anchored to rigid coordinate frames | Temporal state registries & zero-order feature buffers |
| **Query Mechanism** | Ray casting & spatial bounding volume hierarchy | Subgraph traversal, Graph-RAG, & topological retrieval |

---

## 🛠️ Key Design Patterns for Implementation

1. **Chunk-Level Graph Construction:** Process input video streams in short windows (e.g., 2–5 seconds) to extract localized scene graphs (entities, predicates, states).
2. **Topological Entity Consolidation:** Match candidate entity nodes against active memory using visual embedding similarity and semantic verification rather than coordinate proximity.
3. **Staleness & State Management:** Maintain state vectors containing `last_observed_timestamp`, `interaction_status`, and `confidence_score` to handle occluded and out-of-frame objects.
4. **Decoupled Graph Querying:** Execute downstream questions and planning directly on the generated graph schema via Graph-RAG or Graph Neural Networks, bypassing raw video frames during inference.
