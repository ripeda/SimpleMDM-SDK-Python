"""
logs.py: SimpleMDM Logs REST API endpoints.
"""

from .._connection import Connection
from .models.logs import LogsListAllResponse, LogResponse


class Logs(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "logs"


    def list_all(self) -> LogsListAllResponse:
        """
        List all logs.
        """
        result = self._get(endpoint=self._endpoint)
        return LogsListAllResponse(**result)


    def retrieve_one(self, log_id: str) -> LogResponse:
        """
        Retrieve one log.
        """
        result = self._get(endpoint=f"{self._endpoint}/{log_id}")
        return LogResponse(**result)