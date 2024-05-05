# LogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**exception** | **str** |  | [optional] 
**exception_type** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**logger** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**method** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.log_resource import LogResource

# TODO update the JSON string below
json = "{}"
# create an instance of LogResource from a JSON string
log_resource_instance = LogResource.from_json(json)
# print the JSON string representation of the object
print(LogResource.to_json())

# convert the object into a dict
log_resource_dict = log_resource_instance.to_dict()
# create an instance of LogResource from a dict
log_resource_from_dict = LogResource.from_dict(log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


