# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.31.2.4975
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class IndexerStatistics(BaseModel):
    """
    IndexerStatistics
    """ # noqa: E501
    indexer_id: Optional[StrictInt] = Field(default=None, alias="indexerId")
    indexer_name: Optional[StrictStr] = Field(default=None, alias="indexerName")
    average_response_time: Optional[StrictInt] = Field(default=None, alias="averageResponseTime")
    average_grab_response_time: Optional[StrictInt] = Field(default=None, alias="averageGrabResponseTime")
    number_of_queries: Optional[StrictInt] = Field(default=None, alias="numberOfQueries")
    number_of_grabs: Optional[StrictInt] = Field(default=None, alias="numberOfGrabs")
    number_of_rss_queries: Optional[StrictInt] = Field(default=None, alias="numberOfRssQueries")
    number_of_auth_queries: Optional[StrictInt] = Field(default=None, alias="numberOfAuthQueries")
    number_of_failed_queries: Optional[StrictInt] = Field(default=None, alias="numberOfFailedQueries")
    number_of_failed_grabs: Optional[StrictInt] = Field(default=None, alias="numberOfFailedGrabs")
    number_of_failed_rss_queries: Optional[StrictInt] = Field(default=None, alias="numberOfFailedRssQueries")
    number_of_failed_auth_queries: Optional[StrictInt] = Field(default=None, alias="numberOfFailedAuthQueries")
    __properties: ClassVar[List[str]] = ["indexerId", "indexerName", "averageResponseTime", "averageGrabResponseTime", "numberOfQueries", "numberOfGrabs", "numberOfRssQueries", "numberOfAuthQueries", "numberOfFailedQueries", "numberOfFailedGrabs", "numberOfFailedRssQueries", "numberOfFailedAuthQueries"]

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
        """Create an instance of IndexerStatistics from a JSON string"""
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
        # set to None if indexer_name (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_name is None and "indexer_name" in self.model_fields_set:
            _dict['indexerName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "indexerId": obj.get("indexerId"),
            "indexerName": obj.get("indexerName"),
            "averageResponseTime": obj.get("averageResponseTime"),
            "averageGrabResponseTime": obj.get("averageGrabResponseTime"),
            "numberOfQueries": obj.get("numberOfQueries"),
            "numberOfGrabs": obj.get("numberOfGrabs"),
            "numberOfRssQueries": obj.get("numberOfRssQueries"),
            "numberOfAuthQueries": obj.get("numberOfAuthQueries"),
            "numberOfFailedQueries": obj.get("numberOfFailedQueries"),
            "numberOfFailedGrabs": obj.get("numberOfFailedGrabs"),
            "numberOfFailedRssQueries": obj.get("numberOfFailedRssQueries"),
            "numberOfFailedAuthQueries": obj.get("numberOfFailedAuthQueries")
        })
        return _obj


