# UiConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_day_of_week** | **int** |  | [optional] 
**calendar_week_column_header** | **str** |  | [optional] 
**short_date_format** | **str** |  | [optional] 
**long_date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**show_relative_dates** | **bool** |  | [optional] 
**enable_color_impaired_mode** | **bool** |  | [optional] 
**ui_language** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.ui_config_resource import UiConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of UiConfigResource from a JSON string
ui_config_resource_instance = UiConfigResource.from_json(json)
# print the JSON string representation of the object
print(UiConfigResource.to_json())

# convert the object into a dict
ui_config_resource_dict = ui_config_resource_instance.to_dict()
# create an instance of UiConfigResource from a dict
ui_config_resource_form_dict = ui_config_resource.from_dict(ui_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


