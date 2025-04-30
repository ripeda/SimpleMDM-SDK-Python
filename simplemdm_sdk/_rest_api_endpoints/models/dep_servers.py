"""
dep_servers.py: Pydantic models for SimpleMDM DEP Servers API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class DepServerAttributes(SimpleMDMSDKModel):
    server_name:       str
    organization_name: str
    token_expires_at:  Optional[str] = None
    last_synced_at:    Optional[str] = None


class DepServerData(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: Optional[DepServerAttributes] = None


class DepServersListAllResponse(SimpleMDMSDKModel):
    data: list[DepServerData]


class DepServerResponse(SimpleMDMSDKModel):
    data: DepServerData


class DepServerDeviceDataAttributes(SimpleMDMSDKModel):
    serial_number: Optional[str] = None
    model:         Optional[str] = None
    color:         Optional[str] = None
    checked_in_at: Optional[str] = None


class DepServerDeviceRelationshipsDeviceData(SimpleMDMSDKModel):
    type: str
    id:   int


class DepServerDeviceRelationshipsDevice(SimpleMDMSDKModel):
    data: DepServerDeviceRelationshipsDeviceData


class DepServerDeviceGarbage(SimpleMDMSDKModel):
    device: DepServerDeviceRelationshipsDevice


class DepServerDeviceData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    DepServerDeviceDataAttributes
    relationships: DepServerDeviceGarbage


class DepServerDevicesListAllResponse(SimpleMDMSDKModel):
    data: list[DepServerDeviceData]


class DepServerDeviceResponse(SimpleMDMSDKModel):
    data: DepServerDeviceData