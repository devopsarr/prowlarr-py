# UserAgentStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | **str** |  | [optional] 
**number_of_queries** | **int** |  | [optional] 
**number_of_grabs** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.user_agent_statistics import UserAgentStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgentStatistics from a JSON string
user_agent_statistics_instance = UserAgentStatistics.from_json(json)
# print the JSON string representation of the object
print UserAgentStatistics.to_json()

# convert the object into a dict
user_agent_statistics_dict = user_agent_statistics_instance.to_dict()
# create an instance of UserAgentStatistics from a dict
user_agent_statistics_form_dict = user_agent_statistics.from_dict(user_agent_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


