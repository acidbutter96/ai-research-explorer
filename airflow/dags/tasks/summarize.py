from airflow.decorators import task


@task
def summarize_topics(papers: list) -> dict:
    """
        Produce a simplistic combined summary & keyword cloud placeholder.
    """
    titles = [p.get("title", "") for p in papers]
    keywords = {}
    for t in titles:
        for token in t.lower().split():
            if len(token) <= 3:
                continue
            keywords[token] = keywords.get(token, 0) + 1
    top_keywords = sorted(
        keywords.items(),
        key=lambda x: x[1],
        reverse=True,
    )[:10]
    summary = f"Collected {len(papers)} papers. Common terms: " + ", ".join(
        k for k, _ in top_keywords
    )
    return {"summary": summary, "keywords": top_keywords}
