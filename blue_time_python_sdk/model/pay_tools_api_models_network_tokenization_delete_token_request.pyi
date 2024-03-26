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


class PayToolsApiModelsNetworkTokenizationDeleteTokenRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Network Tokenization Request
    """


    class MetaOapg:
        required = {
            "tokenId",
            "source",
        }
        
        class properties:
        
            @staticmethod
            def source() -> typing.Type['NetworkTokenRequestSource']:
                return NetworkTokenRequestSource
            
            
            class tokenId(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def brand() -> typing.Type['PaymentsNetworkTokenSchemes']:
                return PaymentsNetworkTokenSchemes
            
            
            class reason(
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
                ) -> 'reason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "source": source,
                "tokenId": tokenId,
                "brand": brand,
                "reason": reason,
            }
    
    tokenId: MetaOapg.properties.tokenId
    source: 'NetworkTokenRequestSource'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'NetworkTokenRequestSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenId"]) -> MetaOapg.properties.tokenId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand"]) -> 'PaymentsNetworkTokenSchemes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["source", "tokenId", "brand", "reason", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> 'NetworkTokenRequestSource': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenId"]) -> MetaOapg.properties.tokenId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand"]) -> typing.Union['PaymentsNetworkTokenSchemes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["source", "tokenId", "brand", "reason", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tokenId: typing.Union[MetaOapg.properties.tokenId, str, ],
        source: 'NetworkTokenRequestSource',
        brand: typing.Union['PaymentsNetworkTokenSchemes', schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsApiModelsNetworkTokenizationDeleteTokenRequest':
        return super().__new__(
            cls,
            *args,
            tokenId=tokenId,
            source=source,
            brand=brand,
            reason=reason,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.network_token_request_source import NetworkTokenRequestSource
from blue_time_python_sdk.model.payments_network_token_schemes import PaymentsNetworkTokenSchemes
