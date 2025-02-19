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


class PayToolsApiModelsNetworkTokenizationTokenizeRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Network Tokenization Request
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def tokenizationRequest() -> typing.Type['PayToolsApiModelsTokenizationRequest']:
                return PayToolsApiModelsTokenizationRequest
        
            @staticmethod
            def card() -> typing.Type['PayToolsApiModelsCardBaseWithSecurityCode']:
                return PayToolsApiModelsCardBaseWithSecurityCode
            __annotations__ = {
                "tokenizationRequest": tokenizationRequest,
                "card": card,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenizationRequest"]) -> 'PayToolsApiModelsTokenizationRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card"]) -> 'PayToolsApiModelsCardBaseWithSecurityCode': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tokenizationRequest", "card", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenizationRequest"]) -> typing.Union['PayToolsApiModelsTokenizationRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card"]) -> typing.Union['PayToolsApiModelsCardBaseWithSecurityCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tokenizationRequest", "card", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tokenizationRequest: typing.Union['PayToolsApiModelsTokenizationRequest', schemas.Unset] = schemas.unset,
        card: typing.Union['PayToolsApiModelsCardBaseWithSecurityCode', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsApiModelsNetworkTokenizationTokenizeRequest':
        return super().__new__(
            cls,
            *args,
            tokenizationRequest=tokenizationRequest,
            card=card,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.pay_tools_api_models_card_base_with_security_code import PayToolsApiModelsCardBaseWithSecurityCode
from blue_time_python_sdk.model.pay_tools_api_models_tokenization_request import PayToolsApiModelsTokenizationRequest
