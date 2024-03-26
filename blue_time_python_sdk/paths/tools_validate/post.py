# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from blue_time_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from blue_time_python_sdk.api_response import AsyncGeneratorResponse
from blue_time_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from blue_time_python_sdk import schemas  # noqa: F401

from blue_time_python_sdk.model.pay_tools_api_models_payer_base_with_client_ip import PayToolsApiModelsPayerBaseWithClientIp as PayToolsApiModelsPayerBaseWithClientIpSchema
from blue_time_python_sdk.model.pay_tools_api_models_card_validation_results import PayToolsApiModelsCardValidationResults as PayToolsApiModelsCardValidationResultsSchema

from blue_time_python_sdk.type.pay_tools_api_models_card_validation_results import PayToolsApiModelsCardValidationResults
from blue_time_python_sdk.type.pay_tools_api_models_payer_base_with_client_ip import PayToolsApiModelsPayerBaseWithClientIp

from ...api_client import Dictionary
from blue_time_python_sdk.pydantic.pay_tools_api_models_card_validation_results import PayToolsApiModelsCardValidationResults as PayToolsApiModelsCardValidationResultsPydantic
from blue_time_python_sdk.pydantic.pay_tools_api_models_payer_base_with_client_ip import PayToolsApiModelsPayerBaseWithClientIp as PayToolsApiModelsPayerBaseWithClientIpPydantic

from . import path

# Query params


class IinSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'\d{6,11}',
        }]
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'iin': typing.Union[IinSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_iin = api_client.QueryParameter(
    name="iin",
    style=api_client.ParameterStyle.FORM,
    schema=IinSchema,
    required=True,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = PayToolsApiModelsPayerBaseWithClientIpSchema


request_body_pay_tools_api_models_payer_base_with_client_ip = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor200ResponseBodyApplicationJson = PayToolsApiModelsCardValidationResultsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PayToolsApiModelsCardValidationResults


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PayToolsApiModelsCardValidationResults


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _validate_card_details_mapped_args(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if client_ip_address is not None:
            _body["clientIPAddress"] = client_ip_address
        if city is not None:
            _body["city"] = city
        if state_province is not None:
            _body["stateProvince"] = state_province
        if country_code is not None:
            _body["countryCode"] = country_code
        args.body = _body
        if iin is not None:
            _query_params["iin"] = iin
        args.query = _query_params
        return args

    async def _avalidate_card_details_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Card Validation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_iin,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Tools/validate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pay_tools_api_models_payer_base_with_client_ip.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _validate_card_details_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Card Validation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_iin,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Tools/validate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pay_tools_api_models_payer_base_with_client_ip.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ValidateCardDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avalidate_card_details(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validate_card_details_mapped_args(
            client_ip_address=client_ip_address,
            country_code=country_code,
            iin=iin,
            city=city,
            state_province=state_province,
        )
        return await self._avalidate_card_details_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def validate_card_details(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validate_card_details_mapped_args(
            client_ip_address=client_ip_address,
            country_code=country_code,
            iin=iin,
            city=city,
            state_province=state_province,
        )
        return self._validate_card_details_oapg(
            body=args.body,
            query_params=args.query,
        )

class ValidateCardDetails(BaseApi):

    async def avalidate_card_details(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PayToolsApiModelsCardValidationResultsPydantic:
        raw_response = await self.raw.avalidate_card_details(
            client_ip_address=client_ip_address,
            country_code=country_code,
            iin=iin,
            city=city,
            state_province=state_province,
            **kwargs,
        )
        if validate:
            return PayToolsApiModelsCardValidationResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayToolsApiModelsCardValidationResultsPydantic, raw_response.body)
    
    
    def validate_card_details(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> PayToolsApiModelsCardValidationResultsPydantic:
        raw_response = self.raw.validate_card_details(
            client_ip_address=client_ip_address,
            country_code=country_code,
            iin=iin,
            city=city,
            state_province=state_province,
        )
        if validate:
            return PayToolsApiModelsCardValidationResultsPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayToolsApiModelsCardValidationResultsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validate_card_details_mapped_args(
            client_ip_address=client_ip_address,
            country_code=country_code,
            iin=iin,
            city=city,
            state_province=state_province,
        )
        return await self._avalidate_card_details_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        client_ip_address: str,
        country_code: str,
        iin: str,
        city: typing.Optional[typing.Optional[str]] = None,
        state_province: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validate_card_details_mapped_args(
            client_ip_address=client_ip_address,
            country_code=country_code,
            iin=iin,
            city=city,
            state_province=state_province,
        )
        return self._validate_card_details_oapg(
            body=args.body,
            query_params=args.query,
        )

