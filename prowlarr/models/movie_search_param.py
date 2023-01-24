# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MovieSearchParam(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    Q = 'q'
    IMDB_ID = 'imdbId'
    TMDB_ID = 'tmdbId'
    IMDB_TITLE = 'imdbTitle'
    IMDB_YEAR = 'imdbYear'
    TRAKT_ID = 'traktId'
    GENRE = 'genre'
    DOUBAN_ID = 'doubanId'
    YEAR = 'year'

