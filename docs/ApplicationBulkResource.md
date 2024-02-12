# ApplicationBulkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**sync_level** | [**ApplicationSyncLevel**](ApplicationSyncLevel.md) |  | [optional] 

## Example

```python
from prowlarr.models.application_bulk_resource import ApplicationBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationBulkResource from a JSON string
application_bulk_resource_instance = ApplicationBulkResource.from_json(json)
# print the JSON string representation of the object
print ApplicationBulkResource.to_json()

# convert the object into a dict
application_bulk_resource_dict = application_bulk_resource_instance.to_dict()
# create an instance of ApplicationBulkResource from a dict
application_bulk_resource_form_dict = application_bulk_resource.from_dict(application_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


