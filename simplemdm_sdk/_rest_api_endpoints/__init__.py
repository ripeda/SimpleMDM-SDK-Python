"""
___init__.py: SimpleMDM REST API endpoint initialization file.
"""

from .account import Account
from .apps import Apps
from .assignment_groups import AssignmentGroups
from .custom_attributes import CustomAttributes
from .custom_configuration_profiles import CustomConfigurationProfiles
from .dep_servers import DEPServers
from .device_groups import DeviceGroups
from .devices import Devices
from .enrollments import Enrollments
from .installed_apps import InstalledApps
from .logs import Logs
from .lost_mode import LostMode
from .managed_app_configs import ManagedAppConfigs
from .profiles import Profiles
from .push_certificate import PushCertificate
from .script_jobs import ScriptJobs
from .scripts import Scripts


__all__ = [
    "Account",
    "Apps",
    "AssignmentGroups",
    "CustomAttributes",
    "CustomConfigurationProfiles",
    "DEPServers",
    "DeviceGroups",
    "Devices",
    "Enrollments",
    "InstalledApps",
    "Logs",
    "LostMode",
    "ManagedAppConfigs",
    "Profiles",
    "PushCertificate",
    "ScriptJobs",
    "Scripts",
]