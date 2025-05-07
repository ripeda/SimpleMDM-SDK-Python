"""
push_certificate.py: Validation for SimpleMDM SDK Push Certificate class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidatePushCertificate(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Push Certificate class...")

        print("  Validating show() method...")
        push_certificate = self.api.push_certificate.show()
        assert push_certificate is not None, "Push Certificate show() method returned None"

        print("  Validating get_signed_csr() method...")
        signed_csr = self.api.push_certificate.get_signed_csr()
        assert signed_csr is not None, "Push Certificate get_signed_csr() method returned None"

        if self.read_only:
            print("  Skipping update() methods in read-only mode.")
            return
        
        # TODO: Implement the rest...