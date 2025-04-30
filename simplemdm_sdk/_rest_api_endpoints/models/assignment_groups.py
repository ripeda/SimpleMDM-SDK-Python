"""
assignment_groups.py: Pydantic models for SimpleMDM Assignment Groups API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class ListAssignmentGroupsRelationshipsAppsData(SimpleMDMSDKModel):
    type: str
    id:   int


class ListAssignmentGroupsRelationshipsDeviceGroupsData(SimpleMDMSDKModel):
    type: str
    id:   int


class ListAssignmentGroupsRelationshipsDevicesData(SimpleMDMSDKModel):
    type: str
    id:   int


class ListAssignmentGroupsAttributes(SimpleMDMSDKModel):
    name:               Optional[str] = None
    auto_deploy:        Optional[bool] = None
    priority:           Optional[int] = None
    app_track_location: Optional[bool] = None
    type:               Optional[str] = None
    group_type:         Optional[str] = None
    install_type:       Optional[str] = None


class ListAssignmentGroupsDataAttributes(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    ListAssignmentGroupsAttributes
    relationships: dict # TODO: Define a proper model for relationships


class ListAssignmentGroupsResponse(SimpleMDMSDKModel):
    data: list[ListAssignmentGroupsDataAttributes]


class AssignmentGroupsResponse(SimpleMDMSDKModel):
    data: ListAssignmentGroupsDataAttributes