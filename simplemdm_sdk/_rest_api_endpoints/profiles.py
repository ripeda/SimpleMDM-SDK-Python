"""
profiles.py: SimpleMDM Profiles REST API endpoints.
"""

from .._connection import Connection
from .models.profiles import ListProfilesResponse, ProfilesResponse


class Profiles(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "profiles"


    def list_all(self) -> ListProfilesResponse:
        """
        List all profiles.
        """
        result = self._get(endpoint=self._endpoint)
        return ListProfilesResponse(**result)


    def retrieve_one(self, profile_id: str) -> ProfilesResponse:
        """
        Retrieve one profile.
        """
        result = self._get(endpoint=f"{self._endpoint}/{profile_id}")
        return ProfilesResponse(**result)


    def assign_to_device_group(self, profile_id: str, device_group_id: str) -> None:
        """
        Assign a profile to a device group.
        """
        self._post(endpoint=f"{self._endpoint}/{profile_id}/device_groups/{device_group_id}")


    def unassign_from_device_group(self, profile_id: str, device_group_id: str) -> None:
        """
        Unassign a profile from a device group.
        """
        self._delete(endpoint=f"{self._endpoint}/{profile_id}/device_groups/{device_group_id}")


    def assign_to_device(self, profile_id: str, device_id: str) -> None:
        """
        Assign a profile to a device.
        """
        self._post(endpoint=f"{self._endpoint}/{profile_id}/devices/{device_id}")


    def unassign_from_device(self, profile_id: str, device_id: str) -> None:
        """
        Unassign a profile from a device.
        """
        self._delete(endpoint=f"{self._endpoint}/{profile_id}/devices/{device_id}")