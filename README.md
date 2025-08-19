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

## 🪂 Airflow DAGs

| DAG ID | Purpose |
|--------|---------|
| `example_hello_world` | Minimal example printing a greeting |
| `integral_calculator` | Placeholder showing a simple task pattern |
| `research_pipeline` | Core paper search → enrich → embed → store → summarize workflow |

### research_pipeline overview

Current placeholder stages (will be replaced with real logic):

1. Search (mock) arXiv & Semantic Scholar with a default query (`federated learning`).
2. Merge & deduplicate results.
3. Simulate content extraction (adds sections & dummy full text).
4. Generate simple deterministic hash embeddings.
5. Simulate vector DB storage (returns a reference string via XCom).
6. Produce a naive keyword frequency summary.

Modify or extend any stage under `airflow/dags/tasks/`.

### Run locally (Docker / Airflow)

```bash
docker compose up -d --build
# open http://localhost:8080 and trigger `research_pipeline`
```

### Next implementation steps

- Replace search placeholders with real API calls (`requests` already added; handle rate limiting & pagination).
- Add PDF download + parsing (e.g., `pypdf`).
- Swap hash embed with real embedding model (OpenAI, HuggingFace, Instructor). Batch for efficiency.
- Integrate a vector DB (Postgres + pgvector, Chroma, Weaviate) em docker-compose & implementar upsert.
- Expose semantic query API via FastAPI usando vetores armazenados.
- Conectar Streamlit para disparar novas indexações (Airflow REST API) & chat.

---

📝 This project is licensed under the MIT License. See the LICENSE file for details.

## 🧩 Git Commit Conventions

All commit messages should be in English and follow a Conventional Commits style (e.g. `feat: add semantic search endpoint`).

To enable the included commit template and hook:

```bash
git config commit.template .gitmessage
chmod +x scripts/prepare-commit-msg
ln -s ../../scripts/prepare-commit-msg .git/hooks/prepare-commit-msg 2>/dev/null || cp scripts/prepare-commit-msg .git/hooks/prepare-commit-msg
```

Template types:
`feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
