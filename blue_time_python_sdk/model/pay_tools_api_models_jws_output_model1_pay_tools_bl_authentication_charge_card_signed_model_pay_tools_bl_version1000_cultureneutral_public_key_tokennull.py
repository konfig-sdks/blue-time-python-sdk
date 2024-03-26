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


class PayToolsApiModelsJwsOutputModel1PayToolsBlAuthenticationChargeCardSignedModelPayToolsBlVersion1000CultureneutralPublicKeyTokennull(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The model used to return a valid Jws with payload
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def payload() -> typing.Type['PayToolsBlAuthenticationChargeCardSignedModel']:
                return PayToolsBlAuthenticationChargeCardSignedModel
            
            
            class authToken(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'authToken':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "payload": payload,
                "authToken": authToken,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> 'PayToolsBlAuthenticationChargeCardSignedModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authToken"]) -> MetaOapg.properties.authToken: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payload", "authToken", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> typing.Union['PayToolsBlAuthenticationChargeCardSignedModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authToken"]) -> typing.Union[MetaOapg.properties.authToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payload", "authToken", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payload: typing.Union['PayToolsBlAuthenticationChargeCardSignedModel', schemas.Unset] = schemas.unset,
        authToken: typing.Union[MetaOapg.properties.authToken, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsApiModelsJwsOutputModel1PayToolsBlAuthenticationChargeCardSignedModelPayToolsBlVersion1000CultureneutralPublicKeyTokennull':
        return super().__new__(
            cls,
            *args,
            payload=payload,
            authToken=authToken,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.pay_tools_bl_authentication_charge_card_signed_model import PayToolsBlAuthenticationChargeCardSignedModel
