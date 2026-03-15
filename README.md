# Ciklum AI Academy 2026: Capstone Project (AL Level-3)
## Personal Achievement Agent: A RAG-Based Summarizer

### Project Overview
This project implements an Autonomous AI Agent designed for secure interaction with private datasets. Developed as the final capstone for the Ciklum AI Academy, the agent utilizes a Retrieval-Augmented Generation (RAG) architecture to transform raw achievement notes into high-impact professional summaries.

### 🛠️ Technical Stack
- **LLM Engine**: Google Gemini 2.5 Flash
- **Framework**: LangChain (langchain-google-genai)
- **Architecture**: RAG (local file retrieval + LLM synthesis)
- **Environment**: Python 3.14

### Key Features & Learning Outcomes
- **RAG Pipeline**: Successfully implemented a local retrieval system that augments LLM prompts with private data without requiring external vector databases for small-scale datasets.
- **Hyperparameter Optimization**: Mastered Temperature settings (tuned to 0.7) to achieve a precise balance between professional creativity and factual grounding.
- **Resilient Integration**: Developed a robust connection to the Google GenAI ecosystem, ensuring compatibility with the latest 2026 SDK standards.

### Outputs
- `Agent_Final_Report.txt` → Refined project summary after self-reflection.
- `Agent_LinkedIn_Post.txt` → Professional LinkedIn-style post deliverable.
- `Final_Summary.txt` → Consolidated file containing draft, refined summary, and LinkedIn post.

### Architecture
See `architecture.mmd` for a visual diagram of the agentic workflow (retrieval → reasoning → reflection → LinkedIn post → tool-calling).

### How to Run
1. Ensure `achievements.txt` and `main.py` are in the same directory.
2. Execute the script:
   ```bash
   python main.py
