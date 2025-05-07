"""
script_jobs.py: Validation for SimpleMDM SDK Script Jobs class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateScriptJobs(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Script Jobs class...")

        print("  Validating list_all() method...")
        all_script_jobs = self.api.script_jobs.list_all()
        assert all_script_jobs is not None, "Script Jobs list_all() method returned None"

        if len(all_script_jobs.data) > 0:
            print("  Validating retrieve_one() method...")
            script_job_id = all_script_jobs.data[0].id
            script_job = self.api.script_jobs.retrieve_one(script_job_id)
            assert script_job is not None, "Script Jobs retrieve_one() method returned None"
            assert script_job.data.id == script_job_id, f"Script Job ID {script_job.data.id} does not match the requested ID {script_job_id}."

        if self.read_only:
            print("  Skipping create() and cancel_job() methods in read-only mode.")
            return

        print("  Validating create() method...")
        scripts = self.api.scripts.list_all()
        if len(scripts.data) > 0:
            script_id = scripts.data[0].id
            device_id = self.api.devices.list_all().data[0].id
            script_job = self.api.script_jobs.create(script_id, [device_id])
            assert script_job is not None, "Script Jobs create() method returned None"

            print("  Validating cancel_job() method...")
            script_job_id = script_job.data.id
            self.api.script_jobs.cancel_job(script_job_id)
            script = self.api.script_jobs.retrieve_one(script_job_id)
            assert script.data.attributes.status == "cancelled", f"Script Job ID {script.data.id} was not cancelled successfully: {script.data.attributes.status}"
