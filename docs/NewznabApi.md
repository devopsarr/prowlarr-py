# prowlarr.NewznabApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_indexerid_download**](NewznabApi.md#get_indexerid_download) | **GET** /api/v1/indexer/{id}/download | 
[**get_indexerid_newznab**](NewznabApi.md#get_indexerid_newznab) | **GET** /api/v1/indexer/{id}/newznab | 
[**getid_api**](NewznabApi.md#getid_api) | **GET** /{id}/api | 
[**getid_download**](NewznabApi.md#getid_download) | **GET** /{id}/download | 


# **get_indexerid_download**
> get_indexerid_download(id, link=link, file=file)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    link = 'link_example' # str |  (optional)
    file = 'file_example' # str |  (optional)

    try:
        api_instance.get_indexerid_download(id, link=link, file=file)
    except Exception as e:
        print("Exception when calling NewznabApi->get_indexerid_download: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    link = 'link_example' # str |  (optional)
    file = 'file_example' # str |  (optional)

    try:
        api_instance.get_indexerid_download(id, link=link, file=file)
    except Exception as e:
        print("Exception when calling NewznabApi->get_indexerid_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **link** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indexerid_newznab**
> get_indexerid_newznab(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    t = 't_example' # str |  (optional)
    q = 'q_example' # str |  (optional)
    cat = 'cat_example' # str |  (optional)
    imdbid = 'imdbid_example' # str |  (optional)
    tmdbid = 56 # int |  (optional)
    extended = 'extended_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    rid = 56 # int |  (optional)
    tvmazeid = 56 # int |  (optional)
    traktid = 56 # int |  (optional)
    tvdbid = 56 # int |  (optional)
    doubanid = 56 # int |  (optional)
    season = 56 # int |  (optional)
    ep = 'ep_example' # str |  (optional)
    album = 'album_example' # str |  (optional)
    artist = 'artist_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    track = 'track_example' # str |  (optional)
    year = 56 # int |  (optional)
    genre = 'genre_example' # str |  (optional)
    author = 'author_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    publisher = 'publisher_example' # str |  (optional)
    configured = 'configured_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    host = 'host_example' # str |  (optional)
    server = 'server_example' # str |  (optional)

    try:
        api_instance.get_indexerid_newznab(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)
    except Exception as e:
        print("Exception when calling NewznabApi->get_indexerid_newznab: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    t = 't_example' # str |  (optional)
    q = 'q_example' # str |  (optional)
    cat = 'cat_example' # str |  (optional)
    imdbid = 'imdbid_example' # str |  (optional)
    tmdbid = 56 # int |  (optional)
    extended = 'extended_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    rid = 56 # int |  (optional)
    tvmazeid = 56 # int |  (optional)
    traktid = 56 # int |  (optional)
    tvdbid = 56 # int |  (optional)
    doubanid = 56 # int |  (optional)
    season = 56 # int |  (optional)
    ep = 'ep_example' # str |  (optional)
    album = 'album_example' # str |  (optional)
    artist = 'artist_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    track = 'track_example' # str |  (optional)
    year = 56 # int |  (optional)
    genre = 'genre_example' # str |  (optional)
    author = 'author_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    publisher = 'publisher_example' # str |  (optional)
    configured = 'configured_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    host = 'host_example' # str |  (optional)
    server = 'server_example' # str |  (optional)

    try:
        api_instance.get_indexerid_newznab(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)
    except Exception as e:
        print("Exception when calling NewznabApi->get_indexerid_newznab: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **t** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **cat** | **str**|  | [optional] 
 **imdbid** | **str**|  | [optional] 
 **tmdbid** | **int**|  | [optional] 
 **extended** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **rid** | **int**|  | [optional] 
 **tvmazeid** | **int**|  | [optional] 
 **traktid** | **int**|  | [optional] 
 **tvdbid** | **int**|  | [optional] 
 **doubanid** | **int**|  | [optional] 
 **season** | **int**|  | [optional] 
 **ep** | **str**|  | [optional] 
 **album** | **str**|  | [optional] 
 **artist** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **track** | **str**|  | [optional] 
 **year** | **int**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **author** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **publisher** | **str**|  | [optional] 
 **configured** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **host** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getid_api**
> getid_api(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    t = 't_example' # str |  (optional)
    q = 'q_example' # str |  (optional)
    cat = 'cat_example' # str |  (optional)
    imdbid = 'imdbid_example' # str |  (optional)
    tmdbid = 56 # int |  (optional)
    extended = 'extended_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    rid = 56 # int |  (optional)
    tvmazeid = 56 # int |  (optional)
    traktid = 56 # int |  (optional)
    tvdbid = 56 # int |  (optional)
    doubanid = 56 # int |  (optional)
    season = 56 # int |  (optional)
    ep = 'ep_example' # str |  (optional)
    album = 'album_example' # str |  (optional)
    artist = 'artist_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    track = 'track_example' # str |  (optional)
    year = 56 # int |  (optional)
    genre = 'genre_example' # str |  (optional)
    author = 'author_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    publisher = 'publisher_example' # str |  (optional)
    configured = 'configured_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    host = 'host_example' # str |  (optional)
    server = 'server_example' # str |  (optional)

    try:
        api_instance.getid_api(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)
    except Exception as e:
        print("Exception when calling NewznabApi->getid_api: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    t = 't_example' # str |  (optional)
    q = 'q_example' # str |  (optional)
    cat = 'cat_example' # str |  (optional)
    imdbid = 'imdbid_example' # str |  (optional)
    tmdbid = 56 # int |  (optional)
    extended = 'extended_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    rid = 56 # int |  (optional)
    tvmazeid = 56 # int |  (optional)
    traktid = 56 # int |  (optional)
    tvdbid = 56 # int |  (optional)
    doubanid = 56 # int |  (optional)
    season = 56 # int |  (optional)
    ep = 'ep_example' # str |  (optional)
    album = 'album_example' # str |  (optional)
    artist = 'artist_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    track = 'track_example' # str |  (optional)
    year = 56 # int |  (optional)
    genre = 'genre_example' # str |  (optional)
    author = 'author_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    publisher = 'publisher_example' # str |  (optional)
    configured = 'configured_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    host = 'host_example' # str |  (optional)
    server = 'server_example' # str |  (optional)

    try:
        api_instance.getid_api(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)
    except Exception as e:
        print("Exception when calling NewznabApi->getid_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **t** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **cat** | **str**|  | [optional] 
 **imdbid** | **str**|  | [optional] 
 **tmdbid** | **int**|  | [optional] 
 **extended** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **rid** | **int**|  | [optional] 
 **tvmazeid** | **int**|  | [optional] 
 **traktid** | **int**|  | [optional] 
 **tvdbid** | **int**|  | [optional] 
 **doubanid** | **int**|  | [optional] 
 **season** | **int**|  | [optional] 
 **ep** | **str**|  | [optional] 
 **album** | **str**|  | [optional] 
 **artist** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **track** | **str**|  | [optional] 
 **year** | **int**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **author** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **publisher** | **str**|  | [optional] 
 **configured** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **host** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getid_download**
> getid_download(id, link=link, file=file)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    link = 'link_example' # str |  (optional)
    file = 'file_example' # str |  (optional)

    try:
        api_instance.getid_download(id, link=link, file=file)
    except Exception as e:
        print("Exception when calling NewznabApi->getid_download: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with prowlarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    link = 'link_example' # str |  (optional)
    file = 'file_example' # str |  (optional)

    try:
        api_instance.getid_download(id, link=link, file=file)
    except Exception as e:
        print("Exception when calling NewznabApi->getid_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **link** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

