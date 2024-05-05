# IndexerCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**sub_categories** | [**List[IndexerCategory]**](IndexerCategory.md) |  | [optional] [readonly] 

## Example

```python
from prowlarr.models.indexer_category import IndexerCategory

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerCategory from a JSON string
indexer_category_instance = IndexerCategory.from_json(json)
# print the JSON string representation of the object
print(IndexerCategory.to_json())

# convert the object into a dict
indexer_category_dict = indexer_category_instance.to_dict()
# create an instance of IndexerCategory from a dict
indexer_category_from_dict = IndexerCategory.from_dict(indexer_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


