# IndexerStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexer_id** | **int** |  | [optional] 
**indexer_name** | **str** |  | [optional] 
**average_response_time** | **int** |  | [optional] 
**number_of_queries** | **int** |  | [optional] 
**number_of_grabs** | **int** |  | [optional] 
**number_of_rss_queries** | **int** |  | [optional] 
**number_of_auth_queries** | **int** |  | [optional] 
**number_of_failed_queries** | **int** |  | [optional] 
**number_of_failed_grabs** | **int** |  | [optional] 
**number_of_failed_rss_queries** | **int** |  | [optional] 
**number_of_failed_auth_queries** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.indexer_statistics import IndexerStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerStatistics from a JSON string
indexer_statistics_instance = IndexerStatistics.from_json(json)
# print the JSON string representation of the object
print(IndexerStatistics.to_json())

# convert the object into a dict
indexer_statistics_dict = indexer_statistics_instance.to_dict()
# create an instance of IndexerStatistics from a dict
indexer_statistics_form_dict = indexer_statistics.from_dict(indexer_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


