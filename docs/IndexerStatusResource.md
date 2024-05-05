# IndexerStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**indexer_id** | **int** |  | [optional] 
**disabled_till** | **datetime** |  | [optional] 
**most_recent_failure** | **datetime** |  | [optional] 
**initial_failure** | **datetime** |  | [optional] 

## Example

```python
from prowlarr.models.indexer_status_resource import IndexerStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerStatusResource from a JSON string
indexer_status_resource_instance = IndexerStatusResource.from_json(json)
# print the JSON string representation of the object
print(IndexerStatusResource.to_json())

# convert the object into a dict
indexer_status_resource_dict = indexer_status_resource_instance.to_dict()
# create an instance of IndexerStatusResource from a dict
indexer_status_resource_from_dict = IndexerStatusResource.from_dict(indexer_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


