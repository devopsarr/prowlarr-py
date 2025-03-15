# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.31.2.4975
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ApplicationSyncLevel(str, Enum):
    """
    ApplicationSyncLevel
    """

    """
    allowed enum values
    """
    DISABLED = 'disabled'
    ADDONLY = 'addOnly'
    FULLSYNC = 'fullSync'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplicationSyncLevel from a JSON string"""
        return cls(json.loads(json_str))


