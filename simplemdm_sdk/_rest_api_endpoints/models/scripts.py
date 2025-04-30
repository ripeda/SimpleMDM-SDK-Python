"""
scripts.py: Pydantic models for SimpleMDM Scripts API endpoints.
"""

from ._base_model import SimpleMDMSDKModel


class ScriptAttributes(SimpleMDMSDKModel):
    name:             str
    content:          str
    variable_support: bool
    created_at:       str
    updated_at:       str


class ScriptData(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: ScriptAttributes


class ScriptsListAllResponse(SimpleMDMSDKModel):
    data: list[ScriptData]


class ScriptResponse(SimpleMDMSDKModel):
    data: ScriptData