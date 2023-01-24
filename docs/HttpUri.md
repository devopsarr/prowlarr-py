# HttpUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_uri** | **str** |  | [optional] [readonly] 
**scheme** | **str** |  | [optional] [readonly] 
**host** | **str** |  | [optional] [readonly] 
**port** | **int** |  | [optional] [readonly] 
**path** | **str** |  | [optional] [readonly] 
**query** | **str** |  | [optional] [readonly] 
**fragment** | **str** |  | [optional] [readonly] 

## Example

```python
from prowlarr.models.http_uri import HttpUri

# TODO update the JSON string below
json = "{}"
# create an instance of HttpUri from a JSON string
http_uri_instance = HttpUri.from_json(json)
# print the JSON string representation of the object
print HttpUri.to_json()

# convert the object into a dict
http_uri_dict = http_uri_instance.to_dict()
# create an instance of HttpUri from a dict
http_uri_form_dict = http_uri.from_dict(http_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


