# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.23.1.4708
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class TaskResource(BaseModel):
    """
    TaskResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    task_name: Optional[StrictStr] = Field(default=None, alias="taskName")
    interval: Optional[StrictInt] = None
    last_execution: Optional[datetime] = Field(default=None, alias="lastExecution")
    last_start_time: Optional[datetime] = Field(default=None, alias="lastStartTime")
    next_execution: Optional[datetime] = Field(default=None, alias="nextExecution")
    last_duration: Optional[StrictStr] = Field(default=None, alias="lastDuration")
    __properties: ClassVar[List[str]] = ["id", "name", "taskName", "interval", "lastExecution", "lastStartTime", "nextExecution", "lastDuration"]

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
        """Create an instance of TaskResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "last_duration",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if task_name (nullable) is None
        # and model_fields_set contains the field
        if self.task_name is None and "task_name" in self.model_fields_set:
            _dict['taskName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TaskResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "taskName": obj.get("taskName"),
            "interval": obj.get("interval"),
            "lastExecution": obj.get("lastExecution"),
            "lastStartTime": obj.get("lastStartTime"),
            "nextExecution": obj.get("nextExecution"),
            "lastDuration": obj.get("lastDuration")
        })
        return _obj


