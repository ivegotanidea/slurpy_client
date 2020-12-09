# slurpy_client.EmailApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email**](EmailApi.md#get_email) | **GET** /api/v1/email/mail/{email}/{password}/{folder}/{timeout} | Get Mail
[**get_inbox_folders**](EmailApi.md#get_inbox_folders) | **GET** /api/v1/email/folders/{email}/{password} | Get Folders
[**get_unseen**](EmailApi.md#get_unseen) | **GET** /api/v1/email/unseen/{email}/{password}/{limit} | Get Unseen


# **get_email**
> object get_email(email, password, folder, timeout)

Get Mail

Get email

### Example

```python
from __future__ import print_function
import time
import slurpy_client
from slurpy_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with slurpy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = slurpy_client.EmailApi(api_client)
    email = 'email_example' # str | 
password = 'password_example' # str | 
folder = 'folder_example' # str | 
timeout = 56 # int | 

    try:
        # Get Mail
        api_response = api_instance.get_email(email, password, folder, timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailApi->get_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **password** | **str**|  | 
 **folder** | **str**|  | 
 **timeout** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_folders**
> object get_inbox_folders(email, password)

Get Folders

Get inbox folders

### Example

```python
from __future__ import print_function
import time
import slurpy_client
from slurpy_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with slurpy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = slurpy_client.EmailApi(api_client)
    email = 'email_example' # str | 
password = 'password_example' # str | 

    try:
        # Get Folders
        api_response = api_instance.get_inbox_folders(email, password)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailApi->get_inbox_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **password** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unseen**
> object get_unseen(email, password, limit)

Get Unseen

Get unseen email

### Example

```python
from __future__ import print_function
import time
import slurpy_client
from slurpy_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with slurpy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = slurpy_client.EmailApi(api_client)
    email = 'email_example' # str | 
password = 'password_example' # str | 
limit = 56 # int | 

    try:
        # Get Unseen
        api_response = api_instance.get_unseen(email, password, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailApi->get_unseen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **password** | **str**|  | 
 **limit** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

