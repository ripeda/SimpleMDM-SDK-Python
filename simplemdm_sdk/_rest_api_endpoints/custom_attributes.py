"""
custom_attributes.py: SimpleMDM Custom Attributes REST API endpoints.
"""
import re

from .._connection import Connection
from .models.custom_attributes import ListCustomAttributesResponse, CustomAttributeResponse


class CustomAttributes(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)

        # Love SimpleMDM's disorganized API...
        self._endpoint_custom_attributes = "custom_attributes"
        self._endpoint_devices           = "devices"
        self._endpoint_device_groups     = "device_groups"


    def list_all(self) -> ListCustomAttributesResponse:
        """
        List all custom attributes
        """
        result = self._get(self._endpoint_custom_attributes)
        return ListCustomAttributesResponse(**result)


    def retrieve_one(self, custom_attribute_id: str) -> CustomAttributeResponse:
        """
        Retrieve one custom attribute
        """
        result = self._get(f"{self._endpoint_custom_attributes}/{custom_attribute_id}")
        return CustomAttributeResponse(**result)


    def create(self, name: str, default_value: str = None) -> CustomAttributeResponse:
        """
        Create a custom attribute
        """
        # Ref: https://stackoverflow.com/a/16982669
        if not re.match(r'^\w+$', name):
            raise ValueError("Name must be alphanumeric / underscore")

        parameters = {
            "name": name,
        }
        if default_value:
            parameters["default_value"] = default_value
        result = self._post(self._endpoint_custom_attributes, parameters)
        return CustomAttributeResponse(**result)


    def update(self, custom_attribute_id: str, default_value: str) -> None:
        """
        Update a custom attribute
        """
        parameters = {
            "default_value": default_value
        }
        self._patch(f"{self._endpoint_custom_attributes}/{custom_attribute_id}", parameters)


    def delete(self, custom_attribute_id: str) -> None:
        """
        Delete a custom attribute
        """
        self._delete(f"{self._endpoint_custom_attributes}/{custom_attribute_id}")


    def get_values_for_device(self, device_id: int) -> ListCustomAttributesResponse:
        """
        Get values for device
        """
        result = self._get(f"{self._endpoint_devices}/{device_id}/custom_attribute_values")
        return ListCustomAttributesResponse(**result)


    def set_value_for_device(self, device_id: int, custom_attribute_id: str, value: str) -> CustomAttributeResponse:
        """
        Set value for device
        """
        parameters = {
            "value": value
        }
        result = self._put(f"{self._endpoint_devices}/{device_id}/custom_attribute_values/{custom_attribute_id}", parameters)
        return CustomAttributeResponse(**result)


    def set_multiple_values_for_a_device(self, device_id: int, custom_attributes: list[dict]) -> ListCustomAttributesResponse:
        """
        Set multiple values for a device

        Requires an array of json objects where each object contains a 'name' and 'value' key

        Example:
       [
            {
                "name": "my_custom_attribute_1",
                "value": "test1"
            },
            {
                "name": "my_custom_attribute_2",
                "value": "test2"
            }
        ]
        """
        parameters = {
            "data": custom_attributes
        }
        result = self._put(f"{self._endpoint_devices}/{device_id}/custom_attribute_values", parameters)
        return ListCustomAttributesResponse(**result)



    def set_custom_attribute_value_for_multiple_devices(self, devices_and_attributes: list[dict]) -> ListCustomAttributesResponse:
        """
        Set custom attribute value for multiple devices


        Example:
        [
            {
                "device_id": "123",
                "value": "test1"
            },
            {
                "device_id": "321",
                "value": "test2"
            }
        ]
        """
        parameters = {
            "data": devices_and_attributes
        }
        result = self._put(f"{self._endpoint_devices}/custom_attribute_values", parameters)
        return ListCustomAttributesResponse(**result)


    def get_values_for_group(self, group_id: int) -> ListCustomAttributesResponse:
        """
        Get values for group
        """
        result = self._get(f"{self._endpoint_device_groups}/{group_id}/custom_attribute_values")
        return ListCustomAttributesResponse(**result)


    def set_value_for_group(self, group_id: int, custom_attribute_id: str, value: str) -> CustomAttributeResponse:
        """
        Set value for group
        """
        parameters = {
            "value": value
        }
        result = self._put(f"{self._endpoint_device_groups}/{group_id}/custom_attribute_values/{custom_attribute_id}", parameters)
        return CustomAttributeResponse(**result)