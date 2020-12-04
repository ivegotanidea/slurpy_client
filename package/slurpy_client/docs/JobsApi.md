# slurpy_client.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_result**](JobsApi.md#get_job_result) | **GET** /api/v1.0/job/{job_id} | Get Job Result


# **get_job_result**
> bool, date, datetime, dict, float, int, list, str, none_type get_job_result(job_id)

Get Job Result

Get job status and result by its id

### Example

```python
import time
import slurpy_client
from slurpy_client.api import jobs_api
from slurpy_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with slurpy_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = "job_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Job Result
        api_response = api_instance.get_job_result(job_id)
        pprint(api_response)
    except slurpy_client.ApiException as e:
        print("Exception when calling JobsApi->get_job_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

