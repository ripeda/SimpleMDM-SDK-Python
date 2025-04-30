"""
installed_apps.py: SimpleMDM Installed Apps REST API endpoints.
"""

from .._connection import Connection
from .models.installed_apps import InstalledAppResponse


class InstalledApps(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "installed_apps"


    def retrieve_one(self, installed_app_id: str) -> InstalledAppResponse:
        """
        Retrieve one installed app.
        """
        result = self._get(endpoint=f"{self._endpoint}/{installed_app_id}")
        return InstalledAppResponse(**result)


    def request_management_of_app(self, installed_app_id: str) -> None:
        """
        Request management of an app.
        """
        self._post(endpoint=f"{self._endpoint}/{installed_app_id}/request_management")


    def install_update(self, installed_app_id: str) -> None:
        """
        Update an app.
        """
        self._post(endpoint=f"{self._endpoint}/{installed_app_id}/update")


    def uninstall(self, installed_app_id: str) -> None:
        """
        Uninstall an app.
        """
        self._delete(endpoint=f"{self._endpoint}/{installed_app_id}")