"""
managed_app_configs.py: Validation for SimpleMDM SDK Managed App Configs class.
"""

import simplemdm_sdk

from ._base import BaseValidation


class ValidateManagedAppConfigs(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Managed App Configs class...")


        print("  Validating get() method...")
        apps = self.api.apps.list_all()
        # Ensure we don't grab shared apps
        apps = [app for app in apps.data if not app.attributes.app_type == "shared" and app.attributes.name != "SimpleMDM"]
        assert len(apps) > 0, "No apps found to validate Managed App Configs"
        app_id = apps[0].id

        managed_app_configs = self.api.managed_app_configs.get(app_id)
        assert managed_app_configs is not None, "Managed App Configs get() method returned None"
        current_count = len(managed_app_configs.data)

        if self.read_only:
            print("  Skipping create(), delete() and push_updates() methods in read-only mode.")
            return

        print("  Validating create() method...")
        key = "com.ripeda.simplemdm-sdk"
        value = "demo"
        managed_app_config = self.api.managed_app_configs.create(app_id, key, value, self.api.managed_app_configs.ValueType.STRING)
        assert managed_app_config is not None, "Managed App Configs create() method returned None"
        assert managed_app_config.data.attributes.key == key, f"Managed App Configs create() method returned a different key: {managed_app_config.data.attributes.key} != {key}"
        assert managed_app_config.data.attributes.value == value, f"Managed App Configs create() method returned a different value: {managed_app_config.data.attributes.value} != {value}"
        print("  Validating push_updates() method...")
        self.api.managed_app_configs.push_updates(app_id)

        print("  Validating delete() method...")
        managed_app_config_id = managed_app_config.data.id
        self.api.managed_app_configs.delete(app_id, managed_app_config_id)

        print("  Validating get() method again...")
        managed_app_configs = self.api.managed_app_configs.get(app_id)
        assert managed_app_configs is not None, "Managed App Configs get() method returned None"
        assert len(managed_app_configs.data) == current_count, f"Managed App Configs get() method returned a different count: {len(managed_app_configs.data)} != {current_count}"
