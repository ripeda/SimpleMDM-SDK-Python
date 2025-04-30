# SimpleMDM SDK Python

Python library for interacting with SimpleMDM's REST API. Pseudo-spiritual successor to SteveKueng/MacAdmin's [SimpleMDMpy](https://github.com/macadmins/simpleMDMpy).

Note: Library is highly opinionated and may not be suitable for all use cases. Use at your own discretion.


## Notable differences from SimpleMDMpy

- Implicit conversion of parameters to strings when generating URLs.
  - ex. Passing device IDs as integers will no longer raises an error.
- Single public class for all API endpoints
  - No need to pass API keys to individual endpoint classes.
- Feature parity with SimpleMDM's API.
  - Currently validated against version 1.51.
- Function names matching SimpleMDM's API.
  - ex. `SimpleMDM.Accounts.show()` instead of `SimpleMDM.Accounts.get_account()`.
  - Easier referencing of SimpleMDM's API documentation.
- Pydantic models for API responses.
  - Provides type hints and validation for API responses.
  - Configure strictness of validation with `os.environ["SimpleMDMSDKModelExtra"] = "xxx"` before importing the library.
- Automatic ratelimit handling for all REST methods.
- Enums for static properties in function parameters.
  - ex. `SimpleMDM.AssignmentGroups.MunkiInstallType` instead of strings.


## Usage

```py
from simplemdm_sdk import SimpleMDM

api_key = "your_api_key"
simplemdm = SimpleMDM(api_key)

# List all devices
devices = simplemdm.devices.list_all()
print(devices)
```