"""
script_jobs.py: SimpleMDM Script Jobs REST API endpoints.
"""

from .._connection import Connection
from .models.script_jobs import ScriptJobsListAllResponse, ScriptJobResponse


class ScriptJobs(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "script_jobs"


    def list_all(self) -> ScriptJobsListAllResponse:
        """
        List all script jobs.
        """
        result = self._get(endpoint=self._endpoint)
        return ScriptJobsListAllResponse(**result)


    def retrieve_one(self, script_job_id: str) -> ScriptJobResponse:
        """
        Retrieve one script job.
        """
        result = self._get(endpoint=f"{self._endpoint}/{script_job_id}")
        return ScriptJobResponse(**result)


    def create(self, script_id: str, device_ids: list[int] = None, group_ids: list[int] = None, assignment_group_ids: list[int] = None, custom_attribute: str = None, custom_attribute_regex: str = r"\n") -> ScriptJobResponse:
        """
        Create a script job.
        """
        parameters = {
            "script_id": script_id,
        }
        if device_ids:
            parameters["device_ids"] = ",".join(map(str, device_ids))
        if group_ids:
            parameters["group_ids"] = ",".join(map(str, group_ids))
        if assignment_group_ids:
            parameters["assignment_group_ids"] = ",".join(map(str, assignment_group_ids))
        if custom_attribute:
            parameters["custom_attribute"] = custom_attribute
        if custom_attribute_regex:
            parameters["custom_attribute_regex"] = custom_attribute_regex

        result = self._post(self._endpoint, parameters)
        return ScriptJobResponse(**result)


    def cancel_job(self, script_job_id: str) -> None:
        """
        Cancel a script job.
        """
        self._delete(endpoint=f"{self._endpoint}/{script_job_id}")

