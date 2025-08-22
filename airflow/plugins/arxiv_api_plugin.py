from requests import Response

from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.exceptions import AirflowException

from libs.http.arxiv_api.arxiv_api import ArxivApiService


class ArxivApiOperator(BaseOperator):
    def __init__(
        self,
        action: str,
        query: str = None,
        article_id: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            **kwargs,
        )
        self.action = action
        self.query = query
        self.article_id = article_id
        self.service = ArxivApiService()

    def execute(
        self,
        context,
    ) -> Response | None:
        if self.action == "search":
            if not self.query:
                raise AirflowException("Query is required for search action.")
            return self.service.search(self.query)
        elif self.action == "get_article":
            if not self.article_id:
                raise AirflowException(
                    "Article ID is required for get_article action."
                )
            return self.service.get_article(self.article_id)
        else:
            raise AirflowException(f"Unknown action: {self.action}")


class ArxivApiPlugin(AirflowPlugin):
    name = "arxiv_api_plugin"
    operators = [ArxivApiOperator]
