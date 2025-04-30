"""
dep_servers.py: SimpleMDM DEP Servers REST API endpoints.
"""

from .._connection import Connection
from .models.dep_servers import DepServersListAllResponse, DepServerResponse, DepServerDevicesListAllResponse, DepServerDeviceResponse


class DEPServers(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "dep_servers"


    def list_all(self) -> DepServersListAllResponse:
        """
        List all DEP servers.
        """
        result = self._get(endpoint=self._endpoint)
        return DepServersListAllResponse(**result)


    def retrieve_one(self, dep_server_id: str) -> DepServerResponse:
        """
        Retrieve one DEP server.
        """
        result = self._get(endpoint=f"{self._endpoint}/{dep_server_id}")
        return DepServerResponse(**result)


    def sync_with_apple(self, dep_server_id: str) -> None:
        """
        Sync with Apple DEP.
        """
        self._post(endpoint=f"{self._endpoint}/{dep_server_id}/sync")


    def list_dep_devices(self, dep_server_id: str) -> DepServerDevicesListAllResponse:
        """
        List DEP devices.
        """
        result = self._get(endpoint=f"{self._endpoint}/{dep_server_id}/dep_devices")
        return DepServerDevicesListAllResponse(**result)


    def retrieve_one_dep_device(self, dep_server_id: str, dep_device_id: str) -> DepServerDeviceResponse:
        """
        Retrieve one DEP device.
        """
        result = self._get(endpoint=f"{self._endpoint}/{dep_server_id}/dep_devices/{dep_device_id}")
        return DepServerDeviceResponse(**result)


