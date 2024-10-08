# coding: utf-8

"""
    Prowlarr

    Prowlarr API docs

    The version of the OpenAPI document: v1.23.1.4708
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictInt, StrictStr
from typing import Optional

from prowlarr.api_client import ApiClient, RequestSerialized
from prowlarr.api_response import ApiResponse
from prowlarr.rest import RESTResponseType


class NewznabApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_indexer_download(
        self,
        id: StrictInt,
        link: Optional[StrictStr] = None,
        file: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """get_indexer_download


        :param id: (required)
        :type id: int
        :param link:
        :type link: str
        :param file:
        :type file: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_indexer_download_serialize(
            id=id,
            link=link,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_indexer_download_with_http_info(
        self,
        id: StrictInt,
        link: Optional[StrictStr] = None,
        file: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """get_indexer_download


        :param id: (required)
        :type id: int
        :param link:
        :type link: str
        :param file:
        :type file: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_indexer_download_serialize(
            id=id,
            link=link,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_indexer_download_without_preload_content(
        self,
        id: StrictInt,
        link: Optional[StrictStr] = None,
        file: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """get_indexer_download


        :param id: (required)
        :type id: int
        :param link:
        :type link: str
        :param file:
        :type file: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_indexer_download_serialize(
            id=id,
            link=link,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_indexer_download_serialize(
        self,
        id,
        link,
        file,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if link is not None:
            
            _query_params.append(('link', link))
            
        if file is not None:
            
            _query_params.append(('file', file))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apikey', 
            'X-Api-Key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/indexer/{id}/download',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_indexer_newznab(
        self,
        id: StrictInt,
        t: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        cat: Optional[StrictStr] = None,
        imdbid: Optional[StrictStr] = None,
        tmdbid: Optional[StrictInt] = None,
        extended: Optional[StrictStr] = None,
        limit: Optional[StrictInt] = None,
        offset: Optional[StrictInt] = None,
        minage: Optional[StrictInt] = None,
        maxage: Optional[StrictInt] = None,
        minsize: Optional[StrictInt] = None,
        maxsize: Optional[StrictInt] = None,
        rid: Optional[StrictInt] = None,
        tvmazeid: Optional[StrictInt] = None,
        traktid: Optional[StrictInt] = None,
        tvdbid: Optional[StrictInt] = None,
        doubanid: Optional[StrictInt] = None,
        season: Optional[StrictInt] = None,
        ep: Optional[StrictStr] = None,
        album: Optional[StrictStr] = None,
        artist: Optional[StrictStr] = None,
        label: Optional[StrictStr] = None,
        track: Optional[StrictStr] = None,
        year: Optional[StrictInt] = None,
        genre: Optional[StrictStr] = None,
        author: Optional[StrictStr] = None,
        title: Optional[StrictStr] = None,
        publisher: Optional[StrictStr] = None,
        configured: Optional[StrictStr] = None,
        source: Optional[StrictStr] = None,
        host: Optional[StrictStr] = None,
        server: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """get_indexer_newznab


        :param id: (required)
        :type id: int
        :param t:
        :type t: str
        :param q:
        :type q: str
        :param cat:
        :type cat: str
        :param imdbid:
        :type imdbid: str
        :param tmdbid:
        :type tmdbid: int
        :param extended:
        :type extended: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param minage:
        :type minage: int
        :param maxage:
        :type maxage: int
        :param minsize:
        :type minsize: int
        :param maxsize:
        :type maxsize: int
        :param rid:
        :type rid: int
        :param tvmazeid:
        :type tvmazeid: int
        :param traktid:
        :type traktid: int
        :param tvdbid:
        :type tvdbid: int
        :param doubanid:
        :type doubanid: int
        :param season:
        :type season: int
        :param ep:
        :type ep: str
        :param album:
        :type album: str
        :param artist:
        :type artist: str
        :param label:
        :type label: str
        :param track:
        :type track: str
        :param year:
        :type year: int
        :param genre:
        :type genre: str
        :param author:
        :type author: str
        :param title:
        :type title: str
        :param publisher:
        :type publisher: str
        :param configured:
        :type configured: str
        :param source:
        :type source: str
        :param host:
        :type host: str
        :param server:
        :type server: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_indexer_newznab_serialize(
            id=id,
            t=t,
            q=q,
            cat=cat,
            imdbid=imdbid,
            tmdbid=tmdbid,
            extended=extended,
            limit=limit,
            offset=offset,
            minage=minage,
            maxage=maxage,
            minsize=minsize,
            maxsize=maxsize,
            rid=rid,
            tvmazeid=tvmazeid,
            traktid=traktid,
            tvdbid=tvdbid,
            doubanid=doubanid,
            season=season,
            ep=ep,
            album=album,
            artist=artist,
            label=label,
            track=track,
            year=year,
            genre=genre,
            author=author,
            title=title,
            publisher=publisher,
            configured=configured,
            source=source,
            host=host,
            server=server,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_indexer_newznab_with_http_info(
        self,
        id: StrictInt,
        t: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        cat: Optional[StrictStr] = None,
        imdbid: Optional[StrictStr] = None,
        tmdbid: Optional[StrictInt] = None,
        extended: Optional[StrictStr] = None,
        limit: Optional[StrictInt] = None,
        offset: Optional[StrictInt] = None,
        minage: Optional[StrictInt] = None,
        maxage: Optional[StrictInt] = None,
        minsize: Optional[StrictInt] = None,
        maxsize: Optional[StrictInt] = None,
        rid: Optional[StrictInt] = None,
        tvmazeid: Optional[StrictInt] = None,
        traktid: Optional[StrictInt] = None,
        tvdbid: Optional[StrictInt] = None,
        doubanid: Optional[StrictInt] = None,
        season: Optional[StrictInt] = None,
        ep: Optional[StrictStr] = None,
        album: Optional[StrictStr] = None,
        artist: Optional[StrictStr] = None,
        label: Optional[StrictStr] = None,
        track: Optional[StrictStr] = None,
        year: Optional[StrictInt] = None,
        genre: Optional[StrictStr] = None,
        author: Optional[StrictStr] = None,
        title: Optional[StrictStr] = None,
        publisher: Optional[StrictStr] = None,
        configured: Optional[StrictStr] = None,
        source: Optional[StrictStr] = None,
        host: Optional[StrictStr] = None,
        server: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """get_indexer_newznab


        :param id: (required)
        :type id: int
        :param t:
        :type t: str
        :param q:
        :type q: str
        :param cat:
        :type cat: str
        :param imdbid:
        :type imdbid: str
        :param tmdbid:
        :type tmdbid: int
        :param extended:
        :type extended: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param minage:
        :type minage: int
        :param maxage:
        :type maxage: int
        :param minsize:
        :type minsize: int
        :param maxsize:
        :type maxsize: int
        :param rid:
        :type rid: int
        :param tvmazeid:
        :type tvmazeid: int
        :param traktid:
        :type traktid: int
        :param tvdbid:
        :type tvdbid: int
        :param doubanid:
        :type doubanid: int
        :param season:
        :type season: int
        :param ep:
        :type ep: str
        :param album:
        :type album: str
        :param artist:
        :type artist: str
        :param label:
        :type label: str
        :param track:
        :type track: str
        :param year:
        :type year: int
        :param genre:
        :type genre: str
        :param author:
        :type author: str
        :param title:
        :type title: str
        :param publisher:
        :type publisher: str
        :param configured:
        :type configured: str
        :param source:
        :type source: str
        :param host:
        :type host: str
        :param server:
        :type server: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_indexer_newznab_serialize(
            id=id,
            t=t,
            q=q,
            cat=cat,
            imdbid=imdbid,
            tmdbid=tmdbid,
            extended=extended,
            limit=limit,
            offset=offset,
            minage=minage,
            maxage=maxage,
            minsize=minsize,
            maxsize=maxsize,
            rid=rid,
            tvmazeid=tvmazeid,
            traktid=traktid,
            tvdbid=tvdbid,
            doubanid=doubanid,
            season=season,
            ep=ep,
            album=album,
            artist=artist,
            label=label,
            track=track,
            year=year,
            genre=genre,
            author=author,
            title=title,
            publisher=publisher,
            configured=configured,
            source=source,
            host=host,
            server=server,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_indexer_newznab_without_preload_content(
        self,
        id: StrictInt,
        t: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        cat: Optional[StrictStr] = None,
        imdbid: Optional[StrictStr] = None,
        tmdbid: Optional[StrictInt] = None,
        extended: Optional[StrictStr] = None,
        limit: Optional[StrictInt] = None,
        offset: Optional[StrictInt] = None,
        minage: Optional[StrictInt] = None,
        maxage: Optional[StrictInt] = None,
        minsize: Optional[StrictInt] = None,
        maxsize: Optional[StrictInt] = None,
        rid: Optional[StrictInt] = None,
        tvmazeid: Optional[StrictInt] = None,
        traktid: Optional[StrictInt] = None,
        tvdbid: Optional[StrictInt] = None,
        doubanid: Optional[StrictInt] = None,
        season: Optional[StrictInt] = None,
        ep: Optional[StrictStr] = None,
        album: Optional[StrictStr] = None,
        artist: Optional[StrictStr] = None,
        label: Optional[StrictStr] = None,
        track: Optional[StrictStr] = None,
        year: Optional[StrictInt] = None,
        genre: Optional[StrictStr] = None,
        author: Optional[StrictStr] = None,
        title: Optional[StrictStr] = None,
        publisher: Optional[StrictStr] = None,
        configured: Optional[StrictStr] = None,
        source: Optional[StrictStr] = None,
        host: Optional[StrictStr] = None,
        server: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """get_indexer_newznab


        :param id: (required)
        :type id: int
        :param t:
        :type t: str
        :param q:
        :type q: str
        :param cat:
        :type cat: str
        :param imdbid:
        :type imdbid: str
        :param tmdbid:
        :type tmdbid: int
        :param extended:
        :type extended: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param minage:
        :type minage: int
        :param maxage:
        :type maxage: int
        :param minsize:
        :type minsize: int
        :param maxsize:
        :type maxsize: int
        :param rid:
        :type rid: int
        :param tvmazeid:
        :type tvmazeid: int
        :param traktid:
        :type traktid: int
        :param tvdbid:
        :type tvdbid: int
        :param doubanid:
        :type doubanid: int
        :param season:
        :type season: int
        :param ep:
        :type ep: str
        :param album:
        :type album: str
        :param artist:
        :type artist: str
        :param label:
        :type label: str
        :param track:
        :type track: str
        :param year:
        :type year: int
        :param genre:
        :type genre: str
        :param author:
        :type author: str
        :param title:
        :type title: str
        :param publisher:
        :type publisher: str
        :param configured:
        :type configured: str
        :param source:
        :type source: str
        :param host:
        :type host: str
        :param server:
        :type server: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_indexer_newznab_serialize(
            id=id,
            t=t,
            q=q,
            cat=cat,
            imdbid=imdbid,
            tmdbid=tmdbid,
            extended=extended,
            limit=limit,
            offset=offset,
            minage=minage,
            maxage=maxage,
            minsize=minsize,
            maxsize=maxsize,
            rid=rid,
            tvmazeid=tvmazeid,
            traktid=traktid,
            tvdbid=tvdbid,
            doubanid=doubanid,
            season=season,
            ep=ep,
            album=album,
            artist=artist,
            label=label,
            track=track,
            year=year,
            genre=genre,
            author=author,
            title=title,
            publisher=publisher,
            configured=configured,
            source=source,
            host=host,
            server=server,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_indexer_newznab_serialize(
        self,
        id,
        t,
        q,
        cat,
        imdbid,
        tmdbid,
        extended,
        limit,
        offset,
        minage,
        maxage,
        minsize,
        maxsize,
        rid,
        tvmazeid,
        traktid,
        tvdbid,
        doubanid,
        season,
        ep,
        album,
        artist,
        label,
        track,
        year,
        genre,
        author,
        title,
        publisher,
        configured,
        source,
        host,
        server,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if t is not None:
            
            _query_params.append(('t', t))
            
        if q is not None:
            
            _query_params.append(('q', q))
            
        if cat is not None:
            
            _query_params.append(('cat', cat))
            
        if imdbid is not None:
            
            _query_params.append(('imdbid', imdbid))
            
        if tmdbid is not None:
            
            _query_params.append(('tmdbid', tmdbid))
            
        if extended is not None:
            
            _query_params.append(('extended', extended))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if minage is not None:
            
            _query_params.append(('minage', minage))
            
        if maxage is not None:
            
            _query_params.append(('maxage', maxage))
            
        if minsize is not None:
            
            _query_params.append(('minsize', minsize))
            
        if maxsize is not None:
            
            _query_params.append(('maxsize', maxsize))
            
        if rid is not None:
            
            _query_params.append(('rid', rid))
            
        if tvmazeid is not None:
            
            _query_params.append(('tvmazeid', tvmazeid))
            
        if traktid is not None:
            
            _query_params.append(('traktid', traktid))
            
        if tvdbid is not None:
            
            _query_params.append(('tvdbid', tvdbid))
            
        if doubanid is not None:
            
            _query_params.append(('doubanid', doubanid))
            
        if season is not None:
            
            _query_params.append(('season', season))
            
        if ep is not None:
            
            _query_params.append(('ep', ep))
            
        if album is not None:
            
            _query_params.append(('album', album))
            
        if artist is not None:
            
            _query_params.append(('artist', artist))
            
        if label is not None:
            
            _query_params.append(('label', label))
            
        if track is not None:
            
            _query_params.append(('track', track))
            
        if year is not None:
            
            _query_params.append(('year', year))
            
        if genre is not None:
            
            _query_params.append(('genre', genre))
            
        if author is not None:
            
            _query_params.append(('author', author))
            
        if title is not None:
            
            _query_params.append(('title', title))
            
        if publisher is not None:
            
            _query_params.append(('publisher', publisher))
            
        if configured is not None:
            
            _query_params.append(('configured', configured))
            
        if source is not None:
            
            _query_params.append(('source', source))
            
        if host is not None:
            
            _query_params.append(('host', host))
            
        if server is not None:
            
            _query_params.append(('server', server))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apikey', 
            'X-Api-Key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/indexer/{id}/newznab',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


