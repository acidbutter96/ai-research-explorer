from airflow.providers.http.hooks.http import HttpHook
from requests import Response


class BaseHttpService:
    def __init__(
        self,
        http_conn_id: str,
    ):
        self.http_conn_id = http_conn_id

        self.get_http_hook = HttpHook(
            http_conn_id=self.http_conn_id,
            method="GET",
        )
        self.post_http_hook = HttpHook(
            http_conn_id=self.http_conn_id,
            method="POST",
        )

    def get(
        self,
        endpoint: str,
        params: dict = None,
    ) -> Response:
        response = self.get_http_hook.run(
            endpoint=endpoint,
            data=params,
        )
        return response

    def post(
        self,
        endpoint: str,
        data: dict
    ) -> Response:
        response = self.post_http_hook.run(
            endpoint=endpoint,
            data=data,
        )
        return response
