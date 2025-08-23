from airflow.decorators import task
from airflow.providers.openai.operators.openai import OpenAIEmbeddingOperator

# Minimal placeholder embedding using simple hashing
# Mantido para futuros usos locais sem API externa
# (não utilizado para summaries).


def _fake_embed(text: str) -> list:
    import hashlib
    h = hashlib.sha256(text.encode()).hexdigest()
    # produce small vector of ints normalized
    ints = [int(h[i:i+4], 16) for i in range(0, 64, 4)]
    total = sum(ints) or 1
    return [x / total for x in ints]


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
                "embedding": _fake_embed(s.get("text", "")),
            })
        output.append({**p, "embedded_sections": embedded_sections})
    return output


def _summaries_callable(upstream_task_id: str):
    """Build a callable that extracts summaries from XCom of given task_id."""

    def _inner_callable(**context):
        ti = context["ti"]
        papers = ti.xcom_pull(task_ids=upstream_task_id) or []

        return [
            (p.get("summary") or "N/A").strip()
            for p in papers
        ]

    return _inner_callable


def _resolve_task_id(upstream) -> str:
    """Resolve um task_id a partir de XComArg/BaseOperator/str."""
    op = getattr(upstream, "operator", None)
    if op is not None and getattr(op, "task_id", None):
        return op.task_id
    if getattr(upstream, "task_id", None):
        return upstream.task_id
    if isinstance(upstream, str):
        return upstream
    raise ValueError(
        "upstream deve ser XComArg, BaseOperator ou str de task_id"
    )


def create_openai_summary_embedding_task(
    upstream=None,
    input_text=None,
    *,
    task_id: str = "embed_summaries",
    conn_id: str = "openai_default",
    model: str = "text-embedding-3-small",
):
    """
    Factory que cria um OpenAIEmbeddingOperator
    para embutir p['summary'] de 'papers' do task_id informado.

    Retorna a instância do Operator; use .output para obter
    os vetores via XCom.
    """
    if input_text is not None:
        return OpenAIEmbeddingOperator(
            task_id=task_id,
            conn_id=conn_id,
            input_text=input_text,
            model=model,
        )

    upstream_task_id = _resolve_task_id(upstream)
    return OpenAIEmbeddingOperator(
        task_id=task_id,
        conn_id=conn_id,
        input_text=_summaries_callable(upstream_task_id),
        model=model,
    )


@task
def extract_summaries(papers: list) -> list:
    """Extrai lista de summaries de uma lista de papers.

    Mantém a ordem para alinhamento índice-a-índice com outras listas
    derivadas do mesmo insumo.
    """
    return [
        (p.get("summary") or "N/A").strip()
        for p in (papers or [])
    ]


@task
def attach_summary_embeddings(papers: list, summary_embeddings: list) -> list:
    """Anexa os embeddings dos summaries de volta aos papers (por índice)."""
    attached = []
    for idx, p in enumerate(papers or []):
        emb = None
        if (
            isinstance(summary_embeddings, list)
            and idx < len(summary_embeddings)
        ):
            emb = summary_embeddings[idx]
        attached.append({**p, "summary_embedding": emb})
    return attached


@task
def store_in_vector_db(papers: list) -> str:
    """
    Placeholder storage. Real implementation would upsert into a vector DB.
    Returns a storage reference id.
    """
    # TODO: connect to actual vector database
    # (e.g., PostgreSQL + pgvector / Chroma / Weaviate)
    count_sections = sum(
        len(p.get("embedded_sections", [])) for p in papers or []
    )
    count_summaries = sum(
        1 for p in papers or [] if p.get("summary_embedding") is not None
    )
    return (
        f"stored:{len(papers)}papers:"
        f"{count_sections}sections:{count_summaries}summaries"
    )
