import sys
import os
import pandas as pd

from xmltodict import parse as xml_parse

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../')
    )
)


from airflow.decorators import task # noqa
from plugins.arxiv_api_plugin import ArxivApiOperator # noqa


# Placeholder search functions. In a real implementation you'd call arXiv
# and Semantic Scholar APIs.
# Keeping external calls minimal until dependencies & networking
# are configured.


@task
def search_arxiv(query: str) -> list:
    """
        Busca artigos no arXiv usando o ArxivApiOperator do plugin.
        Retorna lista de metadados mínimos dos artigos.
    """
    operator = ArxivApiOperator(
        action="search",
        task_id="search_arxiv",
        query="dirac equation",
    )
    results = operator.execute(context={})
    xml_dict = xml_parse(results.text)

    entries = xml_dict["feed"]["entry"]
    if not isinstance(entries, list):
        entries = [entries]

    rows = []
    for entry in entries:
        article_id = entry["id"]
        title = entry["title"]
        summary = entry["summary"]
        published = entry["published"]
        authors = entry["author"]
        if not isinstance(authors, list):
            authors = [authors]
        rows.append({
            "source": "arxiv",
            "article_id": article_id,
            "authors": [
                author["name"]
                for author in authors
            ],
            "title": title,
            "summary": summary,
            "published": published
        })

    return rows


@task
def search_semantic_scholar(query: str) -> list:
    """
        Search Semantic Scholar for papers.
        Returns list of minimal metadata dicts.
    """
    # TODO: implement real API call
    return [
        {
            "source": "semanticscholar",
            "id": "ss:5678",
            "title": f"Sample Semantic Scholar paper about {query}",
            "authors": ["Smith"],
            "abstract": "Another abstract.",
        }
    ]


@task
def merge_and_deduplicate(arxiv_results: list, ss_results: list) -> list:
    """
        Merge results lists and deduplicate by (source,id) now;
        later maybe by title DOI.
    """
    seen = set()
    merged = []
    for collection in (arxiv_results or [], ss_results or []):
        for item in collection:
            key = (item.get("source"), item.get("id"))
            if key in seen:
                continue
            seen.add(key)
            merged.append(item)
    return merged
