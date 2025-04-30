"""
device_groups.py: SimpleMDM Device Groups REST API endpoints.
"""

from .._connection import Connection
from .models.device_groups import DeviceGroupsListAllResponse, DeviceGroupResponse


class DeviceGroups(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "device_groups"


    def list_all(self) -> DeviceGroupsListAllResponse:
        """
        List all device groups.
        """
        result = self._get(endpoint=self._endpoint)
        return DeviceGroupsListAllResponse(**result)


    def retrieve_one(self, device_group_id: str) -> DeviceGroupResponse:
        """
        Retrieve one device group.
        """
        result = self._get(endpoint=f"{self._endpoint}/{device_group_id}")
        return DeviceGroupResponse(**result)


    def assign_device(self, device_group_id: str, device_id: str) -> None:
        """
        Assign a device to a device group.
        """
        self._post(endpoint=f"{self._endpoint}/{device_group_id}/devices/{device_id}")


    def clone(self, device_group_id: str) -> DeviceGroupResponse:
        """
        Clone a device group.
        """
        result = self._post(endpoint=f"{self._endpoint}/{device_group_id}/clone")
        return DeviceGroupResponse(**result)
