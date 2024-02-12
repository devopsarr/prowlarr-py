# ProviderMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**type** | [**ProviderMessageType**](ProviderMessageType.md) |  | [optional] 

## Example

```python
from prowlarr.models.provider_message import ProviderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderMessage from a JSON string
provider_message_instance = ProviderMessage.from_json(json)
# print the JSON string representation of the object
print ProviderMessage.to_json()

# convert the object into a dict
provider_message_dict = provider_message_instance.to_dict()
# create an instance of ProviderMessage from a dict
provider_message_form_dict = provider_message.from_dict(provider_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


