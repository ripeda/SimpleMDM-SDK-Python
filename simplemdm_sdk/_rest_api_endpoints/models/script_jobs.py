"""
script_jobs.py: Pydantic models for SimpleMDM Script Jobs API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class ScriptJobAttributes(SimpleMDMSDKModel):
    script_name:            str
    job_name:               str
    content:                str
    job_id:                 str
    variable_support:       bool
    status:                 str
    pending_count:          int
    success_count:          int
    errored_count:          int
    custom_attribute_regex: Optional[str] = None
    created_by:             str
    created_at:             str
    updated_at:             str


class ScriptJobRelationshipsDeviceData(SimpleMDMSDKModel):
    type:        str
    id:          int
    status:      str
    status_code: Optional[str] = None
    response:    Optional[str] = None


class ScriptJobRelationshipsDevice(SimpleMDMSDKModel):
    data: list[ScriptJobRelationshipsDeviceData]


class ScriptJobRelationshipsCustomAttributeData(SimpleMDMSDKModel):
    type: str
    id:   str


class ScriptJobRelationshipsCustomAttribute(SimpleMDMSDKModel):
    data: ScriptJobRelationshipsCustomAttributeData


class ScriptJobRelationships(SimpleMDMSDKModel):
    device:           Optional[ScriptJobRelationshipsDevice] = None
    custom_attribute: Optional[ScriptJobRelationshipsCustomAttribute] = None


class ScriptJobData(SimpleMDMSDKModel):
    type: str
    id:   int
    attributes:    Optional[ScriptJobAttributes] = None
    relationships: Optional[ScriptJobRelationships] = None


class ScriptJobsListAllResponse(SimpleMDMSDKModel):
    data: list[ScriptJobData]


class ScriptJobResponse(SimpleMDMSDKModel):
    data: ScriptJobData