# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    NoneClass,
    BoolClass,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from . import path

# body param


class SchemaForRequestBodyApplicationXWwwFormUrlencoded(
    DictSchema
):
    _required_property_names = {
        "number",
        "pattern_without_delimiter",
        "byte",
        "double",
    }
    
    
    class integer(
        _SchemaValidator(
            inclusive_maximum=100,
            inclusive_minimum=10,
        ),
        IntSchema
    ):
        pass
    
    
    class int32(
        _SchemaValidator(
            inclusive_maximum=200,
            inclusive_minimum=20,
        ),
        Int32Schema
    ):
        pass
    int64 = Int64Schema
    
    
    class number(
        _SchemaValidator(
            inclusive_maximum=543.2,
            inclusive_minimum=32.1,
        ),
        NumberSchema
    ):
        pass
    
    
    class _float(
        _SchemaValidator(
            inclusive_maximum=987.6,
        ),
        Float32Schema
    ):
        pass
    locals()["float"] = _float
    del locals()['_float']
    
    
    class double(
        _SchemaValidator(
            inclusive_maximum=123.4,
            inclusive_minimum=67.8,
        ),
        Float64Schema
    ):
        pass
    
    
    class string(
        _SchemaValidator(
            regex=[{
                'pattern': r'[a-z]',  # noqa: E501
                'flags': (
                    re.IGNORECASE
                )
            }],
        ),
        StrSchema
    ):
        pass
    
    
    class pattern_without_delimiter(
        _SchemaValidator(
            regex=[{
                'pattern': r'^[A-Z].*',  # noqa: E501
            }],
        ),
        StrSchema
    ):
        pass
    byte = StrSchema
    binary = BinarySchema
    date = DateSchema
    dateTime = DateTimeSchema
    
    
    class password(
        _SchemaValidator(
            max_length=64,
            min_length=10,
        ),
        StrSchema
    ):
        pass
    callback = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        number: number,
        pattern_without_delimiter: pattern_without_delimiter,
        byte: byte,
        double: double,
        integer: typing.Union[integer, Unset] = unset,
        int32: typing.Union[int32, Unset] = unset,
        int64: typing.Union[int64, Unset] = unset,
        string: typing.Union[string, Unset] = unset,
        binary: typing.Union[binary, Unset] = unset,
        date: typing.Union[date, Unset] = unset,
        dateTime: typing.Union[dateTime, Unset] = unset,
        password: typing.Union[password, Unset] = unset,
        callback: typing.Union[callback, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaForRequestBodyApplicationXWwwFormUrlencoded':
        return super().__new__(
            cls,
            *args,
            number=number,
            pattern_without_delimiter=pattern_without_delimiter,
            byte=byte,
            double=double,
            integer=integer,
            int32=int32,
            int64=int64,
            string=string,
            binary=binary,
            date=date,
            dateTime=dateTime,
            password=password,
            callback=callback,
            _configuration=_configuration,
            **kwargs,
        )


request_body_body = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)
_auth = [
    'http_basic_test',
]


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: Unset = unset
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: Unset = unset
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
_status_code_to_response = {
    '400': _response_for_400,
    '404': _response_for_404,
}


class BaseApi(api_client.Api):

    def _endpoint_parameters(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] = unset,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling

        _fields = None
        _body = None
        if body is not unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class EndpointParameters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def endpoint_parameters(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] = unset,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._endpoint_parameters(
            body=body,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] = unset,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._endpoint_parameters(
            body=body,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


