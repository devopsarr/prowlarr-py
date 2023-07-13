# IndexerBulkResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**app_profile_id** | **int** |  | [optional] 
**priority** | **int** |  | [optional] 
**minimum_seeders** | **int** |  | [optional] 
**seed_ratio** | **float** |  | [optional] 
**seed_time** | **int** |  | [optional] 
**pack_seed_time** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.indexer_bulk_resource import IndexerBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerBulkResource from a JSON string
indexer_bulk_resource_instance = IndexerBulkResource.from_json(json)
# print the JSON string representation of the object
print IndexerBulkResource.to_json()

# convert the object into a dict
indexer_bulk_resource_dict = indexer_bulk_resource_instance.to_dict()
# create an instance of IndexerBulkResource from a dict
indexer_bulk_resource_form_dict = indexer_bulk_resource.from_dict(indexer_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


