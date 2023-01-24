# PagingResourceFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.paging_resource_filter import PagingResourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PagingResourceFilter from a JSON string
paging_resource_filter_instance = PagingResourceFilter.from_json(json)
# print the JSON string representation of the object
print PagingResourceFilter.to_json()

# convert the object into a dict
paging_resource_filter_dict = paging_resource_filter_instance.to_dict()
# create an instance of PagingResourceFilter from a dict
paging_resource_filter_form_dict = paging_resource_filter.from_dict(paging_resource_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


