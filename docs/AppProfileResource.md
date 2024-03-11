# AppProfileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**enable_rss** | **bool** |  | [optional] 
**enable_automatic_search** | **bool** |  | [optional] 
**enable_interactive_search** | **bool** |  | [optional] 
**minimum_seeders** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.app_profile_resource import AppProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of AppProfileResource from a JSON string
app_profile_resource_instance = AppProfileResource.from_json(json)
# print the JSON string representation of the object
print(AppProfileResource.to_json())

# convert the object into a dict
app_profile_resource_dict = app_profile_resource_instance.to_dict()
# create an instance of AppProfileResource from a dict
app_profile_resource_form_dict = app_profile_resource.from_dict(app_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


