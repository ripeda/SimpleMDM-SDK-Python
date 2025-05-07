"""
_connection.py: wrapper for requests library to handle SimpleMDM API requests.
"""

import time
import plistlib
import requests

from enum import StrEnum
from requests.auth import HTTPBasicAuth


class Connection:

    class __APIEntry(StrEnum):
        API_V1  = "api/v1"
        AUTOPKG = "munki/plugin"


    def __init__(self, api_key: str, __api_entry: __APIEntry = __APIEntry.API_V1):
        self._base         = f"https://a.simplemdm.com/{__api_entry}"
        self._session      = requests.Session()
        self._session.auth = HTTPBasicAuth(api_key, "")

        self._session.headers.update({
            "Accept":       "application/json, application/x-plist",
            "Content-Type": "application/json",
            "User-Agent":   "SimpleMDM-SDK-Python / 0.1.0"
        })


    def __epoch_to_seconds_remaining(self, epoch: int) -> int:
        """
        Convert epoch time to seconds remaining.
        """
        if epoch == 0:
            return 0
        return int(epoch - time.time())


    def __process_content_type(self, response: requests.Response) -> dict:
        """
        Process the response content type and return the appropriate data.
        """
        if response.status_code == 204:
            return {}

        # munki_pkginfo endpoint returns 202 with JSON type, but no content...
        if response.headers.get("Content-Length") == "0":
            return {}

        if "Content-Type" not in response.headers:
            raise ValueError(f"No Content-Type field found in headers: {response.headers}")

        values = response.headers["Content-Type"].split(";")
        for value in values:
            if "application/" in value:
                application_value = value
                break
        else:
            raise ValueError(f"No 'application/' Content-Type field found: {response.headers['Content-Type']}")

        if application_value == "application/json":
            return response.json()
        elif application_value == "application/x-plist":
            return plistlib.loads(response.content)
        return response.content


    def __exec(self, method: str, url: str, params: dict = None, files: dict = None) -> requests.Response:
        """
        Execute a REST API request with rate limit handling.
        """
        function = getattr(self._session, method)
        while True:
            response: requests.Response = function(url, params=params, files=files)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    # Rate limit exceeded, wait and retry
                    delay_epoch = int(response.headers.get("X-RateLimit-Reset", 1))
                    delay = self.__epoch_to_seconds_remaining(delay_epoch)
                    time.sleep(delay)
                    continue
                else:
                    raise e
            break
        return response


    def _get_raw(self, endpoint: str, params: dict = None, starting_after: str | int = 0) -> dict:
        """
        REST GET request.
        """
        url = f"{self._base}/{endpoint}"
        if starting_after != 0: # Note that logs API will return hex strings for IDs, so only compare difference instead of larger than
            url += f"?starting_after={starting_after}"

        response = self.__exec("get", url, params=params)
        return self.__process_content_type(response)


    def _get(self, endpoint: str, params: dict = None) -> dict:
        """
        REST GET request with pagination.
        """
        index = 0
        contents = {
            "data": []
        }
        while True:
            raw_data = self._get_raw(endpoint, params, index)

            # Check if data is a list or dictionary
            # If dictionary, then it is a single object
            if isinstance(raw_data.get("data"), dict):
                if "has_more" in raw_data:
                    if raw_data["has_more"] is True:
                        raise ValueError("has_more is True, but no data found")
                    del raw_data["has_more"]
                return raw_data

            contents["data"].extend(raw_data["data"])

            if "has_more" not in raw_data or raw_data["has_more"] is False:
                break

            index = raw_data["data"][-1].get("id", None)

            if index is None:
                raise ValueError("No index found in data")


        if "has_more" in contents:
            del contents["has_more"]

        return contents


    def _post(self, endpoint: str, params: dict = None, files: dict = None) -> dict:
        """
        REST POST request.
        """
        response = self.__exec("post", f"{self._base}/{endpoint}", params=params, files=files)
        return self.__process_content_type(response)


    def _put(self, endpoint: str, params: dict = None) -> dict:
        """
        REST PUT request.
        """
        response = self.__exec("put", f"{self._base}/{endpoint}", params=params)
        return self.__process_content_type(response)


    def _delete(self, endpoint: str) -> dict:
        """
        REST DELETE request.
        """
        response = self.__exec("delete", f"{self._base}/{endpoint}")
        return self.__process_content_type(response)


    def _patch(self, endpoint: str, params: dict = None, files: dict = None) -> dict:
        """
        REST PATCH request.
        """
        response = self.__exec("patch", f"{self._base}/{endpoint}", params=params, files=files)
        return self.__process_content_type(response)