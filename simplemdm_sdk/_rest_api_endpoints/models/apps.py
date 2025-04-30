"""
apps.py: Pydantic models for SimpleMDM Apps API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class AppAttributes(SimpleMDMSDKModel):
    name:                  Optional[str] = None
    bundle_identifier:     Optional[str] = None
    app_type:              Optional[str] = None
    itunes_store_id:       Optional[int] = None
    version:               Optional[str] = None
    installation_channels: Optional[list[str]] = None
    platform_support:      Optional[str] = None
    processing_status:     Optional[str] = None


class AppData(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: Optional[AppAttributes] = None


class AppsListAllResponse(SimpleMDMSDKModel):
    data: list[AppData]


class AppResponse(SimpleMDMSDKModel):
    data: AppData


class DeviceAttributes(SimpleMDMSDKModel):
    name:          Optional[str] = None
    identifier:    Optional[str] = None
    version:       Optional[str] = None
    short_version: Optional[str] = None
    bundle_size:   Optional[int] = None
    dynamic_size:  Optional[int] = None
    managed:       Optional[bool] = None
    discovered_at: Optional[str] = None
    last_seen_at:  Optional[str] = None


class DeviceRelationshipsDeviceData(SimpleMDMSDKModel):
    type: str
    id:   int


class DeviceRelationshipsDevice(SimpleMDMSDKModel):
    data: DeviceRelationshipsDeviceData


class DeviceGarbage(SimpleMDMSDKModel):
    device: DeviceRelationshipsDevice


class ListInstallsDataAttributes(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    DeviceAttributes
    relationships: DeviceGarbage


class ListInstallsResponse(SimpleMDMSDKModel):
    data: list[ListInstallsDataAttributes]