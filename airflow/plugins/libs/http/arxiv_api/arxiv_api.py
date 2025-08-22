from libs.http.base import BaseHttpService
from requests import Response


class ArxivApiService(BaseHttpService):
    def __init__(
        self,
    ):
        super().__init__(http_conn_id="arxiv_api")

    def search(self, query: str) -> Response:
        endpoint = "/query"
        params = {"search_query": query}

        return self.get(endpoint, params=params)

    def get_article(self, article_id: str) -> Response:
        endpoint = f"/article/{article_id}"
        return self.get(endpoint)
