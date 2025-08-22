from datetime import datetime
from airflow.decorators import dag

from tasks.search_papers import (
    search_arxiv,
    merge_and_deduplicate,
)
from tasks.extract_content import extract_content
from tasks.embed_and_store import generate_embeddings, store_in_vector_db
from tasks.summarize import summarize_topics


@dag(
    dag_id="research_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["research", "nlp", "vector"],
    max_active_runs=1,
)
def research_pipeline():
    """Core AI Research Explorer pipeline.

    Steps:
    1. Search external APIs (arXiv & Semantic Scholar).
    2. Merge & deduplicate results.
    3. Extract / enrich content (placeholder).
    4. Generate embeddings (placeholder).
    5. Store vectors (placeholder storage).
    6. Summarize & extract simple topic keywords.
    """

    query = "federated learning"

    arxiv_results = search_arxiv(query)
    merged = merge_and_deduplicate(
        arxiv_results=arxiv_results,
        ss_results=[],
    )
    enriched = extract_content(merged)
    embedded = generate_embeddings(enriched)
    storage_ref = store_in_vector_db(embedded)
    summary = summarize_topics(merged)

    (
        arxiv_results >> merged >> enriched >>
        embedded >> storage_ref >> summary
    )


research_pipeline()
