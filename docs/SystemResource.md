# SystemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**instance_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**build_time** | **datetime** |  | [optional] 
**is_debug** | **bool** |  | [optional] 
**is_production** | **bool** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**is_user_interactive** | **bool** |  | [optional] 
**startup_path** | **str** |  | [optional] 
**app_data** | **str** |  | [optional] 
**os_name** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**is_net_core** | **bool** |  | [optional] 
**is_linux** | **bool** |  | [optional] 
**is_osx** | **bool** |  | [optional] 
**is_windows** | **bool** |  | [optional] 
**is_docker** | **bool** |  | [optional] 
**mode** | [**RuntimeMode**](RuntimeMode.md) |  | [optional] 
**branch** | **str** |  | [optional] 
**database_type** | [**DatabaseType**](DatabaseType.md) |  | [optional] 
**database_version** | **str** |  | [optional] 
**authentication** | [**AuthenticationType**](AuthenticationType.md) |  | [optional] 
**migration_version** | **int** |  | [optional] 
**url_base** | **str** |  | [optional] 
**runtime_version** | **str** |  | [optional] 
**runtime_name** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**package_version** | **str** |  | [optional] 
**package_author** | **str** |  | [optional] 
**package_update_mechanism** | [**UpdateMechanism**](UpdateMechanism.md) |  | [optional] 
**package_update_mechanism_message** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.system_resource import SystemResource

# TODO update the JSON string below
json = "{}"
# create an instance of SystemResource from a JSON string
system_resource_instance = SystemResource.from_json(json)
# print the JSON string representation of the object
print(SystemResource.to_json())

# convert the object into a dict
system_resource_dict = system_resource_instance.to_dict()
# create an instance of SystemResource from a dict
system_resource_form_dict = system_resource.from_dict(system_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


