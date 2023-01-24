# SelectOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**hint** | **str** |  | [optional] 
**parent_value** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.select_option import SelectOption

# TODO update the JSON string below
json = "{}"
# create an instance of SelectOption from a JSON string
select_option_instance = SelectOption.from_json(json)
# print the JSON string representation of the object
print SelectOption.to_json()

# convert the object into a dict
select_option_dict = select_option_instance.to_dict()
# create an instance of SelectOption from a dict
select_option_form_dict = select_option.from_dict(select_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


