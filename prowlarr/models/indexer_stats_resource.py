# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.30.2.4939
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from prowlarr.models.host_statistics import HostStatistics
from prowlarr.models.indexer_statistics import IndexerStatistics
from prowlarr.models.user_agent_statistics import UserAgentStatistics
from typing import Optional, Set
from typing_extensions import Self

class IndexerStatsResource(BaseModel):
    """
    IndexerStatsResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    indexers: Optional[List[IndexerStatistics]] = None
    user_agents: Optional[List[UserAgentStatistics]] = Field(default=None, alias="userAgents")
    hosts: Optional[List[HostStatistics]] = None
    __properties: ClassVar[List[str]] = ["id", "indexers", "userAgents", "hosts"]

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
        """Create an instance of IndexerStatsResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in indexers (list)
        _items = []
        if self.indexers:
            for _item_indexers in self.indexers:
                if _item_indexers:
                    _items.append(_item_indexers.to_dict())
            _dict['indexers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user_agents (list)
        _items = []
        if self.user_agents:
            for _item_user_agents in self.user_agents:
                if _item_user_agents:
                    _items.append(_item_user_agents.to_dict())
            _dict['userAgents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hosts (list)
        _items = []
        if self.hosts:
            for _item_hosts in self.hosts:
                if _item_hosts:
                    _items.append(_item_hosts.to_dict())
            _dict['hosts'] = _items
        # set to None if indexers (nullable) is None
        # and model_fields_set contains the field
        if self.indexers is None and "indexers" in self.model_fields_set:
            _dict['indexers'] = None

        # set to None if user_agents (nullable) is None
        # and model_fields_set contains the field
        if self.user_agents is None and "user_agents" in self.model_fields_set:
            _dict['userAgents'] = None

        # set to None if hosts (nullable) is None
        # and model_fields_set contains the field
        if self.hosts is None and "hosts" in self.model_fields_set:
            _dict['hosts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerStatsResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "indexers": [IndexerStatistics.from_dict(_item) for _item in obj["indexers"]] if obj.get("indexers") is not None else None,
            "userAgents": [UserAgentStatistics.from_dict(_item) for _item in obj["userAgents"]] if obj.get("userAgents") is not None else None,
            "hosts": [HostStatistics.from_dict(_item) for _item in obj["hosts"]] if obj.get("hosts") is not None else None
        })
        return _obj


