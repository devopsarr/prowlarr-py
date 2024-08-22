# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.22.0.4670
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

class IndexerCategory(BaseModel):
    """
    IndexerCategory
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    sub_categories: Optional[List[IndexerCategory]] = Field(default=None, alias="subCategories")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "subCategories"]

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
        """Create an instance of IndexerCategory from a JSON string"""
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
            "sub_categories",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in sub_categories (list)
        _items = []
        if self.sub_categories:
            for _item in self.sub_categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subCategories'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if sub_categories (nullable) is None
        # and model_fields_set contains the field
        if self.sub_categories is None and "sub_categories" in self.model_fields_set:
            _dict['subCategories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerCategory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "subCategories": [IndexerCategory.from_dict(_item) for _item in obj["subCategories"]] if obj.get("subCategories") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
IndexerCategory.model_rebuild(raise_errors=False)

