# IndexerEditorResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexer_ids** | **List[int]** |  | [optional] 
**enable** | **bool** |  | [optional] 
**app_profile_id** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 

## Example

```python
from prowlarr.models.indexer_editor_resource import IndexerEditorResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerEditorResource from a JSON string
indexer_editor_resource_instance = IndexerEditorResource.from_json(json)
# print the JSON string representation of the object
print IndexerEditorResource.to_json()

# convert the object into a dict
indexer_editor_resource_dict = indexer_editor_resource_instance.to_dict()
# create an instance of IndexerEditorResource from a dict
indexer_editor_resource_form_dict = indexer_editor_resource.from_dict(indexer_editor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


