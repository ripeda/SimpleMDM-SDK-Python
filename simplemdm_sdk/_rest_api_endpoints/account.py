"""
account.py: SimpleMDM Account REST API endpoints.
"""

from .._connection import Connection
from .models.accounts import AccountResponse


class Account(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "account"


    def show(self) -> AccountResponse:
        """
        Retrieve information about your account.
        Subscription information is only available for accounts on a manual billing plan.
        """
        result = self._get(self._endpoint)
        return AccountResponse(**result)


    def update(self, name: str = None, apple_store_country_code: str = None) -> AccountResponse:
        """
        Update account information.
        """
        parameters = {}
        if name:
            parameters["name"] = name
        if apple_store_country_code:
            parameters["apple_store_country_code"] = apple_store_country_code

        result = self._patch(self._endpoint, parameters)
        return AccountResponse(**result)