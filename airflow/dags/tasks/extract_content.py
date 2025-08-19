from airflow.decorators import task

@task
def extract_content(papers: list) -> list:
    """Extract (simulate) full text & metadata enrichment for each paper.
    Real version would fetch PDF or use API extended fields.
    """
    enriched = []
    for p in papers:
        enriched.append({
            **p,
            "full_text": f"Full text for {p['title']}... (placeholder)",
            "sections": [
                {"title": "Introduction", "text": f"Intro about {p['title']}"},
                {"title": "Methods", "text": "Methods placeholder."},
            ]
        })
    return enriched
