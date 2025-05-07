"""
lost_mode.py: Validation for SimpleMDM SDK Lost Mode class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateLostMode(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        if self.read_only:
            print("  Skipping Lost Mode validation in read-only mode.")
            return

        print("Validating Lost Mode class...")

        print("  Validating enable() method...")
        device = self.api.devices.list_all().data[0]
        device_id = device.id
        self.api.lost_mode.enable(device_id)

        print("  Validating disable() method...")
        self.api.lost_mode.disable(device_id)

        print("  Validating play_a_sound() method...")
        self.api.lost_mode.play_a_sound(device_id)

        print("  Validating update_location() method...")
        self.api.lost_mode.update_location(device_id)

