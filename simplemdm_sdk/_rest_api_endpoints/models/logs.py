"""
logs.py: Pydantic models for SimpleMDM Logs API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class LogRelationshipsAccountData(SimpleMDMSDKModel):
    type:    str
    id:      int
    api_key: Optional[str] = None

class LogRelationshipsAccount(SimpleMDMSDKModel):
    data: LogRelationshipsAccountData


class LogRelationshipsUserData(SimpleMDMSDKModel):
    type:  str
    id:    int
    email: Optional[str] = None


class LogRelationshipsUser(SimpleMDMSDKModel):
    data: LogRelationshipsUserData


class LogRelationshipsDeviceDataData(SimpleMDMSDKModel):
    type:          str
    serial_number: Optional[str] = None
    udid:          Optional[str] = None


class LogRelationshipsDeviceData(SimpleMDMSDKModel):
    data: LogRelationshipsDeviceDataData


class LogRelationships(SimpleMDMSDKModel):
    account: LogRelationshipsAccount
    user:    Optional[LogRelationshipsUser] = None
    device:  Optional[LogRelationshipsDeviceData] = None



class LogAttributes(SimpleMDMSDKModel):
    namespace:     str
    event_type:    str
    level:         int | str
    source:        str
    at:            str
    metadata:      Optional[dict] = None # TODO: Define a proper model for metadata
    relationships: LogRelationships


class LogData(SimpleMDMSDKModel):
    type:       str
    id:         str
    attributes: Optional[LogAttributes] = None


class LogsListAllResponse(SimpleMDMSDKModel):
    data: list[LogData]


class LogResponse(SimpleMDMSDKModel):
    data: LogData