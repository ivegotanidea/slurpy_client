# slurpy_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.6
- Package version: 1.0.6
- Build date: 2020-12-09T07:47:15.215Z[GMT]
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import slurpy_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import slurpy_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import slurpy_client
from pprint import pprint
from slurpy_client.api import email_api
from slurpy_client.model.http_validation_error import HTTPValidationError
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with slurpy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)
    email = "email_example" # str | 
password = "password_example" # str | 
folder = "folder_example" # str | 
timeout = 1 # int | 

    try:
        # Get Mail
        api_response = api_instance.get_email(email, password, folder, timeout)
        pprint(api_response)
    except slurpy_client.ApiException as e:
        print("Exception when calling EmailApi->get_email: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EmailApi* | [**get_email**](docs/EmailApi.md#get_email) | **GET** /api/v1/email/mail/{email}/{password}/{folder}/{timeout} | Get Mail
*EmailApi* | [**get_inbox_folders**](docs/EmailApi.md#get_inbox_folders) | **GET** /api/v1/email/folders/{email}/{password} | Get Folders
*EmailApi* | [**get_unseen**](docs/EmailApi.md#get_unseen) | **GET** /api/v1/email/unseen/{email}/{password}/{limit} | Get Unseen
*InboxApi* | [**create_inbox**](docs/InboxApi.md#create_inbox) | **POST** /api/v1/inbox/{email}/{password} | Create Inbox
*InboxApi* | [**create_random_inbox**](docs/InboxApi.md#create_random_inbox) | **POST** /api/v1/inbox/ | Create Random Inbox
*InboxApi* | [**get_inboxes_list**](docs/InboxApi.md#get_inboxes_list) | **GET** /api/v1/inbox/inboxes | Get Inboxes
*JobsApi* | [**get_job_result**](docs/JobsApi.md#get_job_result) | **GET** /api/v1/job/{job_id} | Get Job Result


## Documentation For Models

 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [ValidationError](docs/ValidationError.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in slurpy_client.apis and slurpy_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from slurpy_client.api.default_api import DefaultApi`
- `from slurpy_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import slurpy_client
from slurpy_client.apis import *
from slurpy_client.models import *
```

