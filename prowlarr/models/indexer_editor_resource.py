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
from prowlarr.models.apply_tags import ApplyTags

class IndexerEditorResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    indexer_ids: Optional[List]
    enable: Optional[bool]
    app_profile_id: Optional[int]
    tags: Optional[List]
    apply_tags: Optional[ApplyTags]
    __properties = ["indexerIds", "enable", "appProfileId", "tags", "applyTags"]

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
    def from_json(cls, json_str: str) -> IndexerEditorResource:
        """Create an instance of IndexerEditorResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if indexer_ids (nullable) is None
        if self.indexer_ids is None:
            _dict['indexerIds'] = None

        # set to None if enable (nullable) is None
        if self.enable is None:
            _dict['enable'] = None

        # set to None if app_profile_id (nullable) is None
        if self.app_profile_id is None:
            _dict['appProfileId'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IndexerEditorResource:
        """Create an instance of IndexerEditorResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IndexerEditorResource.parse_obj(obj)

        _obj = IndexerEditorResource.parse_obj({
            "indexer_ids": obj.get("indexerIds"),
            "enable": obj.get("enable"),
            "app_profile_id": obj.get("appProfileId"),
            "tags": obj.get("tags"),
            "apply_tags": obj.get("applyTags")
        })
        return _obj

