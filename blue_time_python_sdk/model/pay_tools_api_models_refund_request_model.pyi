# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

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


class PayToolsApiModelsRefundRequestModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for UPG refund operation
    """


    class MetaOapg:
        required = {
            "amount",
            "currency",
            "refTransId",
            "card",
        }
        
        class properties:
            
            
            class currency(
                schemas.StrSchema
            ):
                pass
            
            
            class refTransId(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def card() -> typing.Type['PayToolsApiModelsCardInputModel']:
                return PayToolsApiModelsCardInputModel
            amount = schemas.Float64Schema
        
            @staticmethod
            def payerDetails() -> typing.Type['PayToolsApiModelsPayerDetails']:
                return PayToolsApiModelsPayerDetails
            
            
            class myRef(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'myRef':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class paymentGatewayAccountName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paymentGatewayAccountName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class certificateName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'certificateName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def paymentGatewayAccount() -> typing.Type['PayToolsApiModelsPaymentGatewayAccount']:
                return PayToolsApiModelsPaymentGatewayAccount
        
            @staticmethod
            def networkTokenBrand() -> typing.Type['PaymentsNetworkTokenSchemes']:
                return PaymentsNetworkTokenSchemes
            __annotations__ = {
                "currency": currency,
                "refTransId": refTransId,
                "card": card,
                "amount": amount,
                "payerDetails": payerDetails,
                "myRef": myRef,
                "paymentGatewayAccountName": paymentGatewayAccountName,
                "certificateName": certificateName,
                "paymentGatewayAccount": paymentGatewayAccount,
                "networkTokenBrand": networkTokenBrand,
            }
    
    amount: MetaOapg.properties.amount
    currency: MetaOapg.properties.currency
    refTransId: MetaOapg.properties.refTransId
    card: 'PayToolsApiModelsCardInputModel'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refTransId"]) -> MetaOapg.properties.refTransId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card"]) -> 'PayToolsApiModelsCardInputModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payerDetails"]) -> 'PayToolsApiModelsPayerDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myRef"]) -> MetaOapg.properties.myRef: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentGatewayAccountName"]) -> MetaOapg.properties.paymentGatewayAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certificateName"]) -> MetaOapg.properties.certificateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentGatewayAccount"]) -> 'PayToolsApiModelsPaymentGatewayAccount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkTokenBrand"]) -> 'PaymentsNetworkTokenSchemes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "refTransId", "card", "amount", "payerDetails", "myRef", "paymentGatewayAccountName", "certificateName", "paymentGatewayAccount", "networkTokenBrand", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refTransId"]) -> MetaOapg.properties.refTransId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card"]) -> 'PayToolsApiModelsCardInputModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payerDetails"]) -> typing.Union['PayToolsApiModelsPayerDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["myRef"]) -> typing.Union[MetaOapg.properties.myRef, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentGatewayAccountName"]) -> typing.Union[MetaOapg.properties.paymentGatewayAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certificateName"]) -> typing.Union[MetaOapg.properties.certificateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentGatewayAccount"]) -> typing.Union['PayToolsApiModelsPaymentGatewayAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkTokenBrand"]) -> typing.Union['PaymentsNetworkTokenSchemes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "refTransId", "card", "amount", "payerDetails", "myRef", "paymentGatewayAccountName", "certificateName", "paymentGatewayAccount", "networkTokenBrand", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        refTransId: typing.Union[MetaOapg.properties.refTransId, str, ],
        card: 'PayToolsApiModelsCardInputModel',
        payerDetails: typing.Union['PayToolsApiModelsPayerDetails', schemas.Unset] = schemas.unset,
        myRef: typing.Union[MetaOapg.properties.myRef, None, str, schemas.Unset] = schemas.unset,
        paymentGatewayAccountName: typing.Union[MetaOapg.properties.paymentGatewayAccountName, None, str, schemas.Unset] = schemas.unset,
        certificateName: typing.Union[MetaOapg.properties.certificateName, None, str, schemas.Unset] = schemas.unset,
        paymentGatewayAccount: typing.Union['PayToolsApiModelsPaymentGatewayAccount', schemas.Unset] = schemas.unset,
        networkTokenBrand: typing.Union['PaymentsNetworkTokenSchemes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsApiModelsRefundRequestModel':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            currency=currency,
            refTransId=refTransId,
            card=card,
            payerDetails=payerDetails,
            myRef=myRef,
            paymentGatewayAccountName=paymentGatewayAccountName,
            certificateName=certificateName,
            paymentGatewayAccount=paymentGatewayAccount,
            networkTokenBrand=networkTokenBrand,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.pay_tools_api_models_card_input_model import PayToolsApiModelsCardInputModel
from blue_time_python_sdk.model.pay_tools_api_models_payer_details import PayToolsApiModelsPayerDetails
from blue_time_python_sdk.model.pay_tools_api_models_payment_gateway_account import PayToolsApiModelsPaymentGatewayAccount
from blue_time_python_sdk.model.payments_network_token_schemes import PaymentsNetworkTokenSchemes
