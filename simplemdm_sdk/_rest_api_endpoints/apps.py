"""
apps.py: SimpleMDM Apps REST API endpoints.
"""

from enum import StrEnum

from .._connection import Connection
from .models.apps import AppResponse, AppsListAllResponse, ListInstallsResponse


class Apps(Connection):

    class DeployTo(StrEnum):
        NONE     = "none"
        OUTDATED = "outdated"
        ALL      = "all"


    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "apps"


    def list_all(self, include_shared: bool = False) -> AppsListAllResponse:
        """
        Retrieve a list of all apps.
        """
        parameters = {}

        # SimpleMDM's API is broken... If you include 'include_shared' regardless of its value,
        # it will return the same result as if you set it to True...

        if include_shared:
            parameters["include_shared"] = include_shared

        result = self._get(self._endpoint, parameters)
        return AppsListAllResponse(**result)


    def retrieve_one(self, app_id: int) -> AppResponse:
        """
        Retrieve information about a specific app.
        """
        result = self._get(f"{self._endpoint}/{app_id}")
        return AppResponse(**result)


    def create(self, app_store_id: int = None, bundle_id: str = None, binary: str = None, name: str = None) -> AppResponse:
        """
        You can use this method to add an App Store app, upload an enterprise iOS app,
        or upload macOS package to your app catalog.
        """
        parameters = {}
        files = {}

        if app_store_id:
            parameters["app_store_id"] = app_store_id
        elif bundle_id:
            parameters["bundle_id"] = bundle_id
        elif binary:
            files["binary"] = open(binary, "rb")
        else:
            raise ValueError("You must provide either an app_store_id, bundle_id or binary")

        if name:
            parameters["name"] = name

        result = self._post(self._endpoint, parameters, files)
        return AppResponse(**result)


    def update(self, app_id: int, binary: str = None, name: str = None, deploy_to: DeployTo = DeployTo.NONE) -> AppResponse:
        """
        Update an app.
        """
        parameters = {
            "deploy_to": deploy_to
        }
        if binary:
            files = {
                "binary": open(binary, "rb")
            }

        if name:
            parameters["name"] = name

        result = self._patch(f"{self._endpoint}/{app_id}", parameters, files if binary else None)
        return AppResponse(**result)


    def delete(self, app_id: int) -> None:
        """
        Delete an app.
        """
        self._delete(f"{self._endpoint}/{app_id}")


    def list_installs(self, app_id: int) -> ListInstallsResponse:
        """
        Returns a listing of the devices that an app is installed on.
        """
        results = self._get(f"{self._endpoint}/{app_id}/installs")
        return ListInstallsResponse(**results)


    def update_munki_pkginfo(self, app_id: int, file: str) -> None:
        """
        Upload a new XML or PLIST file for a Munki App.
        """
        files = {
            "file": open(file, "rb")
        }
        self._post(f"{self._endpoint}/{app_id}/munki_pkginfo", files=files)


    def delete_munki_pkginfo(self, app_id: int) -> None:
        """
        Delete Munki information.
        """
        self._delete(f"{self._endpoint}/{app_id}/munki_pkginfo")
