"""
profiles.py: Pydantic models for SimpleMDM Profiles API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class ListProfilesAttributes(SimpleMDMSDKModel):
    name:                      str
    profile_identifier:        str
    user_scope:                bool
    group_count:               int
    reinstall_after_os_update: Optional[bool] = None
    device_count:              int
    attribute_support:         Optional[bool] = None
    escape_attributes:         Optional[bool] = None


class ListProfilesRelationshipsDeviceGroupsListData(SimpleMDMSDKModel):
    type: str
    id:   int


class ListProfilesRelationshipsDeviceGroupsGroupsDataListData(SimpleMDMSDKModel):
    type:       str
    id:         int
    group_type: str


class ListProfilesRelationshipsDeviceGroupsGroupsData(SimpleMDMSDKModel):
    data: list[ListProfilesRelationshipsDeviceGroupsGroupsDataListData]


class ListProfilesRelationshipsDeviceGroups(SimpleMDMSDKModel):
    data:   list[ListProfilesRelationshipsDeviceGroupsListData]
    groups: Optional[ListProfilesRelationshipsDeviceGroupsGroupsData] = None


class ListProfilesRelationships(SimpleMDMSDKModel):
    device_groups: Optional[ListProfilesRelationshipsDeviceGroups] = None


class ListProfilesData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    ListProfilesAttributes
    relationships: ListProfilesRelationships


class ListProfilesResponse(SimpleMDMSDKModel):
    data: list[ListProfilesData]


class ProfilesResponse(SimpleMDMSDKModel):
    data: ListProfilesData