"""
custom_attributes.py: Validation for SimpleMDM SDK Custom Attributes Groups class.
"""

import time
import requests
import simplemdm_sdk

from ._base import BaseValidation


class ValidateCustomAttributes(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Custom Attributes class...")

        print("  Validating list_all() method...")
        all_custom_attributes = self.api.custom_attributes.list_all()
        assert all_custom_attributes is not None, "Custom Attributes list_all() method returned None"

        if len(all_custom_attributes.data) > 0:
            print("  Validating retrieve_one() method...")
            custom_attribute_id = all_custom_attributes.data[0].id
            custom_attribute = self.api.custom_attributes.retrieve_one(custom_attribute_id)
            assert custom_attribute is not None, "Custom Attributes retrieve_one() method returned None"
            assert custom_attribute.data.id == custom_attribute_id, f"Custom Attribute ID {custom_attribute.data.id} does not match the requested ID {custom_attribute_id}."

        if self.read_only:
            print("  Skipping create(), update(), and delete() methods in read-only mode.")
            return

        print("  Validating create() method...")
        custom_attribute_name = "SimpleMDM_SDK_Test_Custom_Attribute"
        custom_attribute = self.api.custom_attributes.create(name=custom_attribute_name, default_value="Test Value")
        assert custom_attribute is not None, "Custom Attributes create() method returned None"
        assert custom_attribute.data.attributes.name == custom_attribute_name, f"Custom Attribute name {custom_attribute.data.attributes.name} does not match the requested name {custom_attribute_name}."
        assert custom_attribute.data.attributes.default_value == "Test Value", f"Custom Attribute default value {custom_attribute.data.attributes.default_value} does not match the requested default value Test Value."

        print("    data.attributes.name: ", custom_attribute.data.attributes.name)
        print("    data.attributes.default_value: ", custom_attribute.data.attributes.default_value)

        print("  Validating update() method...")
        self.api.custom_attributes.update(custom_attribute.data.id, default_value="SimpleMDM_SDK_Updated_Custom_Value")
        updated_custom_attribute = self.api.custom_attributes.retrieve_one(custom_attribute.data.id)
        assert updated_custom_attribute is not None, "Custom Attributes update() method returned None"
        assert updated_custom_attribute.data.attributes.default_value == "SimpleMDM_SDK_Updated_Custom_Value", "Custom Attributes update() method did not update name"
        print("    data.attributes.default_value: ", updated_custom_attribute.data.attributes.default_value)

        print("  Validating delete() method...")
        self.api.custom_attributes.delete(custom_attribute.data.id)
        # API returns before officially deleting the custom attribute, so we need to wait a bit
        time.sleep(5)
        try:
            self.api.custom_attributes.retrieve_one(custom_attribute.data.id)
            raise AssertionError("Custom Attributes delete() method did not delete the custom attribute")
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404, f"Custom Attributes delete() method did not return 404 error: {e.response.status_code}"

        # TODO: Implement the rest of the validation methods for Custom Attributes
        # - get_values_for_device()
        # - set_value_for_device()
        # - set_multiple_values_for_device()
        # - set_custom_attributes_for_multiple_devices()
        # - get_values_for_group()
        # - set_value_for_group()