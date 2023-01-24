# LogFileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**filename** | **str** |  | [optional] 
**last_write_time** | **datetime** |  | [optional] 
**contents_url** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.log_file_resource import LogFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of LogFileResource from a JSON string
log_file_resource_instance = LogFileResource.from_json(json)
# print the JSON string representation of the object
print LogFileResource.to_json()

# convert the object into a dict
log_file_resource_dict = log_file_resource_instance.to_dict()
# create an instance of LogFileResource from a dict
log_file_resource_form_dict = log_file_resource.from_dict(log_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


