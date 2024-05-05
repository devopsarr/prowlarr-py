# ContractField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**help_text_warning** | **str** |  | [optional] 
**help_link** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**advanced** | **bool** |  | [optional] 
**select_options** | [**List[SelectOption]**](SelectOption.md) |  | [optional] 
**select_options_provider_action** | **str** |  | [optional] 
**section** | **str** |  | [optional] 
**hidden** | **str** |  | [optional] 
**privacy** | [**PrivacyLevel**](PrivacyLevel.md) |  | [optional] 
**placeholder** | **str** |  | [optional] 
**is_float** | **bool** |  | [optional] 

## Example

```python
from prowlarr.models.contract_field import ContractField

# TODO update the JSON string below
json = "{}"
# create an instance of ContractField from a JSON string
contract_field_instance = ContractField.from_json(json)
# print the JSON string representation of the object
print(ContractField.to_json())

# convert the object into a dict
contract_field_dict = contract_field_instance.to_dict()
# create an instance of ContractField from a dict
contract_field_from_dict = ContractField.from_dict(contract_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


