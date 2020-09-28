# slurpy_client.InboxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inbox**](InboxApi.md#create_inbox) | **POST** /api/v1.0/inbox/{email}/{password} | Create Inbox
[**create_random_inbox**](InboxApi.md#create_random_inbox) | **POST** /api/v1.0/inbox/ | Create Random Inbox
[**get_inboxes_list**](InboxApi.md#get_inboxes_list) | **GET** /api/v1.0/inbox/inboxes | Get Inboxes


# **create_inbox**
> object create_inbox(email, password)

Create Inbox

Create inbox with specified credentials

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
    api_instance = slurpy_client.InboxApi(api_client)
    email = 'email_example' # str | 
password = 'password_example' # str | 

    try:
        # Create Inbox
        api_response = api_instance.create_inbox(email, password)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxApi->create_inbox: %s\n" % e)
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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_random_inbox**
> object create_random_inbox()

Create Random Inbox

Create inbox with random credentials

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
    api_instance = slurpy_client.InboxApi(api_client)
    
    try:
        # Create Random Inbox
        api_response = api_instance.create_random_inbox()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxApi->create_random_inbox: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**201** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inboxes_list**
> object get_inboxes_list()

Get Inboxes

Get list of created inboxes

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
    api_instance = slurpy_client.InboxApi(api_client)
    
    try:
        # Get Inboxes
        api_response = api_instance.get_inboxes_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxApi->get_inboxes_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

