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

class IndexerCategory(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    sub_categories: Optional[List]
    __properties = ["id", "name", "description", "subCategories"]

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
    def from_json(cls, json_str: str) -> IndexerCategory:
        """Create an instance of IndexerCategory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "sub_categories",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in sub_categories (list)
        _items = []
        if self.sub_categories:
            for _item in self.sub_categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subCategories'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if description (nullable) is None
        if self.description is None:
            _dict['description'] = None

        # set to None if sub_categories (nullable) is None
        if self.sub_categories is None:
            _dict['subCategories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IndexerCategory:
        """Create an instance of IndexerCategory from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IndexerCategory.parse_obj(obj)

        _obj = IndexerCategory.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "sub_categories": [IndexerCategory.from_dict(_item) for _item in obj.get("subCategories")] if obj.get("subCategories") is not None else None
        })
        return _obj

