# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.21.2.4649
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class IndexerStatusResource(BaseModel):
    """
    IndexerStatusResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    indexer_id: Optional[StrictInt] = Field(default=None, alias="indexerId")
    disabled_till: Optional[datetime] = Field(default=None, alias="disabledTill")
    most_recent_failure: Optional[datetime] = Field(default=None, alias="mostRecentFailure")
    initial_failure: Optional[datetime] = Field(default=None, alias="initialFailure")
    __properties: ClassVar[List[str]] = ["id", "indexerId", "disabledTill", "mostRecentFailure", "initialFailure"]

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
        """Create an instance of IndexerStatusResource from a JSON string"""
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
        # set to None if disabled_till (nullable) is None
        # and model_fields_set contains the field
        if self.disabled_till is None and "disabled_till" in self.model_fields_set:
            _dict['disabledTill'] = None

        # set to None if most_recent_failure (nullable) is None
        # and model_fields_set contains the field
        if self.most_recent_failure is None and "most_recent_failure" in self.model_fields_set:
            _dict['mostRecentFailure'] = None

        # set to None if initial_failure (nullable) is None
        # and model_fields_set contains the field
        if self.initial_failure is None and "initial_failure" in self.model_fields_set:
            _dict['initialFailure'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerStatusResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "indexerId": obj.get("indexerId"),
            "disabledTill": obj.get("disabledTill"),
            "mostRecentFailure": obj.get("mostRecentFailure"),
            "initialFailure": obj.get("initialFailure")
        })
        return _obj


