# DownloadClientResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[ContractField]**](ContractField.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[DownloadClientResource]**](DownloadClientResource.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**priority** | **int** |  | [optional] 
**categories** | [**List[DownloadClientCategory]**](DownloadClientCategory.md) |  | [optional] 
**supports_categories** | **bool** |  | [optional] 

## Example

```python
from prowlarr.models.download_client_resource import DownloadClientResource

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadClientResource from a JSON string
download_client_resource_instance = DownloadClientResource.from_json(json)
# print the JSON string representation of the object
print(DownloadClientResource.to_json())

# convert the object into a dict
download_client_resource_dict = download_client_resource_instance.to_dict()
# create an instance of DownloadClientResource from a dict
download_client_resource_from_dict = DownloadClientResource.from_dict(download_client_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


