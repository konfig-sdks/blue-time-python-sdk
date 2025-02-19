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

from blue_time_python_sdk.model.system_collections_generic_key_value_pair2_system_string_system_private_core_lib_version6000_cultureneutral_public_key_token7cec85d7bea7798e_system_string_system_private_core_lib_version6000_cultureneutral_public_key_token7cec85d7bea7798e import SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e as SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSchema
from blue_time_python_sdk.model.pay_tools_api_models_payment_gateway_account_input_model import PayToolsApiModelsPaymentGatewayAccountInputModel as PayToolsApiModelsPaymentGatewayAccountInputModelSchema
from blue_time_python_sdk.model.pay_tools_api_models_payment_gateway_account_full_output_model import PayToolsApiModelsPaymentGatewayAccountFullOutputModel as PayToolsApiModelsPaymentGatewayAccountFullOutputModelSchema

from blue_time_python_sdk.type.system_collections_generic_key_value_pair2_system_string_system_private_core_lib_version6000_cultureneutral_public_key_token7cec85d7bea7798e_system_string_system_private_core_lib_version6000_cultureneutral_public_key_token7cec85d7bea7798e import SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e
from blue_time_python_sdk.type.pay_tools_api_models_payment_gateway_account_full_output_model import PayToolsApiModelsPaymentGatewayAccountFullOutputModel
from blue_time_python_sdk.type.pay_tools_api_models_payment_gateway_account_input_model import PayToolsApiModelsPaymentGatewayAccountInputModel

from ...api_client import Dictionary
from blue_time_python_sdk.pydantic.pay_tools_api_models_payment_gateway_account_input_model import PayToolsApiModelsPaymentGatewayAccountInputModel as PayToolsApiModelsPaymentGatewayAccountInputModelPydantic
from blue_time_python_sdk.pydantic.system_collections_generic_key_value_pair2_system_string_system_private_core_lib_version6000_cultureneutral_public_key_token7cec85d7bea7798e_system_string_system_private_core_lib_version6000_cultureneutral_public_key_token7cec85d7bea7798e import SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e as SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798ePydantic
from blue_time_python_sdk.pydantic.pay_tools_api_models_payment_gateway_account_full_output_model import PayToolsApiModelsPaymentGatewayAccountFullOutputModel as PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic

from . import path

# Path params


class NameSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[A-Za-z0-9]{3,64}$',
        }]
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'name': typing.Union[NameSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_name = api_client.PathParameter(
    name="name",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NameSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PayToolsApiModelsPaymentGatewayAccountInputModelSchema


request_body_pay_tools_api_models_payment_gateway_account_input_model = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor200ResponseBodyApplicationJson = PayToolsApiModelsPaymentGatewayAccountFullOutputModelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PayToolsApiModelsPaymentGatewayAccountFullOutputModel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PayToolsApiModelsPaymentGatewayAccountFullOutputModel


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_or_replace_mapped_args(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if payment_gateway_name is not None:
            _body["paymentGatewayName"] = payment_gateway_name
        if credentials is not None:
            _body["credentials"] = credentials
        args.body = _body
        if name is not None:
            _path_params["name"] = name
        args.path = _path_params
        return args

    async def _aadd_or_replace_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Add or Replace a Payment Gateway Account
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_name,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/PaymentGatewayAccounts/{name}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pay_tools_api_models_payment_gateway_account_input_model.serialize(body, content_type)
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


    def _add_or_replace_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Add or Replace a Payment Gateway Account
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_name,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/PaymentGatewayAccounts/{name}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pay_tools_api_models_payment_gateway_account_input_model.serialize(body, content_type)
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


class AddOrReplaceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_or_replace(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_or_replace_mapped_args(
            name=name,
            payment_gateway_name=payment_gateway_name,
            credentials=credentials,
        )
        return await self._aadd_or_replace_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_or_replace(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_or_replace_mapped_args(
            name=name,
            payment_gateway_name=payment_gateway_name,
            credentials=credentials,
        )
        return self._add_or_replace_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddOrReplace(BaseApi):

    async def aadd_or_replace(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic:
        raw_response = await self.raw.aadd_or_replace(
            name=name,
            payment_gateway_name=payment_gateway_name,
            credentials=credentials,
            **kwargs,
        )
        if validate:
            return PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic, raw_response.body)
    
    
    def add_or_replace(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
        validate: bool = False,
    ) -> PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic:
        raw_response = self.raw.add_or_replace(
            name=name,
            payment_gateway_name=payment_gateway_name,
            credentials=credentials,
        )
        if validate:
            return PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayToolsApiModelsPaymentGatewayAccountFullOutputModelPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_or_replace_mapped_args(
            name=name,
            payment_gateway_name=payment_gateway_name,
            credentials=credentials,
        )
        return await self._aadd_or_replace_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        name: str,
        payment_gateway_name: typing.Optional[typing.Optional[str]] = None,
        credentials: typing.Optional[typing.Optional[typing.List[SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_or_replace_mapped_args(
            name=name,
            payment_gateway_name=payment_gateway_name,
            credentials=credentials,
        )
        return self._add_or_replace_oapg(
            body=args.body,
            path_params=args.path,
        )

