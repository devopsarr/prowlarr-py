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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TagDetailsResource(BaseModel):
    """
    TagDetailsResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    label: Optional[StrictStr] = None
    notification_ids: Optional[List[StrictInt]] = Field(default=None, alias="notificationIds")
    indexer_ids: Optional[List[StrictInt]] = Field(default=None, alias="indexerIds")
    indexer_proxy_ids: Optional[List[StrictInt]] = Field(default=None, alias="indexerProxyIds")
    application_ids: Optional[List[StrictInt]] = Field(default=None, alias="applicationIds")
    __properties: ClassVar[List[str]] = ["id", "label", "notificationIds", "indexerIds", "indexerProxyIds", "applicationIds"]

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
        """Create an instance of TagDetailsResource from a JSON string"""
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
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if notification_ids (nullable) is None
        # and model_fields_set contains the field
        if self.notification_ids is None and "notification_ids" in self.model_fields_set:
            _dict['notificationIds'] = None

        # set to None if indexer_ids (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_ids is None and "indexer_ids" in self.model_fields_set:
            _dict['indexerIds'] = None

        # set to None if indexer_proxy_ids (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_proxy_ids is None and "indexer_proxy_ids" in self.model_fields_set:
            _dict['indexerProxyIds'] = None

        # set to None if application_ids (nullable) is None
        # and model_fields_set contains the field
        if self.application_ids is None and "application_ids" in self.model_fields_set:
            _dict['applicationIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagDetailsResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "notificationIds": obj.get("notificationIds"),
            "indexerIds": obj.get("indexerIds"),
            "indexerProxyIds": obj.get("indexerProxyIds"),
            "applicationIds": obj.get("applicationIds")
        })
        return _obj


