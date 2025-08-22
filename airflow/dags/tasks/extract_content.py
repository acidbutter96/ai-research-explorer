from io import BytesIO
from requests import Session
from pypdf import PdfReader

from airflow.decorators import task


s = Session()


@task
def extract_content(papers: list) -> list:
    """
        Extract (simulate) full text & metadata enrichment for each paper.
        Real version would fetch PDF or use API extended fields.
    """
    enriched = []
    for p in papers:
        try:
            r = s.get(p["article_id"], timeout=10)
            reader = PdfReader(BytesIO(r.content))
        except Exception:
            continue

        full_text = []

        for page in reader.pages:
            full_text.append(page.extract_text())

        enriched.append({
            **p,
            "full_text": full_text,
        })
    return enriched
