"""
devices.py: Validation for SimpleMDM SDK Enrollments class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateEnrollments(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Enrollments class...")

        print("  Validating list_all() method...")
        all_enrollments = self.api.enrollments.list_all()
        assert all_enrollments is not None, "Enrollments list_all() method returned None"

        if len(all_enrollments.data) > 0:
            print("  Validating retrieve_one() method...")
            enrollment_id = all_enrollments.data[0].id
            enrollment = self.api.enrollments.retrieve_one(enrollment_id)
            assert enrollment is not None, "Enrollments retrieve_one() method returned None"
            assert enrollment.data.id == enrollment_id, f"Enrollment ID {enrollment.data.id} does not match the requested ID {enrollment_id}."

        if self.read_only:
            print("  Skipping send_invitation() and delete() methods in read-only mode.")
            return

        if len(all_enrollments.data) > 0:
            print("  Validating send_invitation() method...")
            enrollment_id = all_enrollments.data[0].id
            enrollment = self.api.enrollments.send_invitation(enrollment_id, "null")

        # TODO: Implement delete() method validation