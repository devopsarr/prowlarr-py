# ApiInfoResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **str** |  | [optional] 
**deprecated** | **List[str]** |  | [optional] 

## Example

```python
from prowlarr.models.api_info_resource import ApiInfoResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoResource from a JSON string
api_info_resource_instance = ApiInfoResource.from_json(json)
# print the JSON string representation of the object
print ApiInfoResource.to_json()

# convert the object into a dict
api_info_resource_dict = api_info_resource_instance.to_dict()
# create an instance of ApiInfoResource from a dict
api_info_resource_form_dict = api_info_resource.from_dict(api_info_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


