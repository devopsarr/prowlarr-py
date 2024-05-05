# LocalizationOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.localization_option import LocalizationOption

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationOption from a JSON string
localization_option_instance = LocalizationOption.from_json(json)
# print the JSON string representation of the object
print(LocalizationOption.to_json())

# convert the object into a dict
localization_option_dict = localization_option_instance.to_dict()
# create an instance of LocalizationOption from a dict
localization_option_from_dict = LocalizationOption.from_dict(localization_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


