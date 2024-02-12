# Command


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_updates_to_client** | **bool** |  | [optional] 
**update_scheduled_task** | **bool** |  | [optional] [readonly] 
**completion_message** | **str** |  | [optional] [readonly] 
**requires_disk_access** | **bool** |  | [optional] [readonly] 
**is_exclusive** | **bool** |  | [optional] [readonly] 
**is_type_exclusive** | **bool** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**last_execution_time** | **datetime** |  | [optional] 
**last_start_time** | **datetime** |  | [optional] 
**trigger** | [**CommandTrigger**](CommandTrigger.md) |  | [optional] 
**suppress_messages** | **bool** |  | [optional] 
**client_user_agent** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.command import Command

# TODO update the JSON string below
json = "{}"
# create an instance of Command from a JSON string
command_instance = Command.from_json(json)
# print the JSON string representation of the object
print Command.to_json()

# convert the object into a dict
command_dict = command_instance.to_dict()
# create an instance of Command from a dict
command_form_dict = command.from_dict(command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


