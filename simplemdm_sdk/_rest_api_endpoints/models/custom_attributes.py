"""
custom_attributes.py: Pydantic models for SimpleMDM Custom Attributes API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class CustomAttributeAttributes(SimpleMDMSDKModel):
    name:          str
    default_value: Optional[str] = None


class CustomAttributeData(SimpleMDMSDKModel):
    type:       str
    id:         str
    attributes: CustomAttributeAttributes


class CustomAttributeResponse(SimpleMDMSDKModel):
    data: CustomAttributeData


class ListCustomAttributesResponse(SimpleMDMSDKModel):
    data: list[CustomAttributeData]