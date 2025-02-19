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


class PayToolsBlAuthenticationChargePresetData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Data to be used in Charge request
    """


    class MetaOapg:
        
        class properties:
            
            
            class dsc(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dsc':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ref(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ref':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            dig = schemas.BoolSchema
        
            @staticmethod
            def amt() -> typing.Type['PayToolsSharedModelsMoneyModel']:
                return PayToolsSharedModelsMoneyModel
            
            
            class uan(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'uan':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ucc(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ucc':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "dsc": dsc,
                "ref": ref,
                "dig": dig,
                "amt": amt,
                "uan": uan,
                "ucc": ucc,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dsc"]) -> MetaOapg.properties.dsc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dig"]) -> MetaOapg.properties.dig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amt"]) -> 'PayToolsSharedModelsMoneyModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uan"]) -> MetaOapg.properties.uan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ucc"]) -> MetaOapg.properties.ucc: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dsc", "ref", "dig", "amt", "uan", "ucc", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dsc"]) -> typing.Union[MetaOapg.properties.dsc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dig"]) -> typing.Union[MetaOapg.properties.dig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amt"]) -> typing.Union['PayToolsSharedModelsMoneyModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uan"]) -> typing.Union[MetaOapg.properties.uan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ucc"]) -> typing.Union[MetaOapg.properties.ucc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dsc", "ref", "dig", "amt", "uan", "ucc", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dsc: typing.Union[MetaOapg.properties.dsc, None, str, schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, None, str, schemas.Unset] = schemas.unset,
        dig: typing.Union[MetaOapg.properties.dig, bool, schemas.Unset] = schemas.unset,
        amt: typing.Union['PayToolsSharedModelsMoneyModel', schemas.Unset] = schemas.unset,
        uan: typing.Union[MetaOapg.properties.uan, None, str, schemas.Unset] = schemas.unset,
        ucc: typing.Union[MetaOapg.properties.ucc, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsBlAuthenticationChargePresetData':
        return super().__new__(
            cls,
            *args,
            dsc=dsc,
            ref=ref,
            dig=dig,
            amt=amt,
            uan=uan,
            ucc=ucc,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.pay_tools_shared_models_money_model import PayToolsSharedModelsMoneyModel
