"""
custom_configuration_profiles.py: Pydantic models for SimpleMDM Custom Configuration Profiles API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class CustomConfigurationProfileAttributes(SimpleMDMSDKModel):
    name:                      str
    reinstall_after_os_update: bool
    profile_identifier:        str
    user_scope:                bool
    attribute_support:         bool
    escape_attributes:         bool
    group_count:               int
    device_count:              int


class CustomConfigurationProfileRelationshipsDeviceGroupsData(SimpleMDMSDKModel):
    type: str
    id:   int


class CustomConfigurationProfileRelationshipsDeviceGroupsGroupsData(SimpleMDMSDKModel):
    type:       str
    group_type: str
    id:         int


class CustomConfigurationProfileRelationshipsDeviceGroupsGroups(SimpleMDMSDKModel):
    data: list[CustomConfigurationProfileRelationshipsDeviceGroupsGroupsData]


class CustomConfigurationProfileRelationshipsDeviceGroups(SimpleMDMSDKModel):
    data:   list[CustomConfigurationProfileRelationshipsDeviceGroupsData]
    groups: Optional[CustomConfigurationProfileRelationshipsDeviceGroupsGroups] = None


class CustomConfigurationProfileRelationships(SimpleMDMSDKModel):
    device_groups: CustomConfigurationProfileRelationshipsDeviceGroups


class CustomConfigurationProfileDataAttributes(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    CustomConfigurationProfileAttributes
    relationships: CustomConfigurationProfileRelationships


class CustomConfigurationProfileData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    Optional[CustomConfigurationProfileAttributes] = None
    relationships: Optional[CustomConfigurationProfileRelationships] = None


class CustomConfigurationProfilesListAllResponse(SimpleMDMSDKModel):
    data: list[CustomConfigurationProfileData]


class CustomConfigurationProfileResponse(SimpleMDMSDKModel):
    data: CustomConfigurationProfileData