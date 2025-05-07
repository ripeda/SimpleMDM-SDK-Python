"""
devices.py: Validation for SimpleMDM SDK Devices class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateDevices(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Devices class...")

        print("  Validating list_all() method...")
        all_devices = self.api.devices.list_all()
        assert all_devices is not None, "Devices list_all() method returned None"

        if len(all_devices.data) > 0:
            print("  Validating retrieve_one() method...")
            device_id = all_devices.data[0].id
            device = self.api.devices.retrieve_one(device_id)
            assert device is not None, "Devices retrieve_one() method returned None"
            assert device.data.id == device_id, f"Device ID {device.data.id} does not match the requested ID {device_id}."

            # list_profiles() method
            print("  Validating list_profiles() method...")
            profiles = self.api.devices.list_profiles(device_id)
            assert profiles is not None, "Devices list_profiles() method returned None"

            # list_installed_apps() method
            print("  Validating list_installed_apps() method...")
            installed_apps = self.api.devices.list_installed_apps(device_id)
            assert installed_apps is not None, "Devices list_installed_apps() method returned None"

            # list_users() method
            print("  Validating list_users() method...")
            users = self.api.devices.list_users(device_id)
            assert users is not None, "Devices list_users() method returned None"


        if self.read_only:
            print("  Skipping create(), update(), delete(), etc methods in read-only mode.")
            return
        
        # TODO: Implement the rest...