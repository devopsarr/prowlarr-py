# IndexerResource


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
**presets** | [**List[IndexerResource]**](IndexerResource.md) |  | [optional] 
**indexer_urls** | **List[str]** |  | [optional] 
**legacy_urls** | **List[str]** |  | [optional] 
**definition_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**redirect** | **bool** |  | [optional] 
**supports_rss** | **bool** |  | [optional] 
**supports_search** | **bool** |  | [optional] 
**supports_redirect** | **bool** |  | [optional] 
**app_profile_id** | **int** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**privacy** | [**IndexerPrivacy**](IndexerPrivacy.md) |  | [optional] 
**capabilities** | [**IndexerCapabilityResource**](IndexerCapabilityResource.md) |  | [optional] 
**priority** | **int** |  | [optional] 
**added** | **datetime** |  | [optional] 
**status** | [**IndexerStatusResource**](IndexerStatusResource.md) |  | [optional] 
**sort_name** | **str** |  | [optional] 

## Example

```python
from prowlarr.models.indexer_resource import IndexerResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerResource from a JSON string
indexer_resource_instance = IndexerResource.from_json(json)
# print the JSON string representation of the object
print IndexerResource.to_json()

# convert the object into a dict
indexer_resource_dict = indexer_resource_instance.to_dict()
# create an instance of IndexerResource from a dict
indexer_resource_form_dict = indexer_resource.from_dict(indexer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


