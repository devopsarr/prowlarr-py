# CommandResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**command_name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**body** | [**Command**](Command.md) |  | [optional] 
**priority** | [**CommandPriority**](CommandPriority.md) |  | [optional] 
**status** | [**CommandStatus**](CommandStatus.md) |  | [optional] 
**queued** | **datetime** |  | [optional] 
**started** | **datetime** |  | [optional] 
**ended** | **datetime** |  | [optional] 
**duration** | **str** |  | [optional] 
**exception** | **str** |  | [optional] 
**trigger** | [**CommandTrigger**](CommandTrigger.md) |  | [optional] 
**client_user_agent** | **str** |  | [optional] 
**state_change_time** | **datetime** |  | [optional] 
**send_updates_to_client** | **bool** |  | [optional] 
**update_scheduled_task** | **bool** |  | [optional] 
**last_execution_time** | **datetime** |  | [optional] 

## Example

```python
from prowlarr.models.command_resource import CommandResource

# TODO update the JSON string below
json = "{}"
# create an instance of CommandResource from a JSON string
command_resource_instance = CommandResource.from_json(json)
# print the JSON string representation of the object
print CommandResource.to_json()

# convert the object into a dict
command_resource_dict = command_resource_instance.to_dict()
# create an instance of CommandResource from a dict
command_resource_form_dict = command_resource.from_dict(command_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


