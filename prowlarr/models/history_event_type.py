# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.23.1.4708
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class HistoryEventType(str, Enum):
    """
    HistoryEventType
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    RELEASEGRABBED = 'releaseGrabbed'
    INDEXERQUERY = 'indexerQuery'
    INDEXERRSS = 'indexerRss'
    INDEXERAUTH = 'indexerAuth'
    INDEXERINFO = 'indexerInfo'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HistoryEventType from a JSON string"""
        return cls(json.loads(json_str))


