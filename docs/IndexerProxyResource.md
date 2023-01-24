# IndexerProxyResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[Field]**](Field.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[IndexerProxyResource]**](IndexerProxyResource.md) |  | [optional] 
**link** | **str** |  | [optional] 
**on_health_issue** | **bool** |  | [optional] 
**supports_on_health_issue** | **bool** |  | [optional] 
**include_health_warnings** | **bool** |  | [optional] 
**test_command** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.indexer_proxy_resource import IndexerProxyResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerProxyResource from a JSON string
indexer_proxy_resource_instance = IndexerProxyResource.from_json(json)
# print the JSON string representation of the object
print IndexerProxyResource.to_json()

# convert the object into a dict
indexer_proxy_resource_dict = indexer_proxy_resource_instance.to_dict()
# create an instance of IndexerProxyResource from a dict
indexer_proxy_resource_form_dict = indexer_proxy_resource.from_dict(indexer_proxy_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


