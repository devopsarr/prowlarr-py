# prowlarr.HistoryApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_history**](HistoryApi.md#get_history) | **GET** /api/v1/history | 
[**list_history_indexer**](HistoryApi.md#list_history_indexer) | **GET** /api/v1/history/indexer | 
[**list_history_since**](HistoryApi.md#list_history_since) | **GET** /api/v1/history/since | 


# **get_history**
> HistoryResourcePagingResource get_history(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, event_type=event_type, successful=successful, download_id=download_id, indexer_ids=indexer_ids)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.history_resource_paging_resource import HistoryResourcePagingResource
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
    api_instance = prowlarr.HistoryApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    sort_key = 'sort_key_example' # str |  (optional)
    sort_direction = prowlarr.SortDirection() # SortDirection |  (optional)
    event_type = [56] # List[int] |  (optional)
    successful = True # bool |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    indexer_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.get_history(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, event_type=event_type, successful=successful, download_id=download_id, indexer_ids=indexer_ids)
        print("The response of HistoryApi->get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **sort_key** | **str**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **event_type** | [**List[int]**](int.md)|  | [optional] 
 **successful** | **bool**|  | [optional] 
 **download_id** | **str**|  | [optional] 
 **indexer_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**HistoryResourcePagingResource**](HistoryResourcePagingResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_history_indexer**
> List[HistoryResource] list_history_indexer(indexer_id=indexer_id, event_type=event_type, limit=limit)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.history_event_type import HistoryEventType
from prowlarr.models.history_resource import HistoryResource
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
    api_instance = prowlarr.HistoryApi(api_client)
    indexer_id = 56 # int |  (optional)
    event_type = prowlarr.HistoryEventType() # HistoryEventType |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.list_history_indexer(indexer_id=indexer_id, event_type=event_type, limit=limit)
        print("The response of HistoryApi->list_history_indexer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->list_history_indexer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexer_id** | **int**|  | [optional] 
 **event_type** | [**HistoryEventType**](.md)|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**List[HistoryResource]**](HistoryResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_history_since**
> List[HistoryResource] list_history_since(var_date=var_date, event_type=event_type)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.history_event_type import HistoryEventType
from prowlarr.models.history_resource import HistoryResource
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
    api_instance = prowlarr.HistoryApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    event_type = prowlarr.HistoryEventType() # HistoryEventType |  (optional)

    try:
        api_response = api_instance.list_history_since(var_date=var_date, event_type=event_type)
        print("The response of HistoryApi->list_history_since:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->list_history_since: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**|  | [optional] 
 **event_type** | [**HistoryEventType**](.md)|  | [optional] 

### Return type

[**List[HistoryResource]**](HistoryResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

