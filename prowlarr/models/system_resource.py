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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from prowlarr.models.authentication_type import AuthenticationType
from prowlarr.models.database_type import DatabaseType
from prowlarr.models.runtime_mode import RuntimeMode
from prowlarr.models.update_mechanism import UpdateMechanism

class SystemResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    app_name: Optional[str]
    instance_name: Optional[str]
    version: Optional[str]
    build_time: Optional[datetime]
    is_debug: Optional[bool]
    is_production: Optional[bool]
    is_admin: Optional[bool]
    is_user_interactive: Optional[bool]
    startup_path: Optional[str]
    app_data: Optional[str]
    os_name: Optional[str]
    os_version: Optional[str]
    is_net_core: Optional[bool]
    is_linux: Optional[bool]
    is_osx: Optional[bool]
    is_windows: Optional[bool]
    is_docker: Optional[bool]
    mode: Optional[RuntimeMode]
    branch: Optional[str]
    database_type: Optional[DatabaseType]
    database_version: Optional[str]
    authentication: Optional[AuthenticationType]
    migration_version: Optional[int]
    url_base: Optional[str]
    runtime_version: Optional[str]
    runtime_name: Optional[str]
    start_time: Optional[datetime]
    package_version: Optional[str]
    package_author: Optional[str]
    package_update_mechanism: Optional[UpdateMechanism]
    package_update_mechanism_message: Optional[str]
    __properties = ["appName", "instanceName", "version", "buildTime", "isDebug", "isProduction", "isAdmin", "isUserInteractive", "startupPath", "appData", "osName", "osVersion", "isNetCore", "isLinux", "isOsx", "isWindows", "isDocker", "mode", "branch", "databaseType", "databaseVersion", "authentication", "migrationVersion", "urlBase", "runtimeVersion", "runtimeName", "startTime", "packageVersion", "packageAuthor", "packageUpdateMechanism", "packageUpdateMechanismMessage"]

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
    def from_json(cls, json_str: str) -> SystemResource:
        """Create an instance of SystemResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if app_name (nullable) is None
        if self.app_name is None:
            _dict['appName'] = None

        # set to None if instance_name (nullable) is None
        if self.instance_name is None:
            _dict['instanceName'] = None

        # set to None if version (nullable) is None
        if self.version is None:
            _dict['version'] = None

        # set to None if startup_path (nullable) is None
        if self.startup_path is None:
            _dict['startupPath'] = None

        # set to None if app_data (nullable) is None
        if self.app_data is None:
            _dict['appData'] = None

        # set to None if os_name (nullable) is None
        if self.os_name is None:
            _dict['osName'] = None

        # set to None if os_version (nullable) is None
        if self.os_version is None:
            _dict['osVersion'] = None

        # set to None if branch (nullable) is None
        if self.branch is None:
            _dict['branch'] = None

        # set to None if url_base (nullable) is None
        if self.url_base is None:
            _dict['urlBase'] = None

        # set to None if runtime_name (nullable) is None
        if self.runtime_name is None:
            _dict['runtimeName'] = None

        # set to None if package_version (nullable) is None
        if self.package_version is None:
            _dict['packageVersion'] = None

        # set to None if package_author (nullable) is None
        if self.package_author is None:
            _dict['packageAuthor'] = None

        # set to None if package_update_mechanism_message (nullable) is None
        if self.package_update_mechanism_message is None:
            _dict['packageUpdateMechanismMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemResource:
        """Create an instance of SystemResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SystemResource.parse_obj(obj)

        _obj = SystemResource.parse_obj({
            "app_name": obj.get("appName"),
            "instance_name": obj.get("instanceName"),
            "version": obj.get("version"),
            "build_time": obj.get("buildTime"),
            "is_debug": obj.get("isDebug"),
            "is_production": obj.get("isProduction"),
            "is_admin": obj.get("isAdmin"),
            "is_user_interactive": obj.get("isUserInteractive"),
            "startup_path": obj.get("startupPath"),
            "app_data": obj.get("appData"),
            "os_name": obj.get("osName"),
            "os_version": obj.get("osVersion"),
            "is_net_core": obj.get("isNetCore"),
            "is_linux": obj.get("isLinux"),
            "is_osx": obj.get("isOsx"),
            "is_windows": obj.get("isWindows"),
            "is_docker": obj.get("isDocker"),
            "mode": obj.get("mode"),
            "branch": obj.get("branch"),
            "database_type": obj.get("databaseType"),
            "database_version": obj.get("databaseVersion"),
            "authentication": obj.get("authentication"),
            "migration_version": obj.get("migrationVersion"),
            "url_base": obj.get("urlBase"),
            "runtime_version": obj.get("runtimeVersion"),
            "runtime_name": obj.get("runtimeName"),
            "start_time": obj.get("startTime"),
            "package_version": obj.get("packageVersion"),
            "package_author": obj.get("packageAuthor"),
            "package_update_mechanism": obj.get("packageUpdateMechanism"),
            "package_update_mechanism_message": obj.get("packageUpdateMechanismMessage")
        })
        return _obj

