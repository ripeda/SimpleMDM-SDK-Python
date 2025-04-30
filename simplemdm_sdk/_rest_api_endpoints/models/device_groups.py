"""
device_groups.py: Pydantic models for SimpleMDM Device Groups API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class DeviceGroupAttributes(SimpleMDMSDKModel):
    name: str


class DeviceGroupRelationshipsDevicesData(SimpleMDMSDKModel):
    type: str
    id:   int


class DeviceGroupRelationshipsDevices(SimpleMDMSDKModel):
    data: list[DeviceGroupRelationshipsDevicesData]


class DeviceGroupRelationshipsAppsData(SimpleMDMSDKModel):
    devices: Optional[DeviceGroupRelationshipsDevices]


class DeviceGroupData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    DeviceGroupAttributes
    relationships: DeviceGroupRelationshipsAppsData


class DeviceGroupsListAllResponse(SimpleMDMSDKModel):
    data: list[DeviceGroupData]


class DeviceGroupResponse(SimpleMDMSDKModel):
    data: DeviceGroupData