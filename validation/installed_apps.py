"""
installed_apps.py: Validation for SimpleMDM SDK Installed Apps class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateInstalledApps(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Installed Apps class...")

        device = self.api.devices.list_all().data[0]
        device_id = device.id
        apps = self.api.devices.list_installed_apps(device_id)
        app_id = apps.data[0].id

        print("  Validating retrieve_one() method...")
        installed_app = self.api.installed_apps.retrieve_one(app_id)
        assert installed_app is not None, "Installed Apps retrieve_one() method returned None"
        assert installed_app.data.id == app_id, f"Installed App ID {installed_app.data.id} does not match the requested ID {app_id}."

        if self.read_only:
            print("  Skipping request_management_of_app(), install_update() and uninstall() methods in read-only mode.")
            return
        
        # TODO: Implement request_management_of_app() method validation