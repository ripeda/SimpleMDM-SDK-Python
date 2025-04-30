"""
assignment_groups.py: SimpleMDM Assignment Groups REST API endpoints.
"""

from enum import StrEnum

from .._connection import Connection
from .models.assignment_groups import ListAssignmentGroupsResponse, AssignmentGroupsResponse


class AssignmentGroups(Connection):

    class GroupType(StrEnum):
        """
        Types of assignment groups
        """
        STANDARD = "standard"
        MUNKI    = "munki"


    class MunkiInstallType(StrEnum):
        """
        Types of install types
        """
        MANAGED          = "managed"
        SELF_SERVE       = "self_serve"
        DEFAULT_INSTALLS = "default_installs"
        MANAGED_UPDATES  = "managed_updates"


    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "assignment_groups"


    def list_all(self) -> ListAssignmentGroupsResponse:
        """
        List all assignment groups
        """
        result = self._get(self._endpoint)
        return ListAssignmentGroupsResponse(**result)


    def retrieve_one(self, assignment_group_id: int) -> AssignmentGroupsResponse:
        """
        Retrieve one assignment group
        """
        result = self._get(f"{self._endpoint}/{assignment_group_id}")
        return AssignmentGroupsResponse(**result)


    def create(self, name: str, priority: int = None, auto_deploy: bool = True, type: GroupType = GroupType.STANDARD, install_type: MunkiInstallType = MunkiInstallType.MANAGED, app_track_location: bool = True) -> AssignmentGroupsResponse:
        """
        Create an assignment group
        """
        parameters = {
            "name": name,
            "auto_deploy": auto_deploy,
            "type": type.value,
            "install_type": install_type.value,
            "app_track_location": app_track_location
        }
        if priority:
            parameters["priority"] = priority
        result = self._post(self._endpoint, parameters)
        return AssignmentGroupsResponse(**result)


    def update(self, group_id: int, name: str, priority: int = None, auto_deploy: bool = True) -> None:
        """
        Update an assignment group
        """
        parameters = {
            "name": name,
            "auto_deploy": auto_deploy
        }
        if priority:
            parameters["priority"] = priority
        self._patch(f"{self._endpoint}/{group_id}", parameters)


    def delete(self, group_id: int) -> None:
        """
        Delete an assignment group
        """
        self._delete(f"{self._endpoint}/{group_id}")


    def assign_app(self, group_id: int, app_id: int) -> None:
        """
        Assign an app to an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/apps/{app_id}")


    def unassign_app(self, group_id: int, app_id: int) -> None:
        """
        Unassign an app from an assignment group
        """
        self._delete(f"{self._endpoint}/{group_id}/apps/{app_id}")


    def assign_device_group(self, group_id: int, device_group_id: int) -> None:
        """
        Assign a device group to an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/device_groups/{device_group_id}")


    def unassign_device_group(self, group_id: int, device_group_id: int) -> None:
        """
        Unassign a device group from an assignment group
        """
        self._delete(f"{self._endpoint}/{group_id}/device_groups/{device_group_id}")


    def assign_device(self, group_id: int, device_id: int) -> None:
        """
        Assign a device to an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/devices/{device_id}")


    def unassign_device(self, group_id: int, device_id: int) -> None:
        """
        Unassign a device from an assignment group
        """
        self._delete(f"{self._endpoint}/{group_id}/devices/{device_id}")


    def push_apps(self, group_id: int) -> None:
        """
        Push apps to devices in an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/push_apps")


    def update_apps(self, group_id: int) -> None:
        """
        Update apps on devices in an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/update_apps")


    def assign_profile(self, group_id: int, profile_id: int) -> None:
        """
        Assign a profile to an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/profiles/{profile_id}")


    def unassign_profile(self, group_id: int, profile_id: int) -> None:
        """
        Unassign a profile from an assignment group
        """
        self._delete(f"{self._endpoint}/{group_id}/profiles/{profile_id}")


    def sync_profiles(self, group_id: int) -> None:
        """
        Sync profiles to devices in an assignment group

        TODO: Implement proper rate limiting
        """
        self._post(f"{self._endpoint}/{group_id}/sync_profiles")


    def clone(self, group_id: int) -> None:
        """
        Clone an assignment group
        """
        self._post(f"{self._endpoint}/{group_id}/clone")
