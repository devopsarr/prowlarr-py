# IndexerCapabilityResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**limits_max** | **int** |  | [optional] 
**limits_default** | **int** |  | [optional] 
**categories** | [**List[IndexerCategory]**](IndexerCategory.md) |  | [optional] 
**supports_raw_search** | **bool** |  | [optional] 
**search_params** | [**List[SearchParam]**](SearchParam.md) |  | [optional] 
**tv_search_params** | [**List[TvSearchParam]**](TvSearchParam.md) |  | [optional] 
**movie_search_params** | [**List[MovieSearchParam]**](MovieSearchParam.md) |  | [optional] 
**music_search_params** | [**List[MusicSearchParam]**](MusicSearchParam.md) |  | [optional] 
**book_search_params** | [**List[BookSearchParam]**](BookSearchParam.md) |  | [optional] 

## Example

```python
from prowlarr.models.indexer_capability_resource import IndexerCapabilityResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerCapabilityResource from a JSON string
indexer_capability_resource_instance = IndexerCapabilityResource.from_json(json)
# print the JSON string representation of the object
print(IndexerCapabilityResource.to_json())

# convert the object into a dict
indexer_capability_resource_dict = indexer_capability_resource_instance.to_dict()
# create an instance of IndexerCapabilityResource from a dict
indexer_capability_resource_form_dict = indexer_capability_resource.from_dict(indexer_capability_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


