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


class PayToolsApiModelsTokenizationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for sending Network Tokenization Request
    """


    class MetaOapg:
        
        class properties:
            
            
            class consumerLanguage(
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
                ) -> 'consumerLanguage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def cardHolder() -> typing.Type['PayToolsApiModelsNetworkTokenizationPayer']:
                return PayToolsApiModelsNetworkTokenizationPayer
            
            
            class deviceScore(
                schemas.Int32Schema
            ):
                pass
            
            
            class accountScore(
                schemas.Int32Schema
            ):
                pass
            
            
            class deviceLocationLat(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deviceLocationLat':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class deviceLocationLon(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deviceLocationLon':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class deviceIpAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deviceIpAddress':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def cardSource() -> typing.Type['NetworkTokenCardSource']:
                return NetworkTokenCardSource
            __annotations__ = {
                "consumerLanguage": consumerLanguage,
                "cardHolder": cardHolder,
                "deviceScore": deviceScore,
                "accountScore": accountScore,
                "deviceLocationLat": deviceLocationLat,
                "deviceLocationLon": deviceLocationLon,
                "deviceIpAddress": deviceIpAddress,
                "cardSource": cardSource,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consumerLanguage"]) -> MetaOapg.properties.consumerLanguage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardHolder"]) -> 'PayToolsApiModelsNetworkTokenizationPayer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceScore"]) -> MetaOapg.properties.deviceScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountScore"]) -> MetaOapg.properties.accountScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceLocationLat"]) -> MetaOapg.properties.deviceLocationLat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceLocationLon"]) -> MetaOapg.properties.deviceLocationLon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceIpAddress"]) -> MetaOapg.properties.deviceIpAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardSource"]) -> 'NetworkTokenCardSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["consumerLanguage", "cardHolder", "deviceScore", "accountScore", "deviceLocationLat", "deviceLocationLon", "deviceIpAddress", "cardSource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consumerLanguage"]) -> typing.Union[MetaOapg.properties.consumerLanguage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardHolder"]) -> typing.Union['PayToolsApiModelsNetworkTokenizationPayer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceScore"]) -> typing.Union[MetaOapg.properties.deviceScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountScore"]) -> typing.Union[MetaOapg.properties.accountScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceLocationLat"]) -> typing.Union[MetaOapg.properties.deviceLocationLat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceLocationLon"]) -> typing.Union[MetaOapg.properties.deviceLocationLon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceIpAddress"]) -> typing.Union[MetaOapg.properties.deviceIpAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardSource"]) -> typing.Union['NetworkTokenCardSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["consumerLanguage", "cardHolder", "deviceScore", "accountScore", "deviceLocationLat", "deviceLocationLon", "deviceIpAddress", "cardSource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        consumerLanguage: typing.Union[MetaOapg.properties.consumerLanguage, None, str, schemas.Unset] = schemas.unset,
        cardHolder: typing.Union['PayToolsApiModelsNetworkTokenizationPayer', schemas.Unset] = schemas.unset,
        deviceScore: typing.Union[MetaOapg.properties.deviceScore, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        accountScore: typing.Union[MetaOapg.properties.accountScore, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deviceLocationLat: typing.Union[MetaOapg.properties.deviceLocationLat, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        deviceLocationLon: typing.Union[MetaOapg.properties.deviceLocationLon, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        deviceIpAddress: typing.Union[MetaOapg.properties.deviceIpAddress, None, str, schemas.Unset] = schemas.unset,
        cardSource: typing.Union['NetworkTokenCardSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsApiModelsTokenizationRequest':
        return super().__new__(
            cls,
            *args,
            consumerLanguage=consumerLanguage,
            cardHolder=cardHolder,
            deviceScore=deviceScore,
            accountScore=accountScore,
            deviceLocationLat=deviceLocationLat,
            deviceLocationLon=deviceLocationLon,
            deviceIpAddress=deviceIpAddress,
            cardSource=cardSource,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.network_token_card_source import NetworkTokenCardSource
from blue_time_python_sdk.model.pay_tools_api_models_network_tokenization_payer import PayToolsApiModelsNetworkTokenizationPayer
