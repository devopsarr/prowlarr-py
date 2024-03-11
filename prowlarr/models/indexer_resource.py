# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.13.3.4273
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from prowlarr.models.contract_field import ContractField
from prowlarr.models.download_protocol import DownloadProtocol
from prowlarr.models.indexer_capability_resource import IndexerCapabilityResource
from prowlarr.models.indexer_privacy import IndexerPrivacy
from prowlarr.models.indexer_status_resource import IndexerStatusResource
from prowlarr.models.provider_message import ProviderMessage
from typing import Optional, Set
from typing_extensions import Self

class IndexerResource(BaseModel):
    """
    IndexerResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    fields: Optional[List[ContractField]] = None
    implementation_name: Optional[StrictStr] = Field(default=None, alias="implementationName")
    implementation: Optional[StrictStr] = None
    config_contract: Optional[StrictStr] = Field(default=None, alias="configContract")
    info_link: Optional[StrictStr] = Field(default=None, alias="infoLink")
    message: Optional[ProviderMessage] = None
    tags: Optional[List[StrictInt]] = None
    presets: Optional[List[IndexerResource]] = None
    indexer_urls: Optional[List[StrictStr]] = Field(default=None, alias="indexerUrls")
    legacy_urls: Optional[List[StrictStr]] = Field(default=None, alias="legacyUrls")
    definition_name: Optional[StrictStr] = Field(default=None, alias="definitionName")
    description: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    encoding: Optional[StrictStr] = None
    enable: Optional[StrictBool] = None
    redirect: Optional[StrictBool] = None
    supports_rss: Optional[StrictBool] = Field(default=None, alias="supportsRss")
    supports_search: Optional[StrictBool] = Field(default=None, alias="supportsSearch")
    supports_redirect: Optional[StrictBool] = Field(default=None, alias="supportsRedirect")
    supports_pagination: Optional[StrictBool] = Field(default=None, alias="supportsPagination")
    app_profile_id: Optional[StrictInt] = Field(default=None, alias="appProfileId")
    protocol: Optional[DownloadProtocol] = None
    privacy: Optional[IndexerPrivacy] = None
    capabilities: Optional[IndexerCapabilityResource] = None
    priority: Optional[StrictInt] = None
    download_client_id: Optional[StrictInt] = Field(default=None, alias="downloadClientId")
    added: Optional[datetime] = None
    status: Optional[IndexerStatusResource] = None
    sort_name: Optional[StrictStr] = Field(default=None, alias="sortName")
    __properties: ClassVar[List[str]] = ["id", "name", "fields", "implementationName", "implementation", "configContract", "infoLink", "message", "tags", "presets", "indexerUrls", "legacyUrls", "definitionName", "description", "language", "encoding", "enable", "redirect", "supportsRss", "supportsSearch", "supportsRedirect", "supportsPagination", "appProfileId", "protocol", "privacy", "capabilities", "priority", "downloadClientId", "added", "status", "sortName"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndexerResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict['capabilities'] = self.capabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        # set to None if implementation_name (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_name is None and "implementation_name" in self.model_fields_set:
            _dict['implementationName'] = None

        # set to None if implementation (nullable) is None
        # and model_fields_set contains the field
        if self.implementation is None and "implementation" in self.model_fields_set:
            _dict['implementation'] = None

        # set to None if config_contract (nullable) is None
        # and model_fields_set contains the field
        if self.config_contract is None and "config_contract" in self.model_fields_set:
            _dict['configContract'] = None

        # set to None if info_link (nullable) is None
        # and model_fields_set contains the field
        if self.info_link is None and "info_link" in self.model_fields_set:
            _dict['infoLink'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if presets (nullable) is None
        # and model_fields_set contains the field
        if self.presets is None and "presets" in self.model_fields_set:
            _dict['presets'] = None

        # set to None if indexer_urls (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_urls is None and "indexer_urls" in self.model_fields_set:
            _dict['indexerUrls'] = None

        # set to None if legacy_urls (nullable) is None
        # and model_fields_set contains the field
        if self.legacy_urls is None and "legacy_urls" in self.model_fields_set:
            _dict['legacyUrls'] = None

        # set to None if definition_name (nullable) is None
        # and model_fields_set contains the field
        if self.definition_name is None and "definition_name" in self.model_fields_set:
            _dict['definitionName'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if encoding (nullable) is None
        # and model_fields_set contains the field
        if self.encoding is None and "encoding" in self.model_fields_set:
            _dict['encoding'] = None

        # set to None if sort_name (nullable) is None
        # and model_fields_set contains the field
        if self.sort_name is None and "sort_name" in self.model_fields_set:
            _dict['sortName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fields": [ContractField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "implementationName": obj.get("implementationName"),
            "implementation": obj.get("implementation"),
            "configContract": obj.get("configContract"),
            "infoLink": obj.get("infoLink"),
            "message": ProviderMessage.from_dict(obj["message"]) if obj.get("message") is not None else None,
            "tags": obj.get("tags"),
            "presets": [IndexerResource.from_dict(_item) for _item in obj["presets"]] if obj.get("presets") is not None else None,
            "indexerUrls": obj.get("indexerUrls"),
            "legacyUrls": obj.get("legacyUrls"),
            "definitionName": obj.get("definitionName"),
            "description": obj.get("description"),
            "language": obj.get("language"),
            "encoding": obj.get("encoding"),
            "enable": obj.get("enable"),
            "redirect": obj.get("redirect"),
            "supportsRss": obj.get("supportsRss"),
            "supportsSearch": obj.get("supportsSearch"),
            "supportsRedirect": obj.get("supportsRedirect"),
            "supportsPagination": obj.get("supportsPagination"),
            "appProfileId": obj.get("appProfileId"),
            "protocol": obj.get("protocol"),
            "privacy": obj.get("privacy"),
            "capabilities": IndexerCapabilityResource.from_dict(obj["capabilities"]) if obj.get("capabilities") is not None else None,
            "priority": obj.get("priority"),
            "downloadClientId": obj.get("downloadClientId"),
            "added": obj.get("added"),
            "status": IndexerStatusResource.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "sortName": obj.get("sortName")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
IndexerResource.model_rebuild(raise_errors=False)

