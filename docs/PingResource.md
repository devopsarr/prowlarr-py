# PingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.ping_resource import PingResource

# TODO update the JSON string below
json = "{}"
# create an instance of PingResource from a JSON string
ping_resource_instance = PingResource.from_json(json)
# print the JSON string representation of the object
print(PingResource.to_json())

# convert the object into a dict
ping_resource_dict = ping_resource_instance.to_dict()
# create an instance of PingResource from a dict
ping_resource_from_dict = PingResource.from_dict(ping_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


