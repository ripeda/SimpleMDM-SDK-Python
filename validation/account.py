"""
account.py: Validation for SimpleMDM SDK Account class.
"""

from ._base import BaseValidation

import simplemdm_sdk


class ValidateAccount(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Account class...")

        print("  Validating show() method...")
        account = self.api.account.show()
        assert account is not None, "Account show() method returned None"
        print(f"    data.attributes.name: {account.data.attributes.name}")
        print(f"    data.attributes.apple_store_country_code: {account.data.attributes.apple_store_country_code}")

        if self.read_only:
            print("  Skipping update() method validation in read-only mode...")
            return

        print("  Validating update() method...")
        updated_account = self.api.account.update(name="SimpleMDM SDK", apple_store_country_code="AU")
        assert updated_account is not None, "Account update() method returned None"
        assert updated_account.data.attributes.name == "SimpleMDM SDK", "Account update() method did not update name"
        assert updated_account.data.attributes.apple_store_country_code == "AU", "Account update() method did not update apple_store_country_code"
        print("    data.attributes.name: ", updated_account.data.attributes.name)
        print("    data.attributes.apple_store_country_code: ", updated_account.data.attributes.apple_store_country_code)

        print("  Validating update() method (reverting changes)...")
        revert_account = self.api.account.update(name=account.data.attributes.name, apple_store_country_code=account.data.attributes.apple_store_country_code)
        assert revert_account is not None, "Account update() method returned None"
        assert revert_account.data.attributes.name == account.data.attributes.name, "Account update() method did not revert name"
        assert revert_account.data.attributes.apple_store_country_code == account.data.attributes.apple_store_country_code, "Account update() method did not revert apple_store_country_code"
        print("    data.attributes.name: ", revert_account.data.attributes.name)
        print("    data.attributes.apple_store_country_code: ", revert_account.data.attributes.apple_store_country_code)
