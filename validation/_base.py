"""
_base.py: Base validation model for SimpleMDM SDK.
"""

import simplemdm_sdk


class BaseValidation:

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True) -> None:
        self.api = api
        self.read_only = read_only


    def validate(self) -> None:
        """
        Validate the model.
        """
        raise NotImplementedError("Subclasses must implement this method.")