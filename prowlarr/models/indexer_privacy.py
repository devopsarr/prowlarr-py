# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.16.2.4435
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IndexerPrivacy(str, Enum):
    """
    IndexerPrivacy
    """

    """
    allowed enum values
    """
    PUBLIC = 'public'
    SEMIPRIVATE = 'semiPrivate'
    PRIVATE = 'private'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndexerPrivacy from a JSON string"""
        return cls(json.loads(json_str))


