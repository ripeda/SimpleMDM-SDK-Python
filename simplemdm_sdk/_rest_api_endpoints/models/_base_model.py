"""
_base_model.py: Base model for SimpleMDM SDK Pydantic models.
"""

import os

from pydantic import BaseModel, ConfigDict


class SimpleMDMSDKModel(BaseModel):
    model_config = ConfigDict(extra=os.getenv("SimpleMDMSDKModelExtra", "allow"))