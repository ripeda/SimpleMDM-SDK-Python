"""
apps.py: Validation for SimpleMDM SDK Apps class.
"""

import time
import tempfile
import requests
import simplemdm_sdk
import macos_pkg_builder

from ._base import BaseValidation


class ValidateApps(BaseValidation):

    def __init__(self, api: simplemdm_sdk.SimpleMDM, read_only: bool = True):
        super().__init__(api, read_only)


    def validate(self) -> None:
        """
        Validate the class.
        """
        print("Validating Apps class...")

        print("  Validating list_all() method...")
        all_apps = self.api.apps.list_all()
        for app in all_apps.data:
            assert app.attributes.app_type != "shared", f"App ID {app.id} is shared, but should not be included in the list."

        print("  Validating list_all() method with include_shared=True...")
        all_apps_with_shared = self.api.apps.list_all(include_shared=True)
        is_shared = any(app.attributes.app_type == "shared" for app in all_apps_with_shared.data)
        assert is_shared, "No shared apps found in the list when include_shared=True."

        print("  Validating retrieve_one() method...")
        app_id = all_apps.data[0].id
        app = self.api.apps.retrieve_one(app_id)
        assert app.data.id == app_id, f"App ID {app.data.id} does not match the requested ID {app_id}."

        print("  Validating list_installs() method...")
        installs = self.api.apps.list_installs(app_id)
        assert installs.data is not None, "No installs found for the app."
        if len(installs.data) > 0:
            assert installs.data[0].attributes.identifier == all_apps.data[0].attributes.bundle_identifier, f"App bundle identifier does not match the installs: {installs.data[0].attributes.identifier} != {all_apps.data[0].attributes.bundle_identifier}"

        if self.read_only:
            print("  Skipping create(), update(), delete(), update_munki_pkginfo(), and delete_munki_pkginfo() methods in read-only mode.")
            return

        print("  Validating create() method...")
        with tempfile.NamedTemporaryFile(suffix=".pkg", delete=True) as tmp_pkg:
            pkg_path = tmp_pkg.name

            with tempfile.NamedTemporaryFile(suffix=".sh", delete=True) as tmp_script:
                script_path = tmp_script.name
                tmp_script.write(b"#!/bin/bash\necho 'Hello World'")
                tmp_script.flush()

                assert macos_pkg_builder.Packages(
                    pkg_output=pkg_path,
                    pkg_bundle_id="com.ripeda.simplemdm_sdk.validation.apps",
                    pkg_preinstall_script=script_path,
                ).build() is True, "Failed to create a macOS package."

                 # Upload the pkg file
                app = self.api.apps.create(binary=pkg_path, name="SimpleMDM SDK Validation App")
                assert app.data.id is not None, "Failed to create the app."
                assert app.data.attributes.name == "SimpleMDM SDK Validation App", "App name does not match."

                while True:
                    app = self.api.apps.retrieve_one(app.data.id)
                    if app.data.attributes.processing_status == "processing":
                        print("    Processing...")
                        time.sleep(1)
                    else:
                        break

                assert app.data.attributes.processing_status == "processed", f"App processing failed: {app.data.attributes.processing_status}"
                assert app.data.attributes.app_type == "custom", f"App type is not 'custom': {app.data.attributes.app_type}"
                assert app.data.attributes.bundle_identifier == "com.ripeda.simplemdm_sdk.validation.apps", f"App bundle ID does not match: {app.data.attributes.bundle_identifier}"
                assert app.data.attributes.name == "SimpleMDM SDK Validation App", f"App name does not match: {app.data.attributes.name}"

        print("  Validating update() method...")
        updated_app = self.api.apps.update(app.data.id, name="SimpleMDM SDK Validation App Updated")
        assert updated_app.data.attributes.name == "SimpleMDM SDK Validation App Updated", f"App name does not match: {updated_app.data.attributes.name}"

        print("  Validating update_munki_pkginfo() method...")
        with tempfile.NamedTemporaryFile(suffix=".plist", delete=True) as tmp_munki:
            munki_path = tmp_munki.name
            with open(munki_path, "w") as f:
                f.write(self._munki_test())

            self.api.apps.update_munki_pkginfo(app.data.id, munki_path)

        print("  Validating delete_munki_pkginfo() method...")
        self.api.apps.delete_munki_pkginfo(app.data.id)

        print("  Validating delete() method...")
        self.api.apps.delete(updated_app.data.id)
        try:
            self.api.apps.retrieve_one(updated_app.data.id)
            raise AssertionError("App was not deleted.")
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404, f"App was not deleted: {e.response.status_code}"


    def _munki_test(self) -> str:
        """
        Test Munki pkginfo file.
        """
        return r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>_metadata</key>
    <dict>
      <key>created_by</key>
      <string>root</string>
      <key>creation_date</key>
      <date>2025-04-04T19:07:53Z</date>
      <key>munki_version</key>
      <string>6.6.1.4696</string>
      <key>os_version</key>
      <string>13.7.1</string>
    </dict>
    <key>autoremove</key>
    <false/>
    <key>catalogs</key>
    <array>
      <string>testing</string>
    </array>
    <key>installed_size</key>
    <integer>20760</integer>
    <key>installer_item_hash</key>
    <string>194b8b4f80e7f20c8be9ed86c17ddb1180dae7c5ed7cc51fec68bc908b5f918d</string>
    <key>installer_item_location</key>
    <string>RIPEDA-Baseline.pkg</string>
    <key>installer_item_size</key>
    <integer>20305</integer>
    <key>minimum_os_version</key>
    <string>10.5.0</string>
    <key>name</key>
    <string>RIPEDA-Baseline</string>
    <key>receipts</key>
    <array>
      <dict>
        <key>installed_size</key>
        <integer>20760</integer>
        <key>packageid</key>
        <string>com.ripeda.baseline</string>
        <key>version</key>
        <string>4.0.0</string>
      </dict>
    </array>
    <key>uninstall_method</key>
    <string>removepackages</string>
    <key>uninstallable</key>
    <true/>
    <key>version</key>
    <string>4.0.0</string>
  </dict>
</plist>
"""

