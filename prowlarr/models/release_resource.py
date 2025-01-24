# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.30.2.4939
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from prowlarr.models.download_protocol import DownloadProtocol
from prowlarr.models.indexer_category import IndexerCategory
from typing import Optional, Set
from typing_extensions import Self

class ReleaseResource(BaseModel):
    """
    ReleaseResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    guid: Optional[StrictStr] = None
    age: Optional[StrictInt] = None
    age_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageHours")
    age_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageMinutes")
    size: Optional[StrictInt] = None
    files: Optional[StrictInt] = None
    grabs: Optional[StrictInt] = None
    indexer_id: Optional[StrictInt] = Field(default=None, alias="indexerId")
    indexer: Optional[StrictStr] = None
    sub_group: Optional[StrictStr] = Field(default=None, alias="subGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    title: Optional[StrictStr] = None
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    imdb_id: Optional[StrictInt] = Field(default=None, alias="imdbId")
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    tvdb_id: Optional[StrictInt] = Field(default=None, alias="tvdbId")
    tv_maze_id: Optional[StrictInt] = Field(default=None, alias="tvMazeId")
    publish_date: Optional[datetime] = Field(default=None, alias="publishDate")
    comment_url: Optional[StrictStr] = Field(default=None, alias="commentUrl")
    download_url: Optional[StrictStr] = Field(default=None, alias="downloadUrl")
    info_url: Optional[StrictStr] = Field(default=None, alias="infoUrl")
    poster_url: Optional[StrictStr] = Field(default=None, alias="posterUrl")
    indexer_flags: Optional[List[StrictStr]] = Field(default=None, alias="indexerFlags")
    categories: Optional[List[IndexerCategory]] = None
    magnet_url: Optional[StrictStr] = Field(default=None, alias="magnetUrl")
    info_hash: Optional[StrictStr] = Field(default=None, alias="infoHash")
    seeders: Optional[StrictInt] = None
    leechers: Optional[StrictInt] = None
    protocol: Optional[DownloadProtocol] = None
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    download_client_id: Optional[StrictInt] = Field(default=None, alias="downloadClientId")
    __properties: ClassVar[List[str]] = ["id", "guid", "age", "ageHours", "ageMinutes", "size", "files", "grabs", "indexerId", "indexer", "subGroup", "releaseHash", "title", "sortTitle", "imdbId", "tmdbId", "tvdbId", "tvMazeId", "publishDate", "commentUrl", "downloadUrl", "infoUrl", "posterUrl", "indexerFlags", "categories", "magnetUrl", "infoHash", "seeders", "leechers", "protocol", "fileName", "downloadClientId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReleaseResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "file_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['categories'] = _items
        # set to None if guid (nullable) is None
        # and model_fields_set contains the field
        if self.guid is None and "guid" in self.model_fields_set:
            _dict['guid'] = None

        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and "files" in self.model_fields_set:
            _dict['files'] = None

        # set to None if grabs (nullable) is None
        # and model_fields_set contains the field
        if self.grabs is None and "grabs" in self.model_fields_set:
            _dict['grabs'] = None

        # set to None if indexer (nullable) is None
        # and model_fields_set contains the field
        if self.indexer is None and "indexer" in self.model_fields_set:
            _dict['indexer'] = None

        # set to None if sub_group (nullable) is None
        # and model_fields_set contains the field
        if self.sub_group is None and "sub_group" in self.model_fields_set:
            _dict['subGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if sort_title (nullable) is None
        # and model_fields_set contains the field
        if self.sort_title is None and "sort_title" in self.model_fields_set:
            _dict['sortTitle'] = None

        # set to None if comment_url (nullable) is None
        # and model_fields_set contains the field
        if self.comment_url is None and "comment_url" in self.model_fields_set:
            _dict['commentUrl'] = None

        # set to None if download_url (nullable) is None
        # and model_fields_set contains the field
        if self.download_url is None and "download_url" in self.model_fields_set:
            _dict['downloadUrl'] = None

        # set to None if info_url (nullable) is None
        # and model_fields_set contains the field
        if self.info_url is None and "info_url" in self.model_fields_set:
            _dict['infoUrl'] = None

        # set to None if poster_url (nullable) is None
        # and model_fields_set contains the field
        if self.poster_url is None and "poster_url" in self.model_fields_set:
            _dict['posterUrl'] = None

        # set to None if indexer_flags (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_flags is None and "indexer_flags" in self.model_fields_set:
            _dict['indexerFlags'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if magnet_url (nullable) is None
        # and model_fields_set contains the field
        if self.magnet_url is None and "magnet_url" in self.model_fields_set:
            _dict['magnetUrl'] = None

        # set to None if info_hash (nullable) is None
        # and model_fields_set contains the field
        if self.info_hash is None and "info_hash" in self.model_fields_set:
            _dict['infoHash'] = None

        # set to None if seeders (nullable) is None
        # and model_fields_set contains the field
        if self.seeders is None and "seeders" in self.model_fields_set:
            _dict['seeders'] = None

        # set to None if leechers (nullable) is None
        # and model_fields_set contains the field
        if self.leechers is None and "leechers" in self.model_fields_set:
            _dict['leechers'] = None

        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['fileName'] = None

        # set to None if download_client_id (nullable) is None
        # and model_fields_set contains the field
        if self.download_client_id is None and "download_client_id" in self.model_fields_set:
            _dict['downloadClientId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReleaseResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "guid": obj.get("guid"),
            "age": obj.get("age"),
            "ageHours": obj.get("ageHours"),
            "ageMinutes": obj.get("ageMinutes"),
            "size": obj.get("size"),
            "files": obj.get("files"),
            "grabs": obj.get("grabs"),
            "indexerId": obj.get("indexerId"),
            "indexer": obj.get("indexer"),
            "subGroup": obj.get("subGroup"),
            "releaseHash": obj.get("releaseHash"),
            "title": obj.get("title"),
            "sortTitle": obj.get("sortTitle"),
            "imdbId": obj.get("imdbId"),
            "tmdbId": obj.get("tmdbId"),
            "tvdbId": obj.get("tvdbId"),
            "tvMazeId": obj.get("tvMazeId"),
            "publishDate": obj.get("publishDate"),
            "commentUrl": obj.get("commentUrl"),
            "downloadUrl": obj.get("downloadUrl"),
            "infoUrl": obj.get("infoUrl"),
            "posterUrl": obj.get("posterUrl"),
            "indexerFlags": obj.get("indexerFlags"),
            "categories": [IndexerCategory.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
            "magnetUrl": obj.get("magnetUrl"),
            "infoHash": obj.get("infoHash"),
            "seeders": obj.get("seeders"),
            "leechers": obj.get("leechers"),
            "protocol": obj.get("protocol"),
            "fileName": obj.get("fileName"),
            "downloadClientId": obj.get("downloadClientId")
        })
        return _obj


