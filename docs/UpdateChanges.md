# UpdateChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **List[str]** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 

## Example

```python
from prowlarr.models.update_changes import UpdateChanges

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChanges from a JSON string
update_changes_instance = UpdateChanges.from_json(json)
# print the JSON string representation of the object
print(UpdateChanges.to_json())

# convert the object into a dict
update_changes_dict = update_changes_instance.to_dict()
# create an instance of UpdateChanges from a dict
update_changes_from_dict = UpdateChanges.from_dict(update_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


