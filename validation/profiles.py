"""
profiles.py: Validation for SimpleMDM SDK Profiles class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateProfiles(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Profiles class...")

        print("  Validating list_all() method...")
        all_profiles = self.api.profiles.list_all()
        assert all_profiles is not None, "Profiles list_all() method returned None"

        if len(all_profiles.data) > 0:
            print("  Validating retrieve_one() method...")
            profile_id = all_profiles.data[0].id
            profile = self.api.profiles.retrieve_one(profile_id)
            assert profile is not None, "Profiles retrieve_one() method returned None"
            assert profile.data.id == profile_id, f"Profile ID {profile.data.id} does not match the requested ID {profile_id}."

        if self.read_only:
            print("  Skipping assign_to_device_group(), unassign_from_device_group(), assign_to_device(), and unassign_from_device() methods in read-only mode.")
            return

        # TODO: Implement the rest...