# BackupResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**type** | [**BackupType**](BackupType.md) |  | [optional] 
**size** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from prowlarr.models.backup_resource import BackupResource

# TODO update the JSON string below
json = "{}"
# create an instance of BackupResource from a JSON string
backup_resource_instance = BackupResource.from_json(json)
# print the JSON string representation of the object
print BackupResource.to_json()

# convert the object into a dict
backup_resource_dict = backup_resource_instance.to_dict()
# create an instance of BackupResource from a dict
backup_resource_form_dict = backup_resource.from_dict(backup_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


