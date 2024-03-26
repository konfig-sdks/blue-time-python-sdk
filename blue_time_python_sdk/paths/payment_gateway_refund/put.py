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

from blue_time_python_sdk.model.payments_operation_result import PaymentsOperationResult as PaymentsOperationResultSchema
from blue_time_python_sdk.model.payments_network_token_schemes import PaymentsNetworkTokenSchemes as PaymentsNetworkTokenSchemesSchema
from blue_time_python_sdk.model.pay_tools_api_models_card_input_model import PayToolsApiModelsCardInputModel as PayToolsApiModelsCardInputModelSchema
from blue_time_python_sdk.model.pay_tools_api_models_payment_gateway_account import PayToolsApiModelsPaymentGatewayAccount as PayToolsApiModelsPaymentGatewayAccountSchema
from blue_time_python_sdk.model.pay_tools_api_models_refund_request_model import PayToolsApiModelsRefundRequestModel as PayToolsApiModelsRefundRequestModelSchema
from blue_time_python_sdk.model.pay_tools_api_models_payer_details import PayToolsApiModelsPayerDetails as PayToolsApiModelsPayerDetailsSchema

from blue_time_python_sdk.type.payments_network_token_schemes import PaymentsNetworkTokenSchemes
from blue_time_python_sdk.type.pay_tools_api_models_payment_gateway_account import PayToolsApiModelsPaymentGatewayAccount
from blue_time_python_sdk.type.pay_tools_api_models_refund_request_model import PayToolsApiModelsRefundRequestModel
from blue_time_python_sdk.type.payments_operation_result import PaymentsOperationResult
from blue_time_python_sdk.type.pay_tools_api_models_payer_details import PayToolsApiModelsPayerDetails
from blue_time_python_sdk.type.pay_tools_api_models_card_input_model import PayToolsApiModelsCardInputModel

from ...api_client import Dictionary
from blue_time_python_sdk.pydantic.pay_tools_api_models_payer_details import PayToolsApiModelsPayerDetails as PayToolsApiModelsPayerDetailsPydantic
from blue_time_python_sdk.pydantic.pay_tools_api_models_payment_gateway_account import PayToolsApiModelsPaymentGatewayAccount as PayToolsApiModelsPaymentGatewayAccountPydantic
from blue_time_python_sdk.pydantic.payments_operation_result import PaymentsOperationResult as PaymentsOperationResultPydantic
from blue_time_python_sdk.pydantic.pay_tools_api_models_card_input_model import PayToolsApiModelsCardInputModel as PayToolsApiModelsCardInputModelPydantic
from blue_time_python_sdk.pydantic.pay_tools_api_models_refund_request_model import PayToolsApiModelsRefundRequestModel as PayToolsApiModelsRefundRequestModelPydantic
from blue_time_python_sdk.pydantic.payments_network_token_schemes import PaymentsNetworkTokenSchemes as PaymentsNetworkTokenSchemesPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = PayToolsApiModelsRefundRequestModelSchema


request_body_pay_tools_api_models_refund_request_model = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor200ResponseBodyApplicationJson = PaymentsOperationResultSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentsOperationResult


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentsOperationResult


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
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


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)


