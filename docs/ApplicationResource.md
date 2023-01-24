# ApplicationResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[Field]**](Field.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[ApplicationResource]**](ApplicationResource.md) |  | [optional] 
**sync_level** | [**ApplicationSyncLevel**](ApplicationSyncLevel.md) |  | [optional] 
**test_command** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.application_resource import ApplicationResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResource from a JSON string
application_resource_instance = ApplicationResource.from_json(json)
# print the JSON string representation of the object
print ApplicationResource.to_json()

# convert the object into a dict
application_resource_dict = application_resource_instance.to_dict()
# create an instance of ApplicationResource from a dict
application_resource_form_dict = application_resource.from_dict(application_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


