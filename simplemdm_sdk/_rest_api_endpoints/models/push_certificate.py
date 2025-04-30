"""
push_certificate.py: Pydantic models for SimpleMDM Push Certificate API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class PushCertificateAttributes(SimpleMDMSDKModel):
    apple_id:   Optional[str] = None
    expires_at: Optional[str] = None


class PushCertificateData(SimpleMDMSDKModel):
    type:       str
    attributes: PushCertificateAttributes


class PushCertificateResponse(SimpleMDMSDKModel):
    data: PushCertificateData


class PushCertificateSignedCSRResponse(SimpleMDMSDKModel):
    data: list[str] # Documentation states a string is returned..., but the type is actually a list of strings...