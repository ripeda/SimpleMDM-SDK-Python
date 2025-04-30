"""
devices.py: SimpleMDM Devices REST API endpoints.
"""

import requests

from enum import StrEnum

from .._connection import Connection
from .models.devices import DevicesListAllResponse, DeviceResponse, DeviceProfilesListAllResponse, InstalledAppsListAllResponse, DeviceUsersListAllResponse


class Devices(Connection):

    class OSUpdateMode(StrEnum):
        """
        Enum for OS update modes.
        """
        SMART_UPDATE = "smart_update"
        DOWNLOAD_ONLY = "download_only"
        NOTIFY_ONLY = "notify_only"
        INSTALL_ASAP = "install_asap"
        FORCE_UPDATE = "force_update"


    class OSUpdateVersionType(StrEnum):
        """
        Enum for OS update version types.
        """
        LATEST_MINOR_VERSION = "latest_minor_version"
        LATEST_MAJOR_VERSION = "latest_major_version"


    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "devices"


    def list_all(self, search: str = None, include_awaiting_enrollment: bool = None, include_secret_custom_attributes: bool = None) -> DevicesListAllResponse:
        """
        List all devices.
        """
        parameters = {}
        if search:
            parameters["search"] = search
        if include_awaiting_enrollment is not None:
            parameters["include_awaiting_enrollment"] = include_awaiting_enrollment
        if include_secret_custom_attributes is not None:
            parameters["include_secret_custom_attributes"] = include_secret_custom_attributes

        result = self._get(endpoint=self._endpoint, params=parameters)
        return DevicesListAllResponse(**result)


    def retrieve_one(self, device_id: str) -> DeviceResponse:
        """
        Retrieve one device.
        """
        result = self._get(endpoint=f"{self._endpoint}/{device_id}")
        return DeviceResponse(**result)


    def create(self, name: str, group_id: str) -> DeviceResponse:
        """
        Create a device.
        """
        parameters = {
            "name": name,
            "group_id": group_id
        }
        result = self._post(self._endpoint, parameters)
        return DeviceResponse(**result)


    def update(self, device_id: str, name: str = None, device_name: str = None) -> DeviceResponse:
        """
        Update a device.
        """
        parameters = {}
        if name:
            parameters["name"] = name
        if device_name:
            parameters["device_name"] = device_name
        result = self._patch(f"{self._endpoint}/{device_id}", parameters)
        return DeviceResponse(**result)


    def delete(self, device_id: str) -> None:
        """
        Delete a device.
        """
        self._delete(f"{self._endpoint}/{device_id}")


    def list_profiles(self, device_id: str) -> DeviceProfilesListAllResponse:
        """
        List profiles for a device.
        """
        result = self._get(f"{self._endpoint}/{device_id}/profiles")
        return DeviceProfilesListAllResponse(**result)


    def list_installed_apps(self, device_id: str) -> InstalledAppsListAllResponse:
        """
        List installed apps for a device.
        """
        result = self._get(f"{self._endpoint}/{device_id}/installed_apps")
        return InstalledAppsListAllResponse(**result)


    def list_users(self, device_id: str) -> DeviceUsersListAllResponse:
        """
        List users for a device.
        """
        try:
            result = self._get(f"{self._endpoint}/{device_id}/users")
        except Exception as e:
            # Note this API will return 422 if the device doesn't report users.
            # Return an empty list in that case.
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 422:
                response = {"data": []}
                return DeviceUsersListAllResponse(**response)
            else:
                # Raise the exception if it's not a 422 error
                raise e

        return DeviceUsersListAllResponse(**result)


    def delete_user(self, device_id: str, user_id: str) -> None:
        """
        Delete a user from a device.
        """
        self._delete(f"{self._endpoint}/{device_id}/users/{user_id}")


    def push_assigned_apps(self, device_id: str) -> None:
        """
        Push assigned apps to a device.
        """
        self._post(f"{self._endpoint}/{device_id}/push_apps")


    def refresh(self, device_id: str) -> None:
        """
        Refresh a device.
        """
        self._post(f"{self._endpoint}/{device_id}/refresh")


    def restart(self, device_id: str, rebuild_kernel_cache: bool = False, notify_users: bool = False) -> None:
        """
        Restart a device.
        """
        parameters = {}
        if rebuild_kernel_cache:
            parameters["rebuild_kernel_cache"] = rebuild_kernel_cache
        if notify_users:
            parameters["notify_users"] = notify_users
        self._post(f"{self._endpoint}/{device_id}/restart", parameters)


    def shut_down(self, device_id: str) -> None:
        """
        Shut down a device.
        """
        self._post(f"{self._endpoint}/{device_id}/shutdown")


    def lock(self, device_id: str, message: str = None, phone_number: str = None, pin: str = None) -> None:
        """
        Lock a device. Pin required for macOS devices, unsupported on iOS devices.
        """
        parameters = {}
        if message:
            parameters["message"] = message
        if phone_number:
            parameters["phone_number"] = phone_number
        if pin:
            parameters["pin"] = pin
        self._post(f"{self._endpoint}/{device_id}/lock", parameters)


    def clear_passcode(self, device_id: str) -> None:
        """
        Clear the passcode on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/clear_passcode")


    def clear_firmware_password(self, device_id: str) -> None:
        """
        Clear the firmware password on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/clear_firmware_password")


    def rotate_firmware_password(self, device_id: str) -> None:
        """
        Rotate the firmware password on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/rotate_firmware_password")


    def clear_recovery_lock_password(self, device_id: str) -> None:
        """
        Clear the recovery lock password on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/clear_recovery_lock_password")


    def clear_restrictions_password(self, device_id: str) -> None:
        """
        Clear the restrictions password on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/clear_restrictions_password")


    def rotate_recovery_lock_password(self, device_id: str) -> None:
        """
        Rotate the recovery lock password on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/rotate_recovery_lock_password")


    def rotate_filevault_recovery_key(self, device_id: str) -> None:
        """
        Rotate the FileVault recovery key on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/rotate_filevault_recovery_key")


    def set_admin_password(self, device_id: str, password: str) -> None:
        """
        Set the admin password on a device.
        """
        parameters = {
            "new_password": password
        }
        self._post(f"{self._endpoint}/{device_id}/set_admin_password", parameters)


    def rotate_admin_password(self, device_id: str) -> None:
        """
        Rotate the admin password on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/rotate_admin_password")


    def wipe(self, device_id: str, pin: str = None) -> None:
        """
        Wipe a device. 6 digit pin required for pre-T2 Macs
        """
        parameters = {}
        if pin:
            parameters["pin"] = pin
        self._post(f"{self._endpoint}/{device_id}/wipe", parameters)


    def update_os(self, device_id: str, os_update_mode: OSUpdateMode = OSUpdateMode.SMART_UPDATE, os_update_version_type: OSUpdateVersionType = OSUpdateVersionType.LATEST_MAJOR_VERSION) -> None:
        """
        Update the OS on a device.
        """
        parameters = {
            "os_update_mode": os_update_mode,
            "os_update_version_type": os_update_version_type
        }
        self._post(f"{self._endpoint}/{device_id}/update_os", parameters)


    def enable_remote_desktop(self, device_id: str) -> None:
        """
        Enable remote desktop on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/enable_remote_desktop")


    def disable_remote_desktop(self, device_id: str) -> None:
        """
        Disable remote desktop on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/disable_remote_desktop")


    def enable_bluetooth(self, device_id: str) -> None:
        """
        Enable Bluetooth on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/enable_bluetooth")


    def disable_bluetooth(self, device_id: str) -> None:
        """
        Disable Bluetooth on a device.
        """
        self._post(f"{self._endpoint}/{device_id}/disable_bluetooth")


    def set_time_zone(self, device_id: str, time_zone: str) -> None:
        """
        Set the time zone on a device.
        """
        parameters = {
            "time_zone": time_zone
        }
        self._post(f"{self._endpoint}/{device_id}/set_time_zone", parameters)


    def unenroll(self, device_id: str) -> None:
        """
        Unenroll a device.
        """
        self._post(f"{self._endpoint}/{device_id}/unenroll")