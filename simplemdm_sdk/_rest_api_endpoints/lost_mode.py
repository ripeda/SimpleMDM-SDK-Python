"""
lost_mode.py: SimpleMDM Lost Mode REST API endpoints.
"""

from .._connection import Connection


class LostMode(Connection):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._endpoint = "devices"


    def enable(self, device_id: str) -> None:
        """
        Enable Lost Mode on a device.
        """
        self._post(endpoint=f"{self._endpoint}/{device_id}/lost_mode")


    def disable(self, device_id: str) -> None:
        """
        Disable Lost Mode on a device.
        """
        self._delete(endpoint=f"{self._endpoint}/{device_id}/lost_mode")


    def play_a_sound(self, device_id: str) -> None:
        """
        Play a sound on a device.
        """
        self._post(endpoint=f"{self._endpoint}/{device_id}/lost_mode/play_sound")


    def update_location(self, device_id: str) -> None:
        """
        Update the location of a device.
        """
        self._post(endpoint=f"{self._endpoint}/{device_id}/lost_mode/update_location")


