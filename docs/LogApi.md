# prowlarr.LogApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log**](LogApi.md#get_log) | **GET** /api/v1/log | 


# **get_log**
> LogResourcePagingResource get_log(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, level=level)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.log_resource_paging_resource import LogResourcePagingResource
from prowlarr.models.sort_direction import SortDirection
from prowlarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9696
# See configuration.py for a list of all supported configuration parameters.
configuration = prowlarr.Configuration(
    host = "http://localhost:9696"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.LogApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    sort_key = 'sort_key_example' # str |  (optional)
    sort_direction = prowlarr.SortDirection() # SortDirection |  (optional)
    level = 'level_example' # str |  (optional)

    try:
        api_response = api_instance.get_log(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, level=level)
        print("The response of LogApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogApi->get_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **sort_key** | **str**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **level** | **str**|  | [optional] 

### Return type

[**LogResourcePagingResource**](LogResourcePagingResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

