# CustomFilterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**filters** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from prowlarr.models.custom_filter_resource import CustomFilterResource

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFilterResource from a JSON string
custom_filter_resource_instance = CustomFilterResource.from_json(json)
# print the JSON string representation of the object
print(CustomFilterResource.to_json())

# convert the object into a dict
custom_filter_resource_dict = custom_filter_resource_instance.to_dict()
# create an instance of CustomFilterResource from a dict
custom_filter_resource_form_dict = custom_filter_resource.from_dict(custom_filter_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


