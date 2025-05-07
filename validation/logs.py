"""
logs.py: Validation for SimpleMDM SDK Logs class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateLogs(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Logs class...")

        print("  Validating list_all() method...")
        all_logs = self.api.logs.list_all()
        assert all_logs is not None, "Logs list_all() method returned None"

        if len(all_logs.data) > 0:
            print("  Validating retrieve_one() method...")
            log_id = all_logs.data[0].id
            log = self.api.logs.retrieve_one(log_id)
            assert log is not None, "Logs retrieve_one() method returned None"
            assert log.data.id == log_id, f"Log ID {log.data.id} does not match the requested ID {log_id}."