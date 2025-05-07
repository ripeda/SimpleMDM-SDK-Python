"""
device_groups.py: Validation for SimpleMDM SDK Device Groups class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateDeviceGroups(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Device Groups class...")

        print("  Validating list_all() method...")
        all_device_groups = self.api.device_groups.list_all()
        assert all_device_groups is not None, "Device Groups list_all() method returned None"

        if len(all_device_groups.data) > 0:
            print("  Validating retrieve_one() method...")
            device_group_id = all_device_groups.data[0].id
            device_group = self.api.device_groups.retrieve_one(device_group_id)
            assert device_group is not None, "Device Groups retrieve_one() method returned None"
            assert device_group.data.id == device_group_id, f"Device Group ID {device_group.data.id} does not match the requested ID {device_group_id}."


        if self.read_only:
            print("  Skipping create(), update(), and delete() methods in read-only mode.")
            return

        # TODO: Add validation for assign_device() and clone() methods