@dataclass
class ApiResponseFor503(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor503Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_503 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor503,
    response_cls_async=ApiResponseFor503Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '202': _response_for_202,
    '400': _response_for_400,
    '401': _response_for_401,
    '409': _response_for_409,
    '500': _response_for_500,
    '503': _response_for_503,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _perform_refund_operation_mapped_args(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if currency is not None:
            _body["currency"] = currency
        if ref_trans_id is not None:
            _body["refTransId"] = ref_trans_id
        if payer_details is not None:
            _body["payerDetails"] = payer_details
        if card is not None:
            _body["card"] = card
        if amount is not None:
            _body["amount"] = amount
        if my_ref is not None:
            _body["myRef"] = my_ref
        if payment_gateway_account_name is not None:
            _body["paymentGatewayAccountName"] = payment_gateway_account_name
        if certificate_name is not None:
            _body["certificateName"] = certificate_name
        if payment_gateway_account is not None:
            _body["paymentGatewayAccount"] = payment_gateway_account
        if network_token_brand is not None:
            _body["networkTokenBrand"] = network_token_brand
        args.body = _body
        return args

    async def _aperform_refund_operation_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Perform a payment gateway refund operation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/PaymentGateway/refund',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pay_tools_api_models_refund_request_model.serialize(body, content_type)
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


    def _perform_refund_operation_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Perform a payment gateway refund operation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/PaymentGateway/refund',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pay_tools_api_models_refund_request_model.serialize(body, content_type)
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


class PerformRefundOperationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aperform_refund_operation(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._perform_refund_operation_mapped_args(
            currency=currency,
            ref_trans_id=ref_trans_id,
            card=card,
            amount=amount,
            payer_details=payer_details,
            my_ref=my_ref,
            payment_gateway_account_name=payment_gateway_account_name,
            certificate_name=certificate_name,
            payment_gateway_account=payment_gateway_account,
            network_token_brand=network_token_brand,
        )
        return await self._aperform_refund_operation_oapg(
            body=args.body,
            **kwargs,
        )
    
    def perform_refund_operation(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._perform_refund_operation_mapped_args(
            currency=currency,
            ref_trans_id=ref_trans_id,
            card=card,
            amount=amount,
            payer_details=payer_details,
            my_ref=my_ref,
            payment_gateway_account_name=payment_gateway_account_name,
            certificate_name=certificate_name,
            payment_gateway_account=payment_gateway_account,
            network_token_brand=network_token_brand,
        )
        return self._perform_refund_operation_oapg(
            body=args.body,
        )

class PerformRefundOperation(BaseApi):

    async def aperform_refund_operation(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentsOperationResultPydantic:
        raw_response = await self.raw.aperform_refund_operation(
            currency=currency,
            ref_trans_id=ref_trans_id,
            card=card,
            amount=amount,
            payer_details=payer_details,
            my_ref=my_ref,
            payment_gateway_account_name=payment_gateway_account_name,
            certificate_name=certificate_name,
            payment_gateway_account=payment_gateway_account,
            network_token_brand=network_token_brand,
            **kwargs,
        )
        if validate:
            return PaymentsOperationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentsOperationResultPydantic, raw_response.body)
    
    
    def perform_refund_operation(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
        validate: bool = False,
    ) -> PaymentsOperationResultPydantic:
        raw_response = self.raw.perform_refund_operation(
            currency=currency,
            ref_trans_id=ref_trans_id,
            card=card,
            amount=amount,
            payer_details=payer_details,
            my_ref=my_ref,
            payment_gateway_account_name=payment_gateway_account_name,
            certificate_name=certificate_name,
            payment_gateway_account=payment_gateway_account,
            network_token_brand=network_token_brand,
        )
        if validate:
            return PaymentsOperationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentsOperationResultPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._perform_refund_operation_mapped_args(
            currency=currency,
            ref_trans_id=ref_trans_id,
            card=card,
            amount=amount,
            payer_details=payer_details,
            my_ref=my_ref,
            payment_gateway_account_name=payment_gateway_account_name,
            certificate_name=certificate_name,
            payment_gateway_account=payment_gateway_account,
            network_token_brand=network_token_brand,
        )
        return await self._aperform_refund_operation_oapg(
            body=args.body,
            **kwargs,
        )
    
    def put(
        self,
        currency: str,
        ref_trans_id: str,
        card: PayToolsApiModelsCardInputModel,
        amount: typing.Union[int, float],
        payer_details: typing.Optional[PayToolsApiModelsPayerDetails] = None,
        my_ref: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account_name: typing.Optional[typing.Optional[str]] = None,
        certificate_name: typing.Optional[typing.Optional[str]] = None,
        payment_gateway_account: typing.Optional[PayToolsApiModelsPaymentGatewayAccount] = None,
        network_token_brand: typing.Optional[PaymentsNetworkTokenSchemes] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._perform_refund_operation_mapped_args(
            currency=currency,
            ref_trans_id=ref_trans_id,
            card=card,
            amount=amount,
            payer_details=payer_details,
            my_ref=my_ref,
            payment_gateway_account_name=payment_gateway_account_name,
            certificate_name=certificate_name,
            payment_gateway_account=payment_gateway_account,
            network_token_brand=network_token_brand,
        )
        return self._perform_refund_operation_oapg(
            body=args.body,
        )

