# 🚀 AI Research Explorer

A system to search, summarize, and explore scientific papers using LLMs, vector search, Airflow, FastAPI, and Streamlit.

## 🌟 Overview

- Users provide keywords or upload a PDF article.
- **Airflow** orchestrates:
  - 🔍 Retrieval of relevant papers (arXiv API, Semantic Scholar API)
  - 📄 Extraction of text and metadata
  - 🧠 Generation of embeddings for each paragraph
  - 🗄️ Storage in a vector database
  - 📝 Summarization and topic extraction using LLMs
- **FastAPI** serves endpoints for:
  - 🤖 Semantic queries ("papers about federated learning in IoT")
  - 📚 Returning summaries and relevant citations
- **Streamlit** provides a UI for:
  - 📤 PDF upload or topic search
  - 📰 Displaying relevant articles with direct links
  - 💬 Chat with a "Research Assistant" powered by indexed papers
  - ☁️ Keyword cloud and topic graphs

## 🛠️ Technologies & Skills

| Technology         | Usage                                 | Skill Demonstrated           |
|-------------------|---------------------------------------|------------------------------|
| 🤖 LLM            | Summarization, embeddings, Q&A         | Applied NLP for research     |
| 🧩 Vector Search  | Semantic search in paragraphs          | Vector similarity            |
| 🕹️ Airflow        | Automated search & indexing pipeline   | Orchestration & automation   |
| ⚡ FastAPI         | Scalable backend                      | REST API + documentation     |
| 🎨 Streamlit      | Interactive front-end                  | UX with data & NLP           |
| 🌐 External APIs  | arXiv, Semantic Scholar                | Data integration             |
| 🐳 Docker          | Easy deployment                        | Basic DevOps                 |

## 🔄 Workflow

1. User enters a research topic.
2. Airflow runs the pipeline:
   - Finds papers via APIs
   - Extracts content
   - Generates embeddings
   - Stores in vector DB
3. Streamlit displays:
   - List of articles with links
   - Chat for topic questions
   - General summary of the research field
4. FastAPI enables programmatic access to all features

## 💡 Why is this project great for GitHub?

- Real-world AI application with academic value
- Combines automated pipelines with a friendly interface
- Demonstrates integration of external data + NLP + vector search
- Appeals to those interested in applied AI for scientific research
- Easily expandable to multi-language or multimodal search (text + images)

---

Made with ❤️ for the research community!

---

📝 This project is licensed under the MIT License. See the LICENSE file for details.
