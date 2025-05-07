"""
custom_configuration_profiles.py: Validation for SimpleMDM SDK Custom Configuration Profiles class.
"""

import requests
import plistlib
import tempfile
import simplemdm_sdk

from ._base import BaseValidation


class ValidateCustomConfigurationProfiles(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Custom Configuration Profiles class...")

        print("  Validating list_all() method...")
        all_custom_configuration_profiles = self.api.custom_configuration_profiles.list_all()
        assert all_custom_configuration_profiles is not None, "Custom Configuration Profiles list_all() method returned None"

        if len(all_custom_configuration_profiles.data) > 0:
            print("  Validating retrieve_one() method...")
            custom_configuration_profile_id = all_custom_configuration_profiles.data[0].id
            custom_configuration_profile = self.api.custom_configuration_profiles.download(custom_configuration_profile_id)
            assert custom_configuration_profile is not None, "Custom Configuration Profiles retrieve_one() method returned None"
            try:
                plistlib.loads(custom_configuration_profile)
            except plistlib.InvalidFileException as e:
                raise ValueError(f"Custom Configuration Profile ID {custom_configuration_profile_id} is not a valid plist file.") from e

        if self.read_only:
            print("  Skipping create(), update(), and delete() methods in read-only mode.")
            return

        print("  Validating create() method...")
        with tempfile.NamedTemporaryFile(suffix=".mobileconfig", delete=True) as tmp_profile:
            profile_path = tmp_profile.name
            with open(profile_path, "wb") as f:
                f.write(self._profile_test().encode("utf-8"))
                f.flush()

                custom_configuration_profile = self.api.custom_configuration_profiles.create(
                    name="SimpleMDM_SDK_Test_Custom_Configuration_Profile",
                    mobileconfig=profile_path,
                    attribute_support=False,
                    escape_attributes=False,
                    reinstall_after_os_update=False,
                    user_scope=False,
                )
                assert custom_configuration_profile is not None, "Custom Configuration Profiles create() method returned None"
                assert custom_configuration_profile.data.attributes.name == "SimpleMDM_SDK_Test_Custom_Configuration_Profile", f"Custom Configuration Profile name {custom_configuration_profile.data.attributes.name} does not match the requested name SimpleMDM_SDK_Test_Custom_Configuration_Profile."
                assert custom_configuration_profile.data.attributes.reinstall_after_os_update is False, "Custom Configuration Profile create() method did not set reinstall_after_os_update to False"
                assert custom_configuration_profile.data.attributes.user_scope is False, "Custom Configuration Profile create() method did not set user_scope to False"
                assert custom_configuration_profile.data.attributes.attribute_support is False, "Custom Configuration Profile create() method did not set attribute_support to False"
                assert custom_configuration_profile.data.attributes.escape_attributes is False, "Custom Configuration Profile create() method did not set escape_attributes to False"

        print("    data.attributes.name: ", custom_configuration_profile.data.attributes.name)
        print("    data.attributes.reinstall_after_os_update: ", custom_configuration_profile.data.attributes.reinstall_after_os_update)
        print("    data.attributes.user_scope: ", custom_configuration_profile.data.attributes.user_scope)
        print("    data.attributes.attribute_support: ", custom_configuration_profile.data.attributes.attribute_support)
        print("    data.attributes.escape_attributes: ", custom_configuration_profile.data.attributes.escape_attributes)

        print("  Validating update() method...")
        updated_custom_configuration_profile = self.api.custom_configuration_profiles.update(
            custom_configuration_profile.data.id,
            name="SimpleMDM_SDK_Updated_Custom_Configuration_Profile",
            attribute_support=True,
            escape_attributes=True,
            reinstall_after_os_update=True,
            user_scope=True,
        )
        assert updated_custom_configuration_profile is not None, "Custom Configuration Profiles update() method returned None"
        assert updated_custom_configuration_profile.data.attributes.name == "SimpleMDM_SDK_Updated_Custom_Configuration_Profile", f"Custom Configuration Profile name {updated_custom_configuration_profile.data.attributes.name} does not match the requested name SimpleMDM_SDK_Updated_Custom_Configuration_Profile."
        assert updated_custom_configuration_profile.data.attributes.reinstall_after_os_update is True, "Custom Configuration Profile update() method did not set reinstall_after_os_update to True"
        assert updated_custom_configuration_profile.data.attributes.user_scope is True, "Custom Configuration Profile update() method did not set user_scope to True"
        assert updated_custom_configuration_profile.data.attributes.attribute_support is True, "Custom Configuration Profile update() method did not set attribute_support to True"
        assert updated_custom_configuration_profile.data.attributes.escape_attributes is True, "Custom Configuration Profile update() method did not set escape_attributes to True"
        print("    data.attributes.name: ", updated_custom_configuration_profile.data.attributes.name)
        print("    data.attributes.reinstall_after_os_update: ", updated_custom_configuration_profile.data.attributes.reinstall_after_os_update)
        print("    data.attributes.user_scope: ", updated_custom_configuration_profile.data.attributes.user_scope)
        print("    data.attributes.attribute_support: ", updated_custom_configuration_profile.data.attributes.attribute_support)
        print("    data.attributes.escape_attributes: ", updated_custom_configuration_profile.data.attributes.escape_attributes)

        print("  Validating delete() method...")
        self.api.custom_configuration_profiles.delete(updated_custom_configuration_profile.data.id)
        try:
            self.api.custom_configuration_profiles.download(updated_custom_configuration_profile.data.id)
            raise AssertionError("Custom Configuration Profiles delete() method did not delete the custom configuration profile")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code != 404:
                raise AssertionError("Custom Configuration Profiles delete() method did not delete the custom configuration profile") from e
            print("    Custom Configuration Profile deleted successfully.")

        # TODO: Add tests for the following methods:
        # - assign_to_device_group()
        # - unassign_from_device_group()
        # - assign_to_device()
        # - unassign_from_device()


    def _profile_test(self) -> str:
        """
        Test profile for the Custom Configuration Profiles class.
        """
        return r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>MaxAdminTime</key>
			<integer>300</integer>
			<key>Webhook</key>
			<string>https://internal.ripeda.com/escalate-webhooks</string>
			<key>WebhookExtras</key>
			<dict>
				<key>organization </key>
				<string>RIPEDA R&amp;D</string>
			</dict>
			<key>ExcludedUsers</key>
			<array>
				<string>itadmin</string>
				<string>ripeda</string>
			</array>
			<key>PayloadDisplayName</key>
			<string>Escalate</string>
			<key>PayloadIdentifier</key>
			<string>com.ripeda.escalate.D429C0E2-E92D-460A-A95C-4DA3044D9CC6</string>
			<key>PayloadType</key>
			<string>com.ripeda.escalate</string>
			<key>PayloadUUID</key>
			<string>D429C0E2-E92D-460A-A95C-4DA3044D9CC6</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
		</dict>
	</array>
	<key>PayloadDisplayName</key>
	<string>Escalate Admin Configuration - RIPEDA Consulting</string>
	<key>PayloadIdentifier</key>
	<string>com.ripeda.escalate-admin-configuration.ripeda.9940A360-3924-40F5-81A3-E6EA44AD101A</string>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
	<string>9940A360-3924-40F5-81A3-E6EA44AD101A</string>
	<key>PayloadVersion</key>
	<integer>1</integer>
</dict>
</plist>
"""