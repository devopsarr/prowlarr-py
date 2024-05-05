# HostStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**number_of_queries** | **int** |  | [optional] 
**number_of_grabs** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.host_statistics import HostStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of HostStatistics from a JSON string
host_statistics_instance = HostStatistics.from_json(json)
# print the JSON string representation of the object
print(HostStatistics.to_json())

# convert the object into a dict
host_statistics_dict = host_statistics_instance.to_dict()
# create an instance of HostStatistics from a dict
host_statistics_from_dict = HostStatistics.from_dict(host_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


