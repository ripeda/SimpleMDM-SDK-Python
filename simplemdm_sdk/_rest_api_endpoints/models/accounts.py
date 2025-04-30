"""
account.py: Pydantic models for SimpleMDM Account API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class License(SimpleMDMSDKModel):
    total:     int
    available: int


class Subscription(SimpleMDMSDKModel):
    licenses: License


class Account(SimpleMDMSDKModel):
    name:                     Optional[str] = None
    apple_store_country_code: Optional[str] = None
    subscription:             Optional[Subscription] = None


class Data(SimpleMDMSDKModel):
    type:       str
    attributes: Account


class AccountResponse(SimpleMDMSDKModel):
    data: Data