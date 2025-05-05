"""
managed_app_configs.py: SimpleMDM Managed App Configs REST API endpoints.
"""

from enum import StrEnum

from .._connection import Connection
from .models.managed_app_configs import ManagedAppConfigResponse, ManagedAppConfigListResponse


class ManagedAppConfigs(Connection):

    class ValueType(StrEnum):
        BOOLEAN       = "boolean"
        DATE          = "date"
        FLOAT         = "float"
        FLOAT_ARRAY   = "float array"
        INTEGER       = "integer"
        INTEGER_ARRAY = "integer array"
        STRING        = "string"
        STRING_ARRAY  = "string array"


    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "apps"


    def get(self, managed_app_config_id: int) -> ManagedAppConfigListResponse:
        """
        Retrieve a managed app config.
        """
        result = self._get(endpoint=f"{self._endpoint}/{managed_app_config_id}/managed_configs")
        return ManagedAppConfigListResponse(**result)


    def create(self, app_id: int, key: str, value: str = None, value_type: ValueType = None) -> ManagedAppConfigResponse:
        """
        Create a managed app config.
        """
        parameters = {
            "key": key,
        }
        if value is not None:
            parameters["value"] = value
        if value_type is not None:
            parameters["value_type"] = value_type.value

        result = self._post(endpoint=f"{self._endpoint}/{app_id}/managed_configs", params=parameters)
        return ManagedAppConfigResponse(**result)


    def delete(self, app_id: int, managed_app_config_id: int) -> None:
        """
        Delete a managed app config.
        """
        self._delete(endpoint=f"{self._endpoint}/{app_id}/managed_configs/{managed_app_config_id}")


    def push_updates(self, app_id: int) -> None:
        """
        Push updates to a managed app config.
        """
        self._post(endpoint=f"{self._endpoint}/{app_id}/managed_configs/push")