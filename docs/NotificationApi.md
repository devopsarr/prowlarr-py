# prowlarr.NotificationApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationApi.md#create_notification) | **POST** /api/v1/notification | 
[**create_notification_action_by_name**](NotificationApi.md#create_notification_action_by_name) | **POST** /api/v1/notification/action/{name} | 
[**delete_notification**](NotificationApi.md#delete_notification) | **DELETE** /api/v1/notification/{id} | 
[**get_notification_by_id**](NotificationApi.md#get_notification_by_id) | **GET** /api/v1/notification/{id} | 
[**list_notification**](NotificationApi.md#list_notification) | **GET** /api/v1/notification | 
[**list_notification_schema**](NotificationApi.md#list_notification_schema) | **GET** /api/v1/notification/schema | 
[**test_notification**](NotificationApi.md#test_notification) | **POST** /api/v1/notification/test | 
[**testall_notification**](NotificationApi.md#testall_notification) | **POST** /api/v1/notification/testall | 
[**update_notification**](NotificationApi.md#update_notification) | **PUT** /api/v1/notification/{id} | 


# **create_notification**
> NotificationResource create_notification(force_save=force_save, notification_resource=notification_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)
    force_save = False # bool |  (optional) (default to False)
    notification_resource = prowlarr.NotificationResource() # NotificationResource |  (optional)

    try:
        api_response = api_instance.create_notification(force_save=force_save, notification_resource=notification_resource)
        print("The response of NotificationApi->create_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->create_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_save** | **bool**|  | [optional] [default to False]
 **notification_resource** | [**NotificationResource**](NotificationResource.md)|  | [optional] 

### Return type

[**NotificationResource**](NotificationResource.md)

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

# **create_notification_action_by_name**
> create_notification_action_by_name(name, notification_resource=notification_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)
    name = 'name_example' # str | 
    notification_resource = prowlarr.NotificationResource() # NotificationResource |  (optional)

    try:
        api_instance.create_notification_action_by_name(name, notification_resource=notification_resource)
    except Exception as e:
        print("Exception when calling NotificationApi->create_notification_action_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **notification_resource** | [**NotificationResource**](NotificationResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> delete_notification(id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
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
    api_instance = prowlarr.NotificationApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_notification(id)
    except Exception as e:
        print("Exception when calling NotificationApi->delete_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_by_id**
> NotificationResource get_notification_by_id(id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_notification_by_id(id)
        print("The response of NotificationApi->get_notification_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->get_notification_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NotificationResource**](NotificationResource.md)

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

# **list_notification**
> List[NotificationResource] list_notification()

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)

    try:
        api_response = api_instance.list_notification()
        print("The response of NotificationApi->list_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->list_notification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NotificationResource]**](NotificationResource.md)

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

# **list_notification_schema**
> List[NotificationResource] list_notification_schema()

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)

    try:
        api_response = api_instance.list_notification_schema()
        print("The response of NotificationApi->list_notification_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->list_notification_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NotificationResource]**](NotificationResource.md)

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

# **test_notification**
> test_notification(force_test=force_test, notification_resource=notification_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)
    force_test = False # bool |  (optional) (default to False)
    notification_resource = prowlarr.NotificationResource() # NotificationResource |  (optional)

    try:
        api_instance.test_notification(force_test=force_test, notification_resource=notification_resource)
    except Exception as e:
        print("Exception when calling NotificationApi->test_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_test** | **bool**|  | [optional] [default to False]
 **notification_resource** | [**NotificationResource**](NotificationResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testall_notification**
> testall_notification()

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
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
    api_instance = prowlarr.NotificationApi(api_client)

    try:
        api_instance.testall_notification()
    except Exception as e:
        print("Exception when calling NotificationApi->testall_notification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> NotificationResource update_notification(id, force_save=force_save, notification_resource=notification_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.notification_resource import NotificationResource
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
    api_instance = prowlarr.NotificationApi(api_client)
    id = 'id_example' # str | 
    force_save = False # bool |  (optional) (default to False)
    notification_resource = prowlarr.NotificationResource() # NotificationResource |  (optional)

    try:
        api_response = api_instance.update_notification(id, force_save=force_save, notification_resource=notification_resource)
        print("The response of NotificationApi->update_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->update_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **force_save** | **bool**|  | [optional] [default to False]
 **notification_resource** | [**NotificationResource**](NotificationResource.md)|  | [optional] 

### Return type

[**NotificationResource**](NotificationResource.md)

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

