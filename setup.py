from setuptools import setup, find_packages

def fetch_property(property: str) -> str:
    """
    Fetch a property from simplemdm_sdk.
    """
    for line in open("simplemdm_sdk/__init__.py", "r").readlines():
        if not line.startswith(property):
            continue
        return line.split("=")[1].strip().strip('"')
    raise ValueError(f"Property {property} not found.")


setup(
    name='simplemdm_sdk',
    version=fetch_property("__version__:"),
    description=fetch_property("__description__:"),
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    author_email=fetch_property("__author_email__:"),
    author=fetch_property("__author__:"),
    license=fetch_property("__license__:"),
    url=fetch_property("__url__:"),
    python_requires='>=3.6',
    install_requires=open("requirements.txt", "r").readlines(),
    packages=find_packages(include=["simplemdm_sdk", "simplemdm_sdk.*"]),
    package_data={
        "simplemdm_sdk": ["*"],
        "simplemdm_sdk._rest_api_endpoints": ["*"],
        "simplemdm_sdk._rest_api_endpoints.models": ["*"],
    },
    py_modules=["simplemdm_sdk"],
)