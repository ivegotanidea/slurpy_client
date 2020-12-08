"""
    Slurpy

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "slurpy_client"
VERSION = ""
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.15",
  "certifi",
  "python-dateutil",
  "nulltype",
]

setup(
    name=NAME,
    version=VERSION,
    description="Slurpy",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/ivegotanidea/slurpy_client",
    keywords=["OpenAPI", "OpenAPI-Generator", "Slurpy"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501
    """
)
