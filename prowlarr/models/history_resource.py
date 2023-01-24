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
from typing import Dict, Optional
from pydantic import BaseModel
from prowlarr.models.history_event_type import HistoryEventType

class HistoryResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    indexer_id: Optional[int]
    var_date: Optional[datetime]
    download_id: Optional[str]
    successful: Optional[bool]
    event_type: Optional[HistoryEventType]
    data: Optional[Dict]
    __properties = ["id", "indexerId", "date", "downloadId", "successful", "eventType", "data"]

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
    def from_json(cls, json_str: str) -> HistoryResource:
        """Create an instance of HistoryResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if data (nullable) is None
        if self.data is None:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HistoryResource:
        """Create an instance of HistoryResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HistoryResource.parse_obj(obj)

        _obj = HistoryResource.parse_obj({
            "id": obj.get("id"),
            "indexer_id": obj.get("indexerId"),
            "var_date": obj.get("date"),
            "download_id": obj.get("downloadId"),
            "successful": obj.get("successful"),
            "event_type": obj.get("eventType"),
            "data": obj.get("data")
        })
        return _obj

