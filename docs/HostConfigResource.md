# HostConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**bind_address** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**ssl_port** | **int** |  | [optional] 
**enable_ssl** | **bool** |  | [optional] 
**launch_browser** | **bool** |  | [optional] 
**authentication_method** | [**AuthenticationType**](AuthenticationType.md) |  | [optional] 
**authentication_required** | [**AuthenticationRequiredType**](AuthenticationRequiredType.md) |  | [optional] 
**analytics_enabled** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**password_confirmation** | **str** |  | [optional] 
**log_level** | **str** |  | [optional] 
**log_size_limit** | **int** |  | [optional] 
**console_log_level** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**ssl_cert_path** | **str** |  | [optional] 
**ssl_cert_password** | **str** |  | [optional] 
**url_base** | **str** |  | [optional] 
**instance_name** | **str** |  | [optional] 
**application_url** | **str** |  | [optional] 
**update_automatically** | **bool** |  | [optional] 
**update_mechanism** | [**UpdateMechanism**](UpdateMechanism.md) |  | [optional] 
**update_script_path** | **str** |  | [optional] 
**proxy_enabled** | **bool** |  | [optional] 
**proxy_type** | [**ProxyType**](ProxyType.md) |  | [optional] 
**proxy_hostname** | **str** |  | [optional] 
**proxy_port** | **int** |  | [optional] 
**proxy_username** | **str** |  | [optional] 
**proxy_password** | **str** |  | [optional] 
**proxy_bypass_filter** | **str** |  | [optional] 
**proxy_bypass_local_addresses** | **bool** |  | [optional] 
**certificate_validation** | [**CertificateValidationType**](CertificateValidationType.md) |  | [optional] 
**backup_folder** | **str** |  | [optional] 
**backup_interval** | **int** |  | [optional] 
**backup_retention** | **int** |  | [optional] 
**history_cleanup_days** | **int** |  | [optional] 

## Example

```python
from prowlarr.models.host_config_resource import HostConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigResource from a JSON string
host_config_resource_instance = HostConfigResource.from_json(json)
# print the JSON string representation of the object
print(HostConfigResource.to_json())

# convert the object into a dict
host_config_resource_dict = host_config_resource_instance.to_dict()
# create an instance of HostConfigResource from a dict
host_config_resource_from_dict = HostConfigResource.from_dict(host_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


