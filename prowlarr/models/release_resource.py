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



from pydantic import BaseModel
from prowlarr.models.download_protocol import DownloadProtocol
from prowlarr.models.indexer_category import IndexerCategory

class ReleaseResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    guid: Optional[str]
    age: Optional[int]
    age_hours: Optional[float]
    age_minutes: Optional[float]
    size: Optional[int]
    files: Optional[int]
    grabs: Optional[int]
    indexer_id: Optional[int]
    indexer: Optional[str]
    sub_group: Optional[str]
    release_hash: Optional[str]
    title: Optional[str]
    sort_title: Optional[str]
    imdb_id: Optional[int]
    tmdb_id: Optional[int]
    tvdb_id: Optional[int]
    tv_maze_id: Optional[int]
    publish_date: Optional[datetime]
    comment_url: Optional[str]
    download_url: Optional[str]
    info_url: Optional[str]
    poster_url: Optional[str]
    indexer_flags: Optional[List]
    categories: Optional[List]
    magnet_url: Optional[str]
    info_hash: Optional[str]
    seeders: Optional[int]
    leechers: Optional[int]
    protocol: Optional[DownloadProtocol]
    file_name: Optional[str]
    __properties = ["id", "guid", "age", "ageHours", "ageMinutes", "size", "files", "grabs", "indexerId", "indexer", "subGroup", "releaseHash", "title", "sortTitle", "imdbId", "tmdbId", "tvdbId", "tvMazeId", "publishDate", "commentUrl", "downloadUrl", "infoUrl", "posterUrl", "indexerFlags", "categories", "magnetUrl", "infoHash", "seeders", "leechers", "protocol", "fileName"]

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
    def from_json(cls, json_str: str) -> ReleaseResource:
        """Create an instance of ReleaseResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "file_name",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # set to None if guid (nullable) is None
        if self.guid is None:
            _dict['guid'] = None

        # set to None if files (nullable) is None
        if self.files is None:
            _dict['files'] = None

        # set to None if grabs (nullable) is None
        if self.grabs is None:
            _dict['grabs'] = None

        # set to None if indexer (nullable) is None
        if self.indexer is None:
            _dict['indexer'] = None

        # set to None if sub_group (nullable) is None
        if self.sub_group is None:
            _dict['subGroup'] = None

        # set to None if release_hash (nullable) is None
        if self.release_hash is None:
            _dict['releaseHash'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if sort_title (nullable) is None
        if self.sort_title is None:
            _dict['sortTitle'] = None

        # set to None if comment_url (nullable) is None
        if self.comment_url is None:
            _dict['commentUrl'] = None

        # set to None if download_url (nullable) is None
        if self.download_url is None:
            _dict['downloadUrl'] = None

        # set to None if info_url (nullable) is None
        if self.info_url is None:
            _dict['infoUrl'] = None

        # set to None if poster_url (nullable) is None
        if self.poster_url is None:
            _dict['posterUrl'] = None

        # set to None if indexer_flags (nullable) is None
        if self.indexer_flags is None:
            _dict['indexerFlags'] = None

        # set to None if categories (nullable) is None
        if self.categories is None:
            _dict['categories'] = None

        # set to None if magnet_url (nullable) is None
        if self.magnet_url is None:
            _dict['magnetUrl'] = None

        # set to None if info_hash (nullable) is None
        if self.info_hash is None:
            _dict['infoHash'] = None

        # set to None if seeders (nullable) is None
        if self.seeders is None:
            _dict['seeders'] = None

        # set to None if leechers (nullable) is None
        if self.leechers is None:
            _dict['leechers'] = None

        # set to None if file_name (nullable) is None
        if self.file_name is None:
            _dict['fileName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReleaseResource:
        """Create an instance of ReleaseResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReleaseResource.parse_obj(obj)

        _obj = ReleaseResource.parse_obj({
            "id": obj.get("id"),
            "guid": obj.get("guid"),
            "age": obj.get("age"),
            "age_hours": obj.get("ageHours"),
            "age_minutes": obj.get("ageMinutes"),
            "size": obj.get("size"),
            "files": obj.get("files"),
            "grabs": obj.get("grabs"),
            "indexer_id": obj.get("indexerId"),
            "indexer": obj.get("indexer"),
            "sub_group": obj.get("subGroup"),
            "release_hash": obj.get("releaseHash"),
            "title": obj.get("title"),
            "sort_title": obj.get("sortTitle"),
            "imdb_id": obj.get("imdbId"),
            "tmdb_id": obj.get("tmdbId"),
            "tvdb_id": obj.get("tvdbId"),
            "tv_maze_id": obj.get("tvMazeId"),
            "publish_date": obj.get("publishDate"),
            "comment_url": obj.get("commentUrl"),
            "download_url": obj.get("downloadUrl"),
            "info_url": obj.get("infoUrl"),
            "poster_url": obj.get("posterUrl"),
            "indexer_flags": obj.get("indexerFlags"),
            "categories": [IndexerCategory.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None,
            "magnet_url": obj.get("magnetUrl"),
            "info_hash": obj.get("infoHash"),
            "seeders": obj.get("seeders"),
            "leechers": obj.get("leechers"),
            "protocol": obj.get("protocol"),
            "file_name": obj.get("fileName")
        })
        return _obj

