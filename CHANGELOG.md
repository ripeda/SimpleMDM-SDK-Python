# SimpleMDM SDK Python CHANGELOG

### 0.1.0
- Add search parameters to `SimpleMDM.devices.list_all()`
- Resolve error in PATCH method for `_connection.py`.
- Resolve `include_shared` error in `SimpleMDM.apps.list_all()`.
- Resolve `variable_support` error in `SimpleMDM.scripts.list_all()`.
- Resolve `managed_app_configs.py` URL error.
- Resolve `script_jobs.py`'s `create` method failing to build array of identifiers.
- Set `User-Agent` header to `SimpleMDM-SDK-Python / {version}`.
- Set `Accept` header to `application/json, application/x-plist`
- Set `Content-Type` header to `application/json`

### 0.0.1
- Initial alpha release.