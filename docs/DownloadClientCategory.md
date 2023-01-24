# DownloadClientCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_category** | **str** |  | [optional] 
**categories** | **List[int]** |  | [optional] 

## Example

```python
from prowlarr.models.download_client_category import DownloadClientCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadClientCategory from a JSON string
download_client_category_instance = DownloadClientCategory.from_json(json)
# print the JSON string representation of the object
print DownloadClientCategory.to_json()

# convert the object into a dict
download_client_category_dict = download_client_category_instance.to_dict()
# create an instance of DownloadClientCategory from a dict
download_client_category_form_dict = download_client_category.from_dict(download_client_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


