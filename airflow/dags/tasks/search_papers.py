# import pandas as pd

from airflow.decorators import task
from airflow.providers.http.operators.http import HttpOperator

# Placeholder search functions. In a real implementation you'd call arXiv
# and Semantic Scholar APIs.
# Keeping external calls minimal until dependencies & networking
# are configured.

get_arxiv_papers = HttpOperator(
    task_id='search_arxiv',
    endpoint='http://export.arxiv.org/api/query',
    method='GET',
    data={
        "search_query": query,
        "start": 0
    },
    log_response=True,
)


@task
def search_arxiv(query: str) -> list:
    """
        Search arXiv for papers matching query.
        Returns list of minimal metadata dicts.
    """
    # TODO: implement real API call

    return [
        {
            "source": "arxiv",
            "id": "arxiv:1234",
            "title": f"Sample arXiv paper about {query}",
            "authors": ["Doe"],
            "abstract": "Abstract text."
        }
    ]


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
