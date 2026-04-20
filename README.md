# AI Translator System with Multi-Domain RAG

Expert-level multilingual translation system optimized for context-aware and domain-aware translation using RAG (Retrieval-Augmented Generation). 

## 🚀 Overview
This system uses a multi-stage retrieval pipeline (Vector Search + Cross-Encoder Reranking) to provide high-quality, domain-specific translations. It is optimized for local execution on Mac (using MLX) and standard environments (Transformers).

### Key Features:
- **Context-Aware Translation**: Retrieves relevant context from a massive glossary database.
- **Multi-Domain Support**: Specialized prompts and knowledge bases for Medical, Technical, Economic, and General domains.
- **Hybrid Inference**: Supports local fine-tuned models (MLX/Transformers) and API-based backends.
- **Expert System Prompt**: Advanced instructions for the LLM to follow strict terminology and tone.

---

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nardouhn/ai-translator-system.git
   cd ai-translator-system
   ```

2. **Setup environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## 📦 Data & Model Setup

> [!IMPORTANT]
> The Vector Database and Fine-tuned Model weights are not included in this repository due to their size.

### 1. Vector Database (VectorDB_Gemini)
The system expects a ChromaDB persistent storage at `./VectorDB_Gemini`. You can rebuild it using the indexing scripts or request the pre-built index (~1.9GB) from the maintainer.

### 2. Fine-tuned Model
The default demo points to: `./outputs/completed_model_mlx`.
- You can place your MLX-converted LoRA adapters or full model weights in this directory.
- For standard transformers models, update the `model_path` in `scripts/rag_core/full_flow_demo.py`.

---

## 🖥 How to Run Demo

### Full Flow Demo
This script demonstrates the entire RAG pipeline: retrieval, reranking, prompt formatting, and LLM inference.
```bash
python3 scripts/rag_core/full_flow_demo.py
```
Check `demo_flow_log.md` after completion to see the detailed execution log.

### Terminal UI (Simple)
```bash
python3 main.py
```

---

## 📁 Repository Structure
- `scripts/rag_core/`: Core logic for RAG and LLM coordination.
- `prompt_config.py`: Prompt templates and ChromaDB client setup.
- `data/`: Processed glossaries and knowledge bases.
- `manual_rag_pipeline.md`: Documentation of the system architecture.

---

## 📄 License
[Proprietary/Add License Here]
