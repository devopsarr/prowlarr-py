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

class TagDetailsResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    label: Optional[str]
    notification_ids: Optional[List]
    indexer_ids: Optional[List]
    indexer_proxy_ids: Optional[List]
    application_ids: Optional[List]
    __properties = ["id", "label", "notificationIds", "indexerIds", "indexerProxyIds", "applicationIds"]

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
    def from_json(cls, json_str: str) -> TagDetailsResource:
        """Create an instance of TagDetailsResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if label (nullable) is None
        if self.label is None:
            _dict['label'] = None

        # set to None if notification_ids (nullable) is None
        if self.notification_ids is None:
            _dict['notificationIds'] = None

        # set to None if indexer_ids (nullable) is None
        if self.indexer_ids is None:
            _dict['indexerIds'] = None

        # set to None if indexer_proxy_ids (nullable) is None
        if self.indexer_proxy_ids is None:
            _dict['indexerProxyIds'] = None

        # set to None if application_ids (nullable) is None
        if self.application_ids is None:
            _dict['applicationIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TagDetailsResource:
        """Create an instance of TagDetailsResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TagDetailsResource.parse_obj(obj)

        _obj = TagDetailsResource.parse_obj({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "notification_ids": obj.get("notificationIds"),
            "indexer_ids": obj.get("indexerIds"),
            "indexer_proxy_ids": obj.get("indexerProxyIds"),
            "application_ids": obj.get("applicationIds")
        })
        return _obj

