"""
managed_app_configs.py: Pydantic models for SimpleMDM Managed App Configs API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class ManagedAppConfigAttributes(SimpleMDMSDKModel):
    key:        str
    value:      str
    value_type: str


class ManagedAppConfigData(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: Optional[ManagedAppConfigAttributes] = None


class ManagedAppConfigResponse(SimpleMDMSDKModel):
    data: ManagedAppConfigData


class ManagedAppConfigListResponse(SimpleMDMSDKModel):
    data: list[ManagedAppConfigData]