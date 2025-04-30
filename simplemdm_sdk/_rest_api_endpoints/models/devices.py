"""
devices.py: Pydantic models for SimpleMDM Devices API endpoints.
"""

from typing import Optional

from ._base_model import SimpleMDMSDKModel


class DeviceAttributeServiceSubscription(SimpleMDMSDKModel):
    slot:                     Optional[str] = None
    carrier_settings_version: Optional[str] = None
    current_carrier_network:  Optional[str] = None
    current_mcc:              Optional[str] = None
    current_mnc:              Optional[str] = None
    iccid:                    Optional[str] = None
    imei:                     Optional[str] = None
    phone_number:             Optional[str] = None
    is_data_preferred:        Optional[bool] = None
    is_voice_preferred:       Optional[bool] = None
    label:                    Optional[str] = None
    meid:                     Optional[str] = None
    eid:                      Optional[str] = None


class DeviceAttributeFirewall(SimpleMDMSDKModel):
    enabled:            Optional[bool] = None
    block_all_incoming: Optional[bool] = None
    stealth_mode:       Optional[bool] = None


class DeviceAttributeOSUpdate(SimpleMDMSDKModel):
    automatic_os_installation_enabled:  Optional[bool] = None
    automatic_app_installation_enabled: Optional[bool] = None
    automatic_check_enabled:            Optional[bool] = None
    automatic_security_updates_enabled: Optional[bool] = None
    background_download_enabled:        Optional[bool] = None
    catalog_url:                        Optional[str]  = None
    default_catalog:                    Optional[bool] = None
    perform_periodic_check:             Optional[bool] = None
    previous_scan_date:                 Optional[str]  = None
    previous_scan_result:               Optional[str]  = None


class DeviceAttributes(SimpleMDMSDKModel):
    model_config = SimpleMDMSDKModel.model_config
    model_config['protected_namespaces'] = ()

    name:                                     Optional[str] = None
    last_seen_at:                             Optional[str] = None
    last_seen_ip:                             Optional[str] = None
    enrolled_at:                              Optional[str] = None
    status:                                   Optional[str] = None
    enrollment_channels:                      Optional[list[str]] = None
    enrollment_url:                           Optional[str] = None
    device_name:                              Optional[str] = None
    auto_admin_name:                          Optional[str] = None
    os_version:                               Optional[str] = None
    build_version:                            Optional[str] = None
    model_name:                               Optional[str] = None
    model:                                    Optional[str] = None
    product_name:                             Optional[str] = None
    unique_identifier:                        Optional[str] = None
    serial_number:                            Optional[str] = None
    processor_architecture:                   Optional[str] = None
    imei:                                     Optional[str] = None
    meid:                                     Optional[str] = None
    device_capacity:                          Optional[float] = None
    available_device_capacity:                Optional[float] = None
    battery_level:                            Optional[str] = None
    modem_firmware_version:                   Optional[str] = None
    iccid:                                    Optional[str] = None
    bluetooth_mac:                            Optional[str] = None
    ethernet_macs:                            Optional[list[str]] = None
    wifi_mac:                                 Optional[str] = None
    current_carrier_network:                  Optional[str] = None
    sim_carrier_network:                      Optional[str] = None
    subscriber_carrier_network:               Optional[str] = None
    carrier_settings_version:                 Optional[str] = None
    phone_number:                             Optional[str] = None
    voice_roaming_enabled:                    Optional[bool] = None
    data_roaming_enabled:                     Optional[bool] = None
    is_roaming:                               Optional[bool] = None
    subscriber_mcc:                           Optional[str] = None
    subscriber_mnc:                           Optional[str] = None
    simmnc:                                   Optional[str] = None
    current_mcc:                              Optional[str] = None
    current_mnc:                              Optional[str] = None
    hardware_encryption_caps:                 Optional[int] = None
    passcode_present:                         Optional[bool] = None
    passcode_compliant:                       Optional[bool] = None
    passcode_compliant_with_profiles:         Optional[bool] = None
    is_supervised:                            Optional[bool] = None
    is_dep_enrollment:                        Optional[bool] = None
    dep_enrolled:                             Optional[bool] = None
    dep_assigned:                             Optional[bool] = None
    is_user_approved_enrollment:              Optional[bool] = None
    is_device_locator_service_enabled:        Optional[bool] = None
    is_do_not_disturb_in_effect:              Optional[bool] = None
    personal_hotspot_enabled:                 Optional[bool] = None
    itunes_store_account_is_active:           Optional[bool] = None
    cellular_technology:                      Optional[int] = None
    last_cloud_backup_date:                   Optional[str] = None
    is_activation_lock_enabled:               Optional[bool] = None
    is_cloud_backup_enabled:                  Optional[bool] = None
    filevault_enabled:                        Optional[bool] = None
    filevault_recovery_key:                   Optional[str] = None
    lost_mode_enabled:                        Optional[bool] = None
    firmware_password_enabled:                Optional[bool] = None
    recovery_lock_password_enabled:           Optional[bool] = None
    remote_desktop_enabled:                   Optional[bool] = None
    supplemental_build_version:               Optional[str] = None
    supplemental_os_version_extra:            Optional[str] = None
    time_zone:                                Optional[str] = None
    user_enrollment:                          Optional[bool] = None
    ddm_enabled:                              Optional[bool] = None
    firmware_password:                        Optional[str] = None
    recovery_lock_password:                   Optional[str] = None
    firewall:                                 Optional[DeviceAttributeFirewall] = None
    system_integrity_protection_enabled:      Optional[bool] = None
    os_update:                                Optional[DeviceAttributeOSUpdate] = None
    service_subscriptions:                    Optional[list[DeviceAttributeServiceSubscription]] = None
    location_latitude:                        Optional[float] = None
    location_longitude:                       Optional[float] = None
    location_accuracy:                        Optional[float] = None
    location_updated_at:                      Optional[str] = None


