# DownloadClientConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.download_client_config_resource import DownloadClientConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadClientConfigResource from a JSON string
download_client_config_resource_instance = DownloadClientConfigResource.from_json(json)
# print the JSON string representation of the object
print(DownloadClientConfigResource.to_json())

# convert the object into a dict
download_client_config_resource_dict = download_client_config_resource_instance.to_dict()
# create an instance of DownloadClientConfigResource from a dict
download_client_config_resource_from_dict = DownloadClientConfigResource.from_dict(download_client_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


