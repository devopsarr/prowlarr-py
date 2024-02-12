# DownloadClientBulkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.download_client_bulk_resource import DownloadClientBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadClientBulkResource from a JSON string
download_client_bulk_resource_instance = DownloadClientBulkResource.from_json(json)
# print the JSON string representation of the object
print DownloadClientBulkResource.to_json()

# convert the object into a dict
download_client_bulk_resource_dict = download_client_bulk_resource_instance.to_dict()
# create an instance of DownloadClientBulkResource from a dict
download_client_bulk_resource_form_dict = download_client_bulk_resource.from_dict(download_client_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


