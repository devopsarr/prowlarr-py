# TaskResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**task_name** | **str** |  | [optional] 
**interval** | **int** |  | [optional] 
**last_execution** | **datetime** |  | [optional] 
**last_start_time** | **datetime** |  | [optional] 
**next_execution** | **datetime** |  | [optional] 
**last_duration** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.task_resource import TaskResource

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResource from a JSON string
task_resource_instance = TaskResource.from_json(json)
# print the JSON string representation of the object
print(TaskResource.to_json())

# convert the object into a dict
task_resource_dict = task_resource_instance.to_dict()
# create an instance of TaskResource from a dict
task_resource_from_dict = TaskResource.from_dict(task_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


