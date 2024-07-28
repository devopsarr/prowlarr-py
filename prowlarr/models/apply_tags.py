# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.21.2.4649
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ApplyTags(str, Enum):
    """
    ApplyTags
    """

    """
    allowed enum values
    """
    ADD = 'add'
    REMOVE = 'remove'
    REPLACE = 'replace'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplyTags from a JSON string"""
        return cls(json.loads(json_str))


