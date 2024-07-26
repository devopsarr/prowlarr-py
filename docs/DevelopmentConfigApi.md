# prowlarr.DevelopmentConfigApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_development_config**](DevelopmentConfigApi.md#get_development_config) | **GET** /api/v1/config/development | 
[**get_development_config_by_id**](DevelopmentConfigApi.md#get_development_config_by_id) | **GET** /api/v1/config/development/{id} | 
[**update_development_config**](DevelopmentConfigApi.md#update_development_config) | **PUT** /api/v1/config/development/{id} | 


# **get_development_config**
> DevelopmentConfigResource get_development_config()



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.development_config_resource import DevelopmentConfigResource
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
    api_instance = prowlarr.DevelopmentConfigApi(api_client)

    try:
        api_response = api_instance.get_development_config()
        print("The response of DevelopmentConfigApi->get_development_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopmentConfigApi->get_development_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DevelopmentConfigResource**](DevelopmentConfigResource.md)

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

# **get_development_config_by_id**
> DevelopmentConfigResource get_development_config_by_id(id)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.development_config_resource import DevelopmentConfigResource
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
    api_instance = prowlarr.DevelopmentConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_development_config_by_id(id)
        print("The response of DevelopmentConfigApi->get_development_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopmentConfigApi->get_development_config_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DevelopmentConfigResource**](DevelopmentConfigResource.md)

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

# **update_development_config**
> DevelopmentConfigResource update_development_config(id, development_config_resource=development_config_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.development_config_resource import DevelopmentConfigResource
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
    api_instance = prowlarr.DevelopmentConfigApi(api_client)
    id = 'id_example' # str | 
    development_config_resource = prowlarr.DevelopmentConfigResource() # DevelopmentConfigResource |  (optional)

    try:
        api_response = api_instance.update_development_config(id, development_config_resource=development_config_resource)
        print("The response of DevelopmentConfigApi->update_development_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopmentConfigApi->update_development_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **development_config_resource** | [**DevelopmentConfigResource**](DevelopmentConfigResource.md)|  | [optional] 

### Return type

[**DevelopmentConfigResource**](DevelopmentConfigResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

