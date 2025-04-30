"""
scripts.py: SimpleMDM Scripts REST API endpoints.
"""

from .._connection import Connection
from .models.scripts import ScriptsListAllResponse, ScriptResponse


class Scripts(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "scripts"


    def list_all(self) -> ScriptsListAllResponse:
        """
        List all scripts.
        """
        result = self._get(endpoint=self._endpoint)
        return ScriptsListAllResponse(**result)


    def retrieve_one(self, script_id: str) -> ScriptResponse:
        """
        Retrieve one script.
        """
        result = self._get(endpoint=f"{self._endpoint}/{script_id}")
        return ScriptResponse(**result)


    def create(self, name: str, script: str, variable_support: bool = None) -> ScriptResponse:
        """
        Create a script.
        """
        files = {
            "file": open(script, "rb")
        }
        parameters = {
            "name": name,
        }
        if variable_support is not None:
            parameters["variable_support"] = 1 if variable_support else 0

        result = self._post(self._endpoint, parameters, files)
        return ScriptResponse(**result)


    def update(self, script_id: str, name: str = None, script: str = None, variable_support: bool = None) -> ScriptResponse:
        """
        Update a script.
        """
        files = {}
        parameters = {}

        if script is not None:
            files["file"] = open(script, "rb")

        if name is not None:
            parameters["name"] = name

        if variable_support is not None:
            parameters["variable_support"] = 1 if variable_support else 0

        result = self._patch(f"{self._endpoint}/{script_id}", parameters, files)
        return ScriptResponse(**result)


    def delete(self, script_id: str) -> None:
        """
        Delete a script.
        """
        self._delete(f"{self._endpoint}/{script_id}")