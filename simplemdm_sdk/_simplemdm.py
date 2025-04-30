"""
__simplemdm.py: SimpleMDM REST and Autopkg API endpoint wrappers.
"""

from ._rest_api_endpoints import *
# from ._autopkg_endpoints import *


class SimpleMDM:

    def __init__(self, api_key: str):
        self.account                       = Account(api_key)
        self.apps                          = Apps(api_key)
        self.assignment_groups             = AssignmentGroups(api_key)
        self.custom_attributes             = CustomAttributes(api_key)
        self.custom_configuration_profiles = CustomConfigurationProfiles(api_key)
        self.dep_servers                   = DEPServers(api_key)
        self.device_groups                 = DeviceGroups(api_key)
        self.devices                       = Devices(api_key)
        self.enrollments                   = Enrollments(api_key)
        self.installed_apps                = InstalledApps(api_key)
        self.logs                          = Logs(api_key)
        self.lost_mode                     = LostMode(api_key)
        self.managed_app_configs           = ManagedAppConfigs(api_key)
        self.profiles                      = Profiles(api_key)
        self.push_certificate              = PushCertificate(api_key)
        self.script_jobs                   = ScriptJobs(api_key)
        self.scripts                       = Scripts(api_key)


# TODO: Uncomment and finish the AutoPkg API wrapper when ready
# class SimpleMDMAutoPkg:
#
#     def __init__(self, api_key: str):
#         self.catalogs = Catalogs(api_key)
#         self.icons    = Icons(api_key)
#         self.packages = Packages(api_key)