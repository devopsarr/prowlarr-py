# IndexerStatsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**indexers** | [**List[IndexerStatistics]**](IndexerStatistics.md) |  | [optional] 
**user_agents** | [**List[UserAgentStatistics]**](UserAgentStatistics.md) |  | [optional] 
**hosts** | [**List[HostStatistics]**](HostStatistics.md) |  | [optional] 

## Example

```python
from prowlarr.models.indexer_stats_resource import IndexerStatsResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerStatsResource from a JSON string
indexer_stats_resource_instance = IndexerStatsResource.from_json(json)
# print the JSON string representation of the object
print IndexerStatsResource.to_json()

# convert the object into a dict
indexer_stats_resource_dict = indexer_stats_resource_instance.to_dict()
# create an instance of IndexerStatsResource from a dict
indexer_stats_resource_form_dict = indexer_stats_resource.from_dict(indexer_stats_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


