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


from typing import Optional
from pydantic import BaseModel

class IndexerStatistics(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    indexer_id: Optional[int]
    indexer_name: Optional[str]
    average_response_time: Optional[int]
    number_of_queries: Optional[int]
    number_of_grabs: Optional[int]
    number_of_rss_queries: Optional[int]
    number_of_auth_queries: Optional[int]
    number_of_failed_queries: Optional[int]
    number_of_failed_grabs: Optional[int]
    number_of_failed_rss_queries: Optional[int]
    number_of_failed_auth_queries: Optional[int]
    __properties = ["indexerId", "indexerName", "averageResponseTime", "numberOfQueries", "numberOfGrabs", "numberOfRssQueries", "numberOfAuthQueries", "numberOfFailedQueries", "numberOfFailedGrabs", "numberOfFailedRssQueries", "numberOfFailedAuthQueries"]

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
    def from_json(cls, json_str: str) -> IndexerStatistics:
        """Create an instance of IndexerStatistics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if indexer_name (nullable) is None
        if self.indexer_name is None:
            _dict['indexerName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IndexerStatistics:
        """Create an instance of IndexerStatistics from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IndexerStatistics.parse_obj(obj)

        _obj = IndexerStatistics.parse_obj({
            "indexer_id": obj.get("indexerId"),
            "indexer_name": obj.get("indexerName"),
            "average_response_time": obj.get("averageResponseTime"),
            "number_of_queries": obj.get("numberOfQueries"),
            "number_of_grabs": obj.get("numberOfGrabs"),
            "number_of_rss_queries": obj.get("numberOfRssQueries"),
            "number_of_auth_queries": obj.get("numberOfAuthQueries"),
            "number_of_failed_queries": obj.get("numberOfFailedQueries"),
            "number_of_failed_grabs": obj.get("numberOfFailedGrabs"),
            "number_of_failed_rss_queries": obj.get("numberOfFailedRssQueries"),
            "number_of_failed_auth_queries": obj.get("numberOfFailedAuthQueries")
        })
        return _obj
