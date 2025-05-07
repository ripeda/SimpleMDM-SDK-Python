# SimpleMDM SDK Python

Python library for interacting with SimpleMDM's REST API. Pseudo-spiritual successor to SteveKueng/MacAdmin's [SimpleMDMpy](https://github.com/macadmins/simpleMDMpy), with a focus on type hinting through Pydantic models.

Note: Library is highly opinionated and may not be suitable for all use cases. Use at your own discretion.


## Notable differences from SimpleMDMpy

- Implicit conversion of parameters to strings when generating URLs.
  - ex. Passing device IDs as integers will no longer raises an error.
- Single public class for all API endpoints
  - No need to pass API keys to individual endpoint classes.
- Feature parity with SimpleMDM's API.
  - Currently validated against version 1.51.
- Function names matching SimpleMDM's API documentation.
  - ex. `SimpleMDM.Accounts.show()` instead of `SimpleMDM.Accounts.get_account()`.
  - Easier cross referencing of https://api.simplemdm.com.
- Pydantic models for API responses.
  - Provides type hints and validation for API responses.
  - Configure strictness of validation with `os.environ["SimpleMDMSDKModelExtra"] = "xxx"` before importing the library.
  - Defaults to `allow`, see [Pydantic's `ConfigDict.extra` documentation](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) for more information.
- Automatic ratelimit handling for all REST methods.
- Enums for static properties in function parameters.
  - ex. `SimpleMDM.AssignmentGroups.MunkiInstallType` instead of strings.


## Installation

```bash
python3 -m pip install simplemdm-sdk
```


## Usage

```py
from simplemdm_sdk import SimpleMDM

api_key = "your_api_key"
simplemdm = SimpleMDM(api_key)

# List all device names
for device in simplemdm.devices.list_all().data:
    print(device.attributes.name)
```

* Recommend right clicking data and selecting "Go to definition" in your IDE to see the Pydantic model for the response.

```py
class DeviceData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    Optional[DeviceAttributes]    = None
    relationships: Optional[DeviceRelationships] = None


class DevicesListAllResponse(SimpleMDMSDKModel):
    data: list[DeviceData]
```


## Supported functions

For a complete list of function descriptions, please refer to the [SimpleMDM API documentation](https://api.simplemdm.com).

```py
from simplemdm_sdk import SimpleMDM

simplemdm_object = SimpleMDM(api_key)
```

### account
```py
simplemdm_obj.account.show()
simplemdm_obj.account.update()
```
### apps
```py
simplemdm_obj.apps.create()
simplemdm_obj.apps.delete()
simplemdm_obj.apps.delete_munki_pkginfo()
simplemdm_obj.apps.list_all()
simplemdm_obj.apps.list_installs()
simplemdm_obj.apps.retrieve_one()
simplemdm_obj.apps.update()
simplemdm_obj.apps.update_munki_pkginfo()
```
### assignment_groups
```py
simplemdm_obj.assignment_groups.assign_app()
simplemdm_obj.assignment_groups.assign_device()
simplemdm_obj.assignment_groups.assign_device_group()
simplemdm_obj.assignment_groups.assign_profile()
simplemdm_obj.assignment_groups.clone()
simplemdm_obj.assignment_groups.create()
simplemdm_obj.assignment_groups.delete()
simplemdm_obj.assignment_groups.list_all()
simplemdm_obj.assignment_groups.push_apps()
simplemdm_obj.assignment_groups.retrieve_one()
simplemdm_obj.assignment_groups.sync_profiles()
simplemdm_obj.assignment_groups.unassign_app()
simplemdm_obj.assignment_groups.unassign_device()
simplemdm_obj.assignment_groups.unassign_device_group()
simplemdm_obj.assignment_groups.unassign_profile()
simplemdm_obj.assignment_groups.update()
simplemdm_obj.assignment_groups.update_apps()
```
### custom_attributes
```py
simplemdm_obj.custom_attributes.create()
simplemdm_obj.custom_attributes.delete()
simplemdm_obj.custom_attributes.get_values_for_device()
simplemdm_obj.custom_attributes.get_values_for_group()
simplemdm_obj.custom_attributes.list_all()
simplemdm_obj.custom_attributes.retrieve_one()
simplemdm_obj.custom_attributes.set_custom_attribute_value_for_multiple_devices()
simplemdm_obj.custom_attributes.set_multiple_values_for_a_device()
simplemdm_obj.custom_attributes.set_value_for_device()
simplemdm_obj.custom_attributes.set_value_for_group()
simplemdm_obj.custom_attributes.update()
```
### custom_configuration_profiles
```py
simplemdm_obj.custom_configuration_profiles.assign_to_device()
simplemdm_obj.custom_configuration_profiles.assign_to_device_group()
simplemdm_obj.custom_configuration_profiles.create()
simplemdm_obj.custom_configuration_profiles.delete()
simplemdm_obj.custom_configuration_profiles.download()
simplemdm_obj.custom_configuration_profiles.list_all()
simplemdm_obj.custom_configuration_profiles.unassign_from_device()
simplemdm_obj.custom_configuration_profiles.unassign_from_device_group()
simplemdm_obj.custom_configuration_profiles.update()
```
### dep_servers
```py
simplemdm_obj.dep_servers.list_all()
simplemdm_obj.dep_servers.list_dep_devices()
simplemdm_obj.dep_servers.retrieve_one()
simplemdm_obj.dep_servers.retrieve_one_dep_device()
simplemdm_obj.dep_servers.sync_with_apple()
```
### device_groups
```py
simplemdm_obj.device_groups.assign_device()
simplemdm_obj.device_groups.clone()
simplemdm_obj.device_groups.list_all()
simplemdm_obj.device_groups.retrieve_one()
```
### devices
```py
simplemdm_obj.devices.clear_firmware_password()
simplemdm_obj.devices.clear_passcode()
simplemdm_obj.devices.clear_recovery_lock_password()
simplemdm_obj.devices.clear_restrictions_password()
simplemdm_obj.devices.create()
simplemdm_obj.devices.delete()
simplemdm_obj.devices.delete_user()
simplemdm_obj.devices.disable_bluetooth()
simplemdm_obj.devices.disable_remote_desktop()
simplemdm_obj.devices.enable_bluetooth()
simplemdm_obj.devices.enable_remote_desktop()
simplemdm_obj.devices.list_all()
simplemdm_obj.devices.list_installed_apps()
simplemdm_obj.devices.list_profiles()
simplemdm_obj.devices.list_users()
simplemdm_obj.devices.lock()
simplemdm_obj.devices.push_assigned_apps()
simplemdm_obj.devices.refresh()
simplemdm_obj.devices.restart()
simplemdm_obj.devices.retrieve_one()
simplemdm_obj.devices.rotate_admin_password()
simplemdm_obj.devices.rotate_filevault_recovery_key()
simplemdm_obj.devices.rotate_firmware_password()
simplemdm_obj.devices.rotate_recovery_lock_password()
simplemdm_obj.devices.set_admin_password()
simplemdm_obj.devices.set_time_zone()
simplemdm_obj.devices.shut_down()
simplemdm_obj.devices.unenroll()
simplemdm_obj.devices.update()
simplemdm_obj.devices.update_os()
simplemdm_obj.devices.wipe()
```
### enrollments
```py
simplemdm_obj.enrollments.delete()
simplemdm_obj.enrollments.list_all()
simplemdm_obj.enrollments.retrieve_one()
simplemdm_obj.enrollments.send_invitation()
```
### installed_apps
```py
simplemdm_obj.installed_apps.install_update()
simplemdm_obj.installed_apps.request_management_of_app()
simplemdm_obj.installed_apps.retrieve_one()
simplemdm_obj.installed_apps.uninstall()
```
### logs
```py
simplemdm_obj.logs.list_all()
simplemdm_obj.logs.retrieve_one()
```
### lost_mode
```py
simplemdm_obj.lost_mode.disable()
simplemdm_obj.lost_mode.enable()
simplemdm_obj.lost_mode.play_a_sound()
simplemdm_obj.lost_mode.update_location()
```
### managed_app_configs
```py
simplemdm_obj.managed_app_configs.create()
simplemdm_obj.managed_app_configs.delete()
simplemdm_obj.managed_app_configs.get()
simplemdm_obj.managed_app_configs.push_updates()
```
### profiles
```py
simplemdm_obj.profiles.assign_to_device()
simplemdm_obj.profiles.assign_to_device_group()
simplemdm_obj.profiles.list_all()
simplemdm_obj.profiles.retrieve_one()
simplemdm_obj.profiles.unassign_from_device()
simplemdm_obj.profiles.unassign_from_device_group()
```
### push_certificate
```py
simplemdm_obj.push_certificate.get_signed_csr()
simplemdm_obj.push_certificate.show()
simplemdm_obj.push_certificate.update()
```
### script_jobs
```py
simplemdm_obj.script_jobs.cancel_job()
simplemdm_obj.script_jobs.create()
simplemdm_obj.script_jobs.list_all()
simplemdm_obj.script_jobs.retrieve_one()
```
### scripts
```py
simplemdm_obj.scripts.create()
simplemdm_obj.scripts.delete()
simplemdm_obj.scripts.list_all()
simplemdm_obj.scripts.retrieve_one()
simplemdm_obj.scripts.update()
```