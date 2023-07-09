# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from prowlarr.models.download_protocol import DownloadProtocol
from prowlarr.models.field import Field
from prowlarr.models.indexer_capability_resource import IndexerCapabilityResource
from prowlarr.models.indexer_privacy import IndexerPrivacy
from prowlarr.models.indexer_status_resource import IndexerStatusResource
from prowlarr.models.provider_message import ProviderMessage

class IndexerResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    fields: Optional[List]
    implementation_name: Optional[str]
    implementation: Optional[str]
    config_contract: Optional[str]
    info_link: Optional[str]
    message: Optional[ProviderMessage]
    tags: Optional[List]
    presets: Optional[List]
    indexer_urls: Optional[List]
    legacy_urls: Optional[List]
    definition_name: Optional[str]
    description: Optional[str]
    language: Optional[str]
    encoding: Optional[str]
    enable: Optional[bool]
    redirect: Optional[bool]
    supports_rss: Optional[bool]
    supports_search: Optional[bool]
    supports_redirect: Optional[bool]
    supports_pagination: Optional[bool]
    app_profile_id: Optional[int]
    protocol: Optional[DownloadProtocol]
    privacy: Optional[IndexerPrivacy]
    capabilities: Optional[IndexerCapabilityResource]
    priority: Optional[int]
    download_client_id: Optional[int]
    added: Optional[datetime]
    status: Optional[IndexerStatusResource]
    sort_name: Optional[str]
    __properties = ["id", "name", "fields", "implementationName", "implementation", "configContract", "infoLink", "message", "tags", "presets", "indexerUrls", "legacyUrls", "definitionName", "description", "language", "encoding", "enable", "redirect", "supportsRss", "supportsSearch", "supportsRedirect", "supportsPagination", "appProfileId", "protocol", "privacy", "capabilities", "priority", "downloadClientId", "added", "status", "sortName"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IndexerResource:
        """Create an instance of IndexerResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
        if self.name is None:
            _dict['name'] = None

        # set to None if fields (nullable) is None
        if self.fields is None:
            _dict['fields'] = None

        # set to None if implementation_name (nullable) is None
        if self.implementation_name is None:
            _dict['implementationName'] = None

        # set to None if implementation (nullable) is None
        if self.implementation is None:
            _dict['implementation'] = None

        # set to None if config_contract (nullable) is None
        if self.config_contract is None:
            _dict['configContract'] = None

        # set to None if info_link (nullable) is None
        if self.info_link is None:
            _dict['infoLink'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        # set to None if presets (nullable) is None
        if self.presets is None:
            _dict['presets'] = None

        # set to None if indexer_urls (nullable) is None
        if self.indexer_urls is None:
            _dict['indexerUrls'] = None

        # set to None if legacy_urls (nullable) is None
        if self.legacy_urls is None:
            _dict['legacyUrls'] = None

        # set to None if definition_name (nullable) is None
        if self.definition_name is None:
            _dict['definitionName'] = None

        # set to None if description (nullable) is None
        if self.description is None:
            _dict['description'] = None

        # set to None if language (nullable) is None
        if self.language is None:
            _dict['language'] = None

        # set to None if encoding (nullable) is None
        if self.encoding is None:
            _dict['encoding'] = None

        # set to None if sort_name (nullable) is None
        if self.sort_name is None:
            _dict['sortName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IndexerResource:
        """Create an instance of IndexerResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IndexerResource.parse_obj(obj)

        _obj = IndexerResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fields": [Field.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None,
            "implementation_name": obj.get("implementationName"),
            "implementation": obj.get("implementation"),
            "config_contract": obj.get("configContract"),
            "info_link": obj.get("infoLink"),
            "message": ProviderMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None,
            "tags": obj.get("tags"),
            "presets": [IndexerResource.from_dict(_item) for _item in obj.get("presets")] if obj.get("presets") is not None else None,
            "indexer_urls": obj.get("indexerUrls"),
            "legacy_urls": obj.get("legacyUrls"),
            "definition_name": obj.get("definitionName"),
            "description": obj.get("description"),
            "language": obj.get("language"),
            "encoding": obj.get("encoding"),
            "enable": obj.get("enable"),
            "redirect": obj.get("redirect"),
            "supports_rss": obj.get("supportsRss"),
            "supports_search": obj.get("supportsSearch"),
            "supports_redirect": obj.get("supportsRedirect"),
            "supports_pagination": obj.get("supportsPagination"),
            "app_profile_id": obj.get("appProfileId"),
            "protocol": obj.get("protocol"),
            "privacy": obj.get("privacy"),
            "capabilities": IndexerCapabilityResource.from_dict(obj.get("capabilities")) if obj.get("capabilities") is not None else None,
            "priority": obj.get("priority"),
            "download_client_id": obj.get("downloadClientId"),
            "added": obj.get("added"),
            "status": IndexerStatusResource.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "sort_name": obj.get("sortName")
        })
        return _obj

