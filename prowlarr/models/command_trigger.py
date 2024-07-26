# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.20.1.4603
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CommandTrigger(str, Enum):
    """
    CommandTrigger
    """

    """
    allowed enum values
    """
    UNSPECIFIED = 'unspecified'
    MANUAL = 'manual'
    SCHEDULED = 'scheduled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CommandTrigger from a JSON string"""
        return cls(json.loads(json_str))


