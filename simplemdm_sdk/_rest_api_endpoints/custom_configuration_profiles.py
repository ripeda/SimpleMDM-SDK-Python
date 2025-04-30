"""
custom_configuration_profiles.py: SimpleMDM Custom Configuration Profiles REST API endpoints.
"""

from .._connection import Connection
from .models.custom_configuration_profiles import CustomConfigurationProfilesListAllResponse, CustomConfigurationProfileResponse


class CustomConfigurationProfiles(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "custom_configuration_profiles"


    def list_all(self) -> CustomConfigurationProfilesListAllResponse:
        """
        List all custom configuration profiles.
        """
        result = self._get(self._endpoint)
        return CustomConfigurationProfilesListAllResponse(**result)


    def create(self, name: str, mobileconfig: str, user_scope: bool = False, attribute_support: bool = False, escape_attributes: bool = False, reinstall_after_os_update: bool = False) -> CustomConfigurationProfileResponse:
        """
        Create a custom configuration profile.
        """
        parameters = {
            "name": name,
        }

        files = {
            "mobileconfig": open(mobileconfig, "rb")
        }

        if user_scope is True:
            parameters["user_scope"] = user_scope
        if attribute_support is True:
            parameters["attribute_support"] = attribute_support
        if escape_attributes is True:
            parameters["escape_attributes"] = escape_attributes
        if reinstall_after_os_update is True:
            parameters["reinstall_after_os_update"] = reinstall_after_os_update

        result = self._post(self._endpoint, parameters, files)
        return CustomConfigurationProfileResponse(**result)


    def update(self, profile_id: int, name: str = None, mobileconfig: str = None, user_scope: bool = None, attribute_support: bool = None, escape_attributes: bool = None, reinstall_after_os_update: bool = None) -> CustomConfigurationProfileResponse:
        """
        Update a custom configuration profile.
        """
        parameters = {}
        files = {}

        if name:
            parameters["name"] = name
        if user_scope is not None:
            parameters["user_scope"] = user_scope
        if attribute_support is not None:
            parameters["attribute_support"] = attribute_support
        if escape_attributes is not None:
            parameters["escape_attributes"] = escape_attributes
        if reinstall_after_os_update is not None:
            parameters["reinstall_after_os_update"] = reinstall_after_os_update

        if mobileconfig:
            files["mobileconfig"] = open(mobileconfig, "rb")

        if not parameters and not files:
            raise ValueError("No parameters or files provided for update")

        result = self._patch(f"{self._endpoint}/{profile_id}", parameters, files=files if files else None)
        return CustomConfigurationProfileResponse(**result)


    def download(self, profile_id: int) -> bytes:
        """
        Download a custom configuration profile.
        """
        result = self._get_raw(f"{self._endpoint}/{profile_id}/download")
        return result


    def delete(self, profile_id: int) -> None:
        """
        Delete a custom configuration profile.
        """
        self._delete(f"{self._endpoint}/{profile_id}")


    def assign_to_device_group(self, profile_id: int, device_group_id: int) -> None:
        """
        Assign a custom configuration profile to a device group.
        """
        self._post(f"{self._endpoint}/{profile_id}/device_groups/{device_group_id}")


    def unassign_from_device_group(self, profile_id: int, device_group_id: int) -> None:
        """
        Unassign a custom configuration profile from a device group.
        """
        self._delete(f"{self._endpoint}/{profile_id}/device_groups/{device_group_id}")


    def assign_to_device(self, profile_id: int, device_id: int) -> None:
        """
        Assign a custom configuration profile to a device.
        """
        self._post(f"{self._endpoint}/{profile_id}/devices/{device_id}")


    def unassign_from_device(self, profile_id: int, device_id: int) -> None:
        """
        Unassign a custom configuration profile from a device.
        """
        self._delete(f"{self._endpoint}/{profile_id}/devices/{device_id}")