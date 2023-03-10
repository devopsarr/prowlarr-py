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


from typing import List, Optional
from pydantic import BaseModel
from prowlarr.models.host_statistics import HostStatistics
from prowlarr.models.indexer_statistics import IndexerStatistics
from prowlarr.models.user_agent_statistics import UserAgentStatistics

class IndexerStatsResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    indexers: Optional[List]
    user_agents: Optional[List]
    hosts: Optional[List]
    __properties = ["id", "indexers", "userAgents", "hosts"]

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
    def from_json(cls, json_str: str) -> IndexerStatsResource:
        """Create an instance of IndexerStatsResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in indexers (list)
        _items = []
        if self.indexers:
            for _item in self.indexers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['indexers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user_agents (list)
        _items = []
        if self.user_agents:
            for _item in self.user_agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['userAgents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hosts (list)
        _items = []
        if self.hosts:
            for _item in self.hosts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hosts'] = _items
        # set to None if indexers (nullable) is None
        if self.indexers is None:
            _dict['indexers'] = None

        # set to None if user_agents (nullable) is None
        if self.user_agents is None:
            _dict['userAgents'] = None

        # set to None if hosts (nullable) is None
        if self.hosts is None:
            _dict['hosts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IndexerStatsResource:
        """Create an instance of IndexerStatsResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IndexerStatsResource.parse_obj(obj)

        _obj = IndexerStatsResource.parse_obj({
            "id": obj.get("id"),
            "indexers": [IndexerStatistics.from_dict(_item) for _item in obj.get("indexers")] if obj.get("indexers") is not None else None,
            "user_agents": [UserAgentStatistics.from_dict(_item) for _item in obj.get("userAgents")] if obj.get("userAgents") is not None else None,
            "hosts": [HostStatistics.from_dict(_item) for _item in obj.get("hosts")] if obj.get("hosts") is not None else None
        })
        return _obj

