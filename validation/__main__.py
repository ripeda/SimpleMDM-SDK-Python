"""
__main__.py
"""

import simplemdm_sdk

from .account                       import ValidateAccount
from .apps                          import ValidateApps
from .assignment_groups             import ValidateAssignmentGroups
from .custom_attributes             import ValidateCustomAttributes
from .custom_configuration_profiles import ValidateCustomConfigurationProfiles
from .dep_servers                   import ValidateDEPServers
from .device_groups                 import ValidateDeviceGroups
from .devices                       import ValidateDevices
from .enrollments                   import ValidateEnrollments
from .installed_apps                import ValidateInstalledApps
from .logs                          import ValidateLogs
from .lost_mode                     import ValidateLostMode
from .managed_app_configs           import ValidateManagedAppConfigs
from .profiles                      import ValidateProfiles
from .push_certificate              import ValidatePushCertificate
from .script_jobs                   import ValidateScriptJobs
from .scripts                       import ValidateScripts


class Validation:

    def __init__(self, api_key: str, read_only: bool = False) -> None:
        self.api = simplemdm_sdk.SimpleMDM(api_key)
        self.read_only = read_only

        self.account                       = ValidateAccount(self.api, read_only)
        self.apps                          = ValidateApps(self.api, read_only)
        self.assignment_groups             = ValidateAssignmentGroups(self.api, read_only)
        self.custom_attributes             = ValidateCustomAttributes(self.api, read_only)
        self.custom_configuration_profiles = ValidateCustomConfigurationProfiles(self.api, read_only)
        self.dep_servers                   = ValidateDEPServers(self.api, read_only)
        self.device_groups                 = ValidateDeviceGroups(self.api, read_only)
        self.devices                       = ValidateDevices(self.api, read_only)
        self.enrollments                   = ValidateEnrollments(self.api, read_only)
        self.installed_apps                = ValidateInstalledApps(self.api, read_only)
        self.logs                          = ValidateLogs(self.api, read_only)
        self.lost_mode                     = ValidateLostMode(self.api, read_only)
        self.managed_app_configs           = ValidateManagedAppConfigs(self.api, read_only)
        self.profiles                      = ValidateProfiles(self.api, read_only)
        self.push_certificate              = ValidatePushCertificate(self.api, read_only)
        self.script_jobs                   = ValidateScriptJobs(self.api, read_only)
        self.scripts                       = ValidateScripts(self.api, read_only)


    def validate(self) -> None:
        """
        Validate the SDK.
        """
        print(f"Validating SimpleMDM SDK in {'read-only' if self.read_only else 'read-write'} mode...")
        self.account.validate()
        self.apps.validate()
        self.assignment_groups.validate()
        self.custom_attributes.validate()
        self.custom_configuration_profiles.validate()
        self.dep_servers.validate()
        self.device_groups.validate()
        self.devices.validate()
        self.enrollments.validate()
        self.installed_apps.validate()
        self.logs.validate()
        self.lost_mode.validate()
        self.managed_app_configs.validate()
        self.profiles.validate()
        self.push_certificate.validate()
        self.script_jobs.validate()
        self.scripts.validate()