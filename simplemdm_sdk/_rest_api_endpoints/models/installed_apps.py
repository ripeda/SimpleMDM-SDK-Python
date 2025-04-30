"""
installed_apps.py: Pydantic models for SimpleMDM Installed Apps API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class InstalledAppAttributes(SimpleMDMSDKModel):
    name:          str
    identifier:    Optional[str] = None
    version:       Optional[str] = None
    short_version: Optional[str] = None
    bundle_size:   Optional[int] = None
    dynamic_size:  Optional[int] = None
    managed:       bool
    discovered_at: str
    last_seen_at:  str


class InstalledAppData(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: Optional[InstalledAppAttributes] = None


class InstalledAppResponse(SimpleMDMSDKModel):
    data: InstalledAppData