# prowlarr.ApplicationApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_applications**](ApplicationApi.md#create_applications) | **POST** /api/v1/applications | 
[**create_applications_action_by_name**](ApplicationApi.md#create_applications_action_by_name) | **POST** /api/v1/applications/action/{name} | 
[**delete_applications**](ApplicationApi.md#delete_applications) | **DELETE** /api/v1/applications/{id} | 
[**delete_applications_bulk**](ApplicationApi.md#delete_applications_bulk) | **DELETE** /api/v1/applications/bulk | 
[**get_applications_by_id**](ApplicationApi.md#get_applications_by_id) | **GET** /api/v1/applications/{id} | 
[**list_applications**](ApplicationApi.md#list_applications) | **GET** /api/v1/applications | 
[**list_applications_schema**](ApplicationApi.md#list_applications_schema) | **GET** /api/v1/applications/schema | 
[**put_applications_bulk**](ApplicationApi.md#put_applications_bulk) | **PUT** /api/v1/applications/bulk | 
[**test_applications**](ApplicationApi.md#test_applications) | **POST** /api/v1/applications/test | 
[**testall_applications**](ApplicationApi.md#testall_applications) | **POST** /api/v1/applications/testall | 
[**update_applications**](ApplicationApi.md#update_applications) | **PUT** /api/v1/applications/{id} | 


# **create_applications**
> ApplicationResource create_applications(force_save=force_save, application_resource=application_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    force_save = False # bool |  (optional) (default to False)
    application_resource = prowlarr.ApplicationResource() # ApplicationResource |  (optional)

    try:
        api_response = api_instance.create_applications(force_save=force_save, application_resource=application_resource)
        print("The response of ApplicationApi->create_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->create_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_save** | **bool**|  | [optional] [default to False]
 **application_resource** | [**ApplicationResource**](ApplicationResource.md)|  | [optional] 

### Return type

[**ApplicationResource**](ApplicationResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_applications_action_by_name**
> create_applications_action_by_name(name, application_resource=application_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    name = 'name_example' # str | 
    application_resource = prowlarr.ApplicationResource() # ApplicationResource |  (optional)

    try:
        api_instance.create_applications_action_by_name(name, application_resource=application_resource)
    except Exception as e:
        print("Exception when calling ApplicationApi->create_applications_action_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **application_resource** | [**ApplicationResource**](ApplicationResource.md)|  | [optional] 

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
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_applications**
> delete_applications(id)



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
    api_instance = prowlarr.ApplicationApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_applications(id)
    except Exception as e:
        print("Exception when calling ApplicationApi->delete_applications: %s\n" % e)
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
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_applications_bulk**
> delete_applications_bulk(application_bulk_resource=application_bulk_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_bulk_resource import ApplicationBulkResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    application_bulk_resource = prowlarr.ApplicationBulkResource() # ApplicationBulkResource |  (optional)

    try:
        api_instance.delete_applications_bulk(application_bulk_resource=application_bulk_resource)
    except Exception as e:
        print("Exception when calling ApplicationApi->delete_applications_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_bulk_resource** | [**ApplicationBulkResource**](ApplicationBulkResource.md)|  | [optional] 

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
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_by_id**
> ApplicationResource get_applications_by_id(id)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_applications_by_id(id)
        print("The response of ApplicationApi->get_applications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->get_applications_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApplicationResource**](ApplicationResource.md)

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

# **list_applications**
> List[ApplicationResource] list_applications()



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)

    try:
        api_response = api_instance.list_applications()
        print("The response of ApplicationApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->list_applications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApplicationResource]**](ApplicationResource.md)

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

# **list_applications_schema**
> List[ApplicationResource] list_applications_schema()



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)

    try:
        api_response = api_instance.list_applications_schema()
        print("The response of ApplicationApi->list_applications_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->list_applications_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApplicationResource]**](ApplicationResource.md)

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

# **put_applications_bulk**
> ApplicationResource put_applications_bulk(application_bulk_resource=application_bulk_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_bulk_resource import ApplicationBulkResource
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    application_bulk_resource = prowlarr.ApplicationBulkResource() # ApplicationBulkResource |  (optional)

    try:
        api_response = api_instance.put_applications_bulk(application_bulk_resource=application_bulk_resource)
        print("The response of ApplicationApi->put_applications_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->put_applications_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_bulk_resource** | [**ApplicationBulkResource**](ApplicationBulkResource.md)|  | [optional] 

### Return type

[**ApplicationResource**](ApplicationResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_applications**
> test_applications(application_resource=application_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    application_resource = prowlarr.ApplicationResource() # ApplicationResource |  (optional)

    try:
        api_instance.test_applications(application_resource=application_resource)
    except Exception as e:
        print("Exception when calling ApplicationApi->test_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_resource** | [**ApplicationResource**](ApplicationResource.md)|  | [optional] 

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
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testall_applications**
> testall_applications()



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
    api_instance = prowlarr.ApplicationApi(api_client)

    try:
        api_instance.testall_applications()
    except Exception as e:
        print("Exception when calling ApplicationApi->testall_applications: %s\n" % e)
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
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_applications**
> ApplicationResource update_applications(id, force_save=force_save, application_resource=application_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import prowlarr
from prowlarr.models.application_resource import ApplicationResource
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
    api_instance = prowlarr.ApplicationApi(api_client)
    id = 'id_example' # str | 
    force_save = False # bool |  (optional) (default to False)
    application_resource = prowlarr.ApplicationResource() # ApplicationResource |  (optional)

    try:
        api_response = api_instance.update_applications(id, force_save=force_save, application_resource=application_resource)
        print("The response of ApplicationApi->update_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->update_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **force_save** | **bool**|  | [optional] [default to False]
 **application_resource** | [**ApplicationResource**](ApplicationResource.md)|  | [optional] 

### Return type

[**ApplicationResource**](ApplicationResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

