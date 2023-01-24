# Field


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**help_link** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**advanced** | **bool** |  | [optional] 
**select_options** | [**List[SelectOption]**](SelectOption.md) |  | [optional] 
**select_options_provider_action** | **str** |  | [optional] 
**section** | **str** |  | [optional] 
**hidden** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.field import Field

# TODO update the JSON string below
json = "{}"
# create an instance of Field from a JSON string
field_instance = Field.from_json(json)
# print the JSON string representation of the object
print Field.to_json()

# convert the object into a dict
field_dict = field_instance.to_dict()
# create an instance of Field from a dict
field_form_dict = field.from_dict(field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


