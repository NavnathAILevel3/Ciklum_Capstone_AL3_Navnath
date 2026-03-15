# Ciklum AI Academy 2026: Capstone Project (AL Level-3)
## Personal Achievement Agent: A RAG-Based Summarizer

### Project Overview
This project implements an Autonomous AI Agent designed for secure interaction with private datasets.  
Developed as the final capstone for the **Ciklum AI Academy 2026**, the agent utilizes a Retrieval-Augmented Generation (RAG) architecture to transform raw achievement notes into high-impact professional summaries.

---

### Technical Stack
- **LLM Engine**: Google Gemini 2.5 Flash
- **Framework**: LangChain (`langchain-google-genai`)
- **Architecture**: RAG (local file retrieval + LLM synthesis)
- **Environment**: Python 3.14

---

### Key Features & Learning Outcomes
- **RAG Pipeline**: Implemented a local retrieval system that augments LLM prompts with private data without requiring external vector databases for small-scale datasets.
- **Hyperparameter Optimization**: Mastered Temperature settings (tuned to 0.7) to balance professional creativity with factual grounding.
- **Resilient Integration**: Built a robust connection to the Google GenAI ecosystem, ensuring compatibility with the latest 2026 SDK standards.

---

### Achievements
- **Project Context**: Built during the Ciklum AI Academy 2026.
- **Core Feature**: Implemented a Retrieval-Augmented Generation (RAG) system for secure, conversational interaction with private datasets.
- **Learning Outcome**: Mastered Temperature settings to balance creativity with factual accuracy in generative outputs.

---

### Outputs
- `Agent_Final_Report.txt` → Refined project summary after self-reflection.
- `Agent_LinkedIn_Post.txt` → Professional LinkedIn-style post deliverable (published on GitHub).
- `Final_Summary.txt` → Consolidated file containing draft, refined summary, and LinkedIn-style post.

---

### Architecture
See `architecture.mmd` for a visual diagram of the agentic workflow:  
**retrieval → reasoning → reflection → post generation → tool-calling outputs**

---

### How to Run
1. Ensure `achievements.txt` and `main.py` are in the same directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
