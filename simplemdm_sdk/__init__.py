"""
SimpleMDM SDK for Python

Library usage:
   >>> from simplemdm_sdk import SimpleMDM

   >>> simplemdm_obj = SimpleMDM("your_api_key")
   >>> devices = simplemdm_obj.devices.list_all()
   >>> print(devices.data[0].attributes.name)
"""

from ._simplemdm import SimpleMDM


__title__:        str = "simplemdm_sdk"
__version__:      str = "0.1.0"
__description__:  str = "Highly opinionated SimpleMDM Python library"
__url__:          str = "https://github.com/ripeda/SimpleMDM-SDK-Python"
__author__:       str = "RIPEDA Consulting"
__author_email__: str = "info@ripeda.com"
__status__:       str = "Beta"
__license__:      str = "BSD 3-Clause License"
__all__:         list = ["SimpleMDM"]