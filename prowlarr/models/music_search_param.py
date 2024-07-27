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


class MusicSearchParam(str, Enum):
    """
    MusicSearchParam
    """

    """
    allowed enum values
    """
    Q = 'q'
    ALBUM = 'album'
    ARTIST = 'artist'
    LABEL = 'label'
    YEAR = 'year'
    GENRE = 'genre'
    TRACK = 'track'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MusicSearchParam from a JSON string"""
        return cls(json.loads(json_str))


