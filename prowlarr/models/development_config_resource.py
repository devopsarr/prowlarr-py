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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class DevelopmentConfigResource(BaseModel):
    """
    DevelopmentConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    console_log_level: Optional[StrictStr] = Field(default=None, alias="consoleLogLevel")
    log_sql: Optional[StrictBool] = Field(default=None, alias="logSql")
    log_indexer_response: Optional[StrictBool] = Field(default=None, alias="logIndexerResponse")
    log_rotate: Optional[StrictInt] = Field(default=None, alias="logRotate")
    filter_sentry_events: Optional[StrictBool] = Field(default=None, alias="filterSentryEvents")
    __properties: ClassVar[List[str]] = ["id", "consoleLogLevel", "logSql", "logIndexerResponse", "logRotate", "filterSentryEvents"]

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
        """Create an instance of DevelopmentConfigResource from a JSON string"""
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
        # set to None if console_log_level (nullable) is None
        # and model_fields_set contains the field
        if self.console_log_level is None and "console_log_level" in self.model_fields_set:
            _dict['consoleLogLevel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DevelopmentConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "consoleLogLevel": obj.get("consoleLogLevel"),
            "logSql": obj.get("logSql"),
            "logIndexerResponse": obj.get("logIndexerResponse"),
            "logRotate": obj.get("logRotate"),
            "filterSentryEvents": obj.get("filterSentryEvents")
        })
        return _obj


