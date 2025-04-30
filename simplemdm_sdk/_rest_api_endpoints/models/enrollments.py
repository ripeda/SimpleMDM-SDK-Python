"""
enrollments.py: Pydantic models for SimpleMDM Enrollments API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class EnrollmentAttributes(SimpleMDMSDKModel):
    url:             Optional[str] = None
    user_enrollment: bool
    welcome_screen:  bool
    authentication:  bool


class EnrollmentRelationshipsDeviceGroupData(SimpleMDMSDKModel):
    type: str
    id:   int


class EnrollmentRelationshipsDeviceGroup(SimpleMDMSDKModel):
    data: EnrollmentRelationshipsDeviceGroupData


class EnrollmentRelationshipsDeviceData(SimpleMDMSDKModel):
    type: str
    id:   int

class EnrollmentRelationshipsDevice(SimpleMDMSDKModel):
    data: EnrollmentRelationshipsDeviceData


class EnrollmentRelationships(SimpleMDMSDKModel):
    device_group: EnrollmentRelationshipsDeviceGroup
    device:       Optional[EnrollmentRelationshipsDevice] = None


class EnrollmentData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    Optional[EnrollmentAttributes] = None
    relationships: Optional[EnrollmentRelationships] = None


class EnrollmentsListAllResponse(SimpleMDMSDKModel):
    data: list[EnrollmentData]


class EnrollmentResponse(SimpleMDMSDKModel):
    data: EnrollmentData