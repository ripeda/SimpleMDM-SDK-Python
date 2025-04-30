"""
push_certificate.py: SimpleMDM Push Certificate REST API endpoints.
"""

from .._connection import Connection
from .models.push_certificate import PushCertificateSignedCSRResponse, PushCertificateResponse


class PushCertificate(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "push_certificate"


    def show(self) -> PushCertificateResponse:
        """
        Show details related to the current push certificate being used.
        """
        result = self._get(self._endpoint)
        return PushCertificateResponse(**result)


    def update(self, push_certificate_file: str, apple_id: str = None) -> PushCertificateResponse:
        """
        Update the push certificate.
        """
        parameters = {}
        if apple_id:
            parameters["apple_id"] = apple_id

        files = {
            "file": open(push_certificate_file, "rb")
        }

        result = self._put(self._endpoint, parameters, files)
        return PushCertificateResponse(**result)


    def get_signed_csr(self) -> PushCertificateSignedCSRResponse:
        """
        Get the signed CSR for the push certificate.
        """
        result = self._get(f"{self._endpoint}/scsr")
        return PushCertificateSignedCSRResponse(**result)

