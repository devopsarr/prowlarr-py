# HistoryResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**indexer_id** | **int** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**download_id** | **str** |  | [optional] 
**successful** | **bool** |  | [optional] 
**event_type** | [**HistoryEventType**](HistoryEventType.md) |  | [optional] 
**data** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from prowlarr.models.history_resource import HistoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryResource from a JSON string
history_resource_instance = HistoryResource.from_json(json)
# print the JSON string representation of the object
print(HistoryResource.to_json())

# convert the object into a dict
history_resource_dict = history_resource_instance.to_dict()
# create an instance of HistoryResource from a dict
history_resource_from_dict = HistoryResource.from_dict(history_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


