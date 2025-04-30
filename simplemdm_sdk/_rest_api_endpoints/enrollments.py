"""
enrollments.py: SimpleMDM Enrollments REST API endpoints.
"""

from .._connection import Connection
from .models.enrollments import EnrollmentsListAllResponse, EnrollmentResponse


class Enrollments(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "enrollments"


    def list_all(self) -> EnrollmentsListAllResponse:
        """
        List all enrollments.
        """
        result = self._get(self._endpoint)
        return EnrollmentsListAllResponse(**result)


    def retrieve_one(self, enrollment_id: int) -> EnrollmentResponse:
        """
        Retrieve one enrollment.
        """
        result = self._get(f"{self._endpoint}/{enrollment_id}")
        return EnrollmentResponse(**result)


    def send_invitation(self, enrollment_id: int, contact: str) -> None:
        """
        Send an enrollment invitation.
        """
        parameters = {
            "contact": contact
        }
        self._post(f"{self._endpoint}/{enrollment_id}/invitations", parameters)


    def delete(self, enrollment_id: int) -> None:
        """
        Delete an enrollment.
        """
        self._delete(f"{self._endpoint}/{enrollment_id}")