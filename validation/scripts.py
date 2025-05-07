"""
scripts.py: Validation for SimpleMDM SDK Scripts class.
"""

import tempfile
import requests
import simplemdm_sdk

from ._base import BaseValidation


class ValidateScripts(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Scripts class...")

        print("  Validating list_all() method...")
        all_scripts = self.api.scripts.list_all()
        assert all_scripts is not None, "Scripts list_all() method returned None"

        if len(all_scripts.data) > 0:
            print("  Validating retrieve_one() method...")
            script_id = all_scripts.data[0].id
            script = self.api.scripts.retrieve_one(script_id)
            assert script is not None, "Scripts retrieve_one() method returned None"
            assert script.data.id == script_id, f"Script ID {script.data.id} does not match the requested ID {script_id}."

        if self.read_only:
            print("  Skipping create(), update(), and delete() methods in read-only mode.")
            return

        print("  Validating create() method...")
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(self._script_test().encode())
            temp_file.flush()

            script = self.api.scripts.create(name="Test Script", script=temp_file.name)
            assert script is not None, "Scripts create() method returned None"
            assert script.data.attributes.name == "Test Script", f"Script name {script.data.attributes.name} does not match the expected name 'Test Script'."
            assert script.data.attributes.variable_support is False, "Script create() method did not set variable_support to False"

        print("  Validating update() method...")
        script_id = script.data.id
        script = self.api.scripts.update(script_id, variable_support=True)
        assert script is not None, "Scripts update() method returned None"
        assert script.data.attributes.variable_support is True, "Script update() method did not set variable_support to True"
        assert script.data.attributes.content == self._script_test(), "Script update() method did not retain the original script content"

        print("  Validating delete() method...")
        self.api.scripts.delete(script_id)
        try:
            self.api.scripts.retrieve_one(script_id)
            raise ValueError(f"Script ID {script_id} was not deleted successfully.")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code != 404:
                raise ValueError(f"Script ID {script_id} was not deleted successfully: {e}") from e
        print("    Script ID deleted successfully.")



    def _script_test(self) -> str:
        """
        Create a test script for validation.
        """
        return r'#!/bin/zsh --no-rcs\necho "Hello World"\n'