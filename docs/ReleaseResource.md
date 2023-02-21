# ReleaseResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**guid** | **str** |  | [optional] 
**age** | **int** |  | [optional] 
**age_hours** | **float** |  | [optional] 
**age_minutes** | **float** |  | [optional] 
**size** | **int** |  | [optional] 
**files** | **int** |  | [optional] 
**grabs** | **int** |  | [optional] 
**indexer_id** | **int** |  | [optional] 
**indexer** | **str** |  | [optional] 
**sub_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**imdb_id** | **int** |  | [optional] 
**publish_date** | **datetime** |  | [optional] 
**comment_url** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**info_url** | **str** |  | [optional] 
**poster_url** | **str** |  | [optional] 
**indexer_flags** | **List[str]** |  | [optional] 
**categories** | [**List[IndexerCategory]**](IndexerCategory.md) |  | [optional] 
**magnet_url** | **str** |  | [optional] 
**info_hash** | **str** |  | [optional] 
**seeders** | **int** |  | [optional] 
**leechers** | **int** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**file_name** | **str** |  | [optional] [readonly] 

## Example

```python
from prowlarr.models.release_resource import ReleaseResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseResource from a JSON string
release_resource_instance = ReleaseResource.from_json(json)
# print the JSON string representation of the object
print ReleaseResource.to_json()

# convert the object into a dict
release_resource_dict = release_resource_instance.to_dict()
# create an instance of ReleaseResource from a dict
release_resource_form_dict = release_resource.from_dict(release_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


