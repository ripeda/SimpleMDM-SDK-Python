"""
assignment_groups.py: Validation for SimpleMDM SDK Assignment Groups class.
"""

import requests
import simplemdm_sdk

from ._base import BaseValidation


class ValidateAssignmentGroups(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Assignment Groups class...")

        print("  Validating list_all() method...")
        all_groups = self.api.assignment_groups.list_all()
        assert all_groups is not None, "Assignment Groups list_all() method returned None"
        assert len(all_groups.data) > 0, "Assignment Groups list_all() method returned an empty list"

        print("  Validating retrieve_one() method...")
        group_id = all_groups.data[0].id
        group = self.api.assignment_groups.retrieve_one(group_id)
        assert group is not None, "Assignment Groups retrieve_one() method returned None"
        assert group.data.id == group_id, f"Assignment Group ID {group.data.id} does not match the requested ID {group_id}."

        if self.read_only:
            print("  Skipping create(), update(), and delete() methods in read-only mode.")
            return

        print("  Validating create() method...")
        group_name = "SimpleMDM SDK Test Group"
        group = self.api.assignment_groups.create(name=group_name)
        assert group is not None, "Assignment Groups create() method returned None"
        assert group.data.attributes.name == group_name, f"Assignment Group name {group.data.attributes.name} does not match the requested name {group_name}."

        # In the new Groups Beta (as of 2025/05/01), the support mixed types thus ignore the type and install_type
        if group.data.attributes.type is not None:
            assert group.data.attributes.type == "standard", f"Assignment Group type {group.data.attributes.type} is not 'standard'."
        if group.data.attributes.install_type is not None:
            assert group.data.attributes.install_type == "managed", f"Assignment Group install type {group.data.attributes.install_type} is not 'managed'."

        print("    data.attributes.name: ", group.data.attributes.name)
        print("    data.attributes.type: ", group.data.attributes.type)

        print("  Validating update() method...")
        self.api.assignment_groups.update(group.data.id, name="SimpleMDM SDK Updated Group")
        updated_group = self.api.assignment_groups.retrieve_one(group.data.id)
        assert updated_group is not None, "Assignment Groups update() method returned None"
        assert updated_group.data.attributes.name == "SimpleMDM SDK Updated Group", "Assignment Groups update() method did not update name"

        print("    data.attributes.name: ", updated_group.data.attributes.name)

        print("  Validating delete() method...")
        self.api.assignment_groups.delete(group.data.id)
        try:
            self.api.assignment_groups.retrieve_one(group.data.id)
            raise AssertionError("Assignment group was not deleted.")
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404, f"Assignment group was not deleted: {e.response.status_code}"

        # TODO: Implement the rest of the methods
        # - assign_app()
        # - unassign_app()
        # - assign_device_group()
        # - unassign_device_group()
        # - assign_device()
        # - unassign_device()
        # - push_apps()
        # - update_apps()
        # - assign_profile()
        # - unassign_profile()
        # - sync_profiles()
        # - clone()

