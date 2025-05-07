"""
dep_servers.py: Validation for SimpleMDM SDK DEP Servers class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateDEPServers(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating DEP Servers class...")

        print("  Validating list_all() method...")
        all_dep_servers = self.api.dep_servers.list_all()
        assert all_dep_servers is not None, "DEP Servers list_all() method returned None"

        if len(all_dep_servers.data) > 0:
            print("  Validating retrieve_one() method...")
            dep_server_id = all_dep_servers.data[0].id
            dep_server = self.api.dep_servers.retrieve_one(dep_server_id)
            assert dep_server is not None, "DEP Servers retrieve_one() method returned None"
            assert dep_server.data.id == dep_server_id, f"DEP Server ID {dep_server.data.id} does not match the requested ID {dep_server_id}."

            print("  Validating list_dep_devices() method...")
            dep_devices = self.api.dep_servers.list_dep_devices(dep_server_id)
            assert dep_devices is not None, "DEP Servers list_dep_devices() method returned None"

            if len(dep_devices.data) > 0:
                print("  Validating retrieve_one_dep_device() method...")
                dep_device_id = dep_devices.data[0].id
                dep_device = self.api.dep_servers.retrieve_one_dep_device(dep_server_id, dep_device_id)
                assert dep_device is not None, "DEP Servers retrieve_one_dep_device() method returned None"
                assert dep_device.data.id == dep_device_id, f"DEP Device ID {dep_device.data.id} does not match the requested ID {dep_device_id}."

        if self.read_only:
            print("  Skipping sync_with_apple()")
            return

        print("  Validating sync_with_apple() method...")
        dep_server_id = all_dep_servers.data[0].id
        self.api.dep_servers.sync_with_apple(dep_server_id)