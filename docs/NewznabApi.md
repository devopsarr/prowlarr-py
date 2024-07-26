# prowlarr.NewznabApi

All URIs are relative to *http://localhost:9696*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_indexer_download**](NewznabApi.md#get_indexer_download) | **GET** /api/v1/indexer/{id}/download | 
[**get_indexer_newznab**](NewznabApi.md#get_indexer_newznab) | **GET** /api/v1/indexer/{id}/newznab | 


# **get_indexer_download**
> get_indexer_download(id, link=link, file=file)



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
    api_instance = prowlarr.NewznabApi(api_client)
    id = 56 # int | 
    link = 'link_example' # str |  (optional)
    file = 'file_example' # str |  (optional)

    try:
        api_instance.get_indexer_download(id, link=link, file=file)
    except Exception as e:
        print("Exception when calling NewznabApi->get_indexer_download: %s\n" % e)
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

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indexer_newznab**
> get_indexer_newznab(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, minage=minage, maxage=maxage, minsize=minsize, maxsize=maxsize, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)



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
    minage = 56 # int |  (optional)
    maxage = 56 # int |  (optional)
    minsize = 56 # int |  (optional)
    maxsize = 56 # int |  (optional)
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
        api_instance.get_indexer_newznab(id, t=t, q=q, cat=cat, imdbid=imdbid, tmdbid=tmdbid, extended=extended, limit=limit, offset=offset, minage=minage, maxage=maxage, minsize=minsize, maxsize=maxsize, rid=rid, tvmazeid=tvmazeid, traktid=traktid, tvdbid=tvdbid, doubanid=doubanid, season=season, ep=ep, album=album, artist=artist, label=label, track=track, year=year, genre=genre, author=author, title=title, publisher=publisher, configured=configured, source=source, host=host, server=server)
    except Exception as e:
        print("Exception when calling NewznabApi->get_indexer_newznab: %s\n" % e)
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
 **minage** | **int**|  | [optional] 
 **maxage** | **int**|  | [optional] 
 **minsize** | **int**|  | [optional] 
 **maxsize** | **int**|  | [optional] 
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

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