class DeviceRelationshipsDeviceGroupData(SimpleMDMSDKModel):
    type: str
    id:   int

class DeviceRelationshipsDeviceGroup(SimpleMDMSDKModel):
    data: DeviceRelationshipsDeviceGroupData


class DeviceRelationshipsGroupData(SimpleMDMSDKModel):
    type:       str
    group_type: str
    id:         int


class DeviceRelationshipsGroup(SimpleMDMSDKModel):
    data: list[DeviceRelationshipsGroupData]


class DeviceRelationshipsCustomAttributeValuesDataAttributes(SimpleMDMSDKModel):
    value:  str
    secret: bool


class DeviceRelationshipsCustomAttributeValuesData(SimpleMDMSDKModel):
    type:       str
    id:         str
    attributes: DeviceRelationshipsCustomAttributeValuesDataAttributes


class DeviceRelationshipsCustomAttributeValues(SimpleMDMSDKModel):
    data: list[DeviceRelationshipsCustomAttributeValuesData]


class DeviceRelationships(SimpleMDMSDKModel):
    device_group:            Optional[DeviceRelationshipsDeviceGroup] = None
    groups:                  Optional[DeviceRelationshipsGroup] = None
    custom_attribute_values: Optional[DeviceRelationshipsCustomAttributeValues] = None


class DeviceData(SimpleMDMSDKModel):
    type:          str
    id:            int
    attributes:    Optional[DeviceAttributes] = None
    relationships: Optional[DeviceRelationships] = None


class DevicesListAllResponse(SimpleMDMSDKModel):
    data: list[DeviceData]


class DeviceResponse(SimpleMDMSDKModel):
    data: DeviceData


class DeviceProfilesAttributes(SimpleMDMSDKModel):
    name:                      Optional[str] = None
    reinstall_after_os_update: Optional[bool] = None
    profile_identifier:        Optional[str] = None
    user_scope:                Optional[bool] = None
    attribute_support:         Optional[bool] = None
    escape_attributes:         Optional[bool] = None
    group_count:               Optional[int] = None
    device_count:              Optional[int] = None


class DeviceProfileResponse(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: Optional[DeviceProfilesAttributes] = None


class DeviceProfilesListAllResponse(SimpleMDMSDKModel):
    data: list[DeviceProfileResponse]


class InstalledAppAttributes(SimpleMDMSDKModel):
    name:          Optional[str] = None
    identifier:    Optional[str] = None
    version:       Optional[str] = None
    short_version: Optional[str] = None
    bundle_size:   Optional[int] = None
    dynamic_size:  Optional[int] = None
    managed:       Optional[bool] = None
    discovered_at: Optional[str] = None
    last_seen_at:  Optional[str] = None


class InstalledAppResponse(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: InstalledAppAttributes


class InstalledAppsListAllResponse(SimpleMDMSDKModel):
    data: list[InstalledAppResponse]


class DeviceUserAttributes(SimpleMDMSDKModel):
    username:       Optional[str] = None
    full_name:      Optional[str] = None
    uid:            Optional[int] = None
    user_guid:      Optional[str] = None
    data_quota:     Optional[int] = None
    data_used:      Optional[int] = None
    data_to_sync:   Optional[bool] = None
    secure_token:   Optional[bool] = None
    logged_in:      Optional[bool] = None
    mobile_account: Optional[bool] = None



class DeviceUserResponse(SimpleMDMSDKModel):
    type:       str
    id:         int
    attributes: DeviceUserAttributes


class DeviceUsersListAllResponse(SimpleMDMSDKModel):
    data: list[DeviceUserResponse]