# HistoryResourcePagingResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[HistoryResource]**](HistoryResource.md) |  | [optional] 

## Example

```python
from prowlarr.models.history_resource_paging_resource import HistoryResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryResourcePagingResource from a JSON string
history_resource_paging_resource_instance = HistoryResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print HistoryResourcePagingResource.to_json()

# convert the object into a dict
history_resource_paging_resource_dict = history_resource_paging_resource_instance.to_dict()
# create an instance of HistoryResourcePagingResource from a dict
history_resource_paging_resource_form_dict = history_resource_paging_resource.from_dict(history_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


