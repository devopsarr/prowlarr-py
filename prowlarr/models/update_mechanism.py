# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.22.0.4670
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UpdateMechanism(str, Enum):
    """
    UpdateMechanism
    """

    """
    allowed enum values
    """
    BUILTIN = 'builtIn'
    SCRIPT = 'script'
    EXTERNAL = 'external'
    APT = 'apt'
    DOCKER = 'docker'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UpdateMechanism from a JSON string"""
        return cls(json.loads(json_str))


