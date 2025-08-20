from airflow.decorators import task

# Minimal placeholder embedding using simple hashing
# so we avoid heavyweight libs for now


def _fake_embed(text: str) -> list:
    import hashlib
    h = hashlib.sha256(text.encode()).hexdigest()
    # produce small vector of ints normalized
    ints = [int(h[i:i+4], 16) for i in range(0, 64, 4)]
    total = sum(ints) or 1
    return [x/total for x in ints]


@task
def generate_embeddings(papers: list) -> list:
    """Generate paragraph/section embeddings (placeholder)."""
    output = []
    for p in papers:
        sections = p.get("sections", [])
        embedded_sections = []
        for s in sections:
            embedded_sections.append({
                **s,
                "embedding": _fake_embed(s.get("text", ""))
            })
        output.append({**p, "embedded_sections": embedded_sections})
    return output


@task
def store_in_vector_db(embedded_papers: list) -> str:
    """
        Placeholder storage. Real implementation would upsert into a vector DB.
        Returns a storage reference id.
    """
    # TODO: connect to actual vector database
    # (e.g., PostgreSQL + pgvector / Chroma / Weaviate)
    count = sum(len(p.get("embedded_sections", [])) for p in embedded_papers)
    return f"stored:{len(embedded_papers)}papers:{count}sections"
