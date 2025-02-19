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


class PayToolsBlAuthenticationSignedData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Class to represent signed data
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def vld_rq() -> typing.Type['PciBookingIINLookupLibraryCardValidationRequest']:
                return PciBookingIINLookupLibraryCardValidationRequest
        
            @staticmethod
            def vld_rs() -> typing.Type['PciBookingIINLookupLibraryCardValidationResult']:
                return PciBookingIINLookupLibraryCardValidationResult
        
            @staticmethod
            def crg_rq() -> typing.Type['PaymentsChargeRequest']:
                return PaymentsChargeRequest
        
            @staticmethod
            def crg_rs() -> typing.Type['PaymentsOperationResult']:
                return PaymentsOperationResult
            
            
            class tkn_rs(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tkn_rs':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def _3ds_d() -> typing.Type['PayToolsBlAuthenticationThreeDsPresetData']:
                return PayToolsBlAuthenticationThreeDsPresetData
        
            @staticmethod
            def vld() -> typing.Type['PciBookingIINLookupLibraryRiskLevel']:
                return PciBookingIINLookupLibraryRiskLevel
        
            @staticmethod
            def _3ds() -> typing.Type['PayToolsSharedEnumsPerform3ds']:
                return PayToolsSharedEnumsPerform3ds
            crg = schemas.BoolSchema
        
            @staticmethod
            def tkn() -> typing.Type['PayToolsBlAuthenticationTokenizationAction']:
                return PayToolsBlAuthenticationTokenizationAction
        
            @staticmethod
            def crg_d() -> typing.Type['PayToolsBlAuthenticationChargePresetData']:
                return PayToolsBlAuthenticationChargePresetData
            __annotations__ = {
                "vld_rq": vld_rq,
                "vld_rs": vld_rs,
                "crg_rq": crg_rq,
                "crg_rs": crg_rs,
                "tkn_rs": tkn_rs,
                "3ds_d": _3ds_d,
                "vld": vld,
                "3ds": _3ds,
                "crg": crg,
                "tkn": tkn,
                "crg_d": crg_d,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vld_rq"]) -> 'PciBookingIINLookupLibraryCardValidationRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vld_rs"]) -> 'PciBookingIINLookupLibraryCardValidationResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crg_rq"]) -> 'PaymentsChargeRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crg_rs"]) -> 'PaymentsOperationResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tkn_rs"]) -> MetaOapg.properties.tkn_rs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["3ds_d"]) -> 'PayToolsBlAuthenticationThreeDsPresetData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vld"]) -> 'PciBookingIINLookupLibraryRiskLevel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["3ds"]) -> 'PayToolsSharedEnumsPerform3ds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crg"]) -> MetaOapg.properties.crg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tkn"]) -> 'PayToolsBlAuthenticationTokenizationAction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crg_d"]) -> 'PayToolsBlAuthenticationChargePresetData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["vld_rq", "vld_rs", "crg_rq", "crg_rs", "tkn_rs", "3ds_d", "vld", "3ds", "crg", "tkn", "crg_d", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vld_rq"]) -> typing.Union['PciBookingIINLookupLibraryCardValidationRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vld_rs"]) -> typing.Union['PciBookingIINLookupLibraryCardValidationResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crg_rq"]) -> typing.Union['PaymentsChargeRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crg_rs"]) -> typing.Union['PaymentsOperationResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tkn_rs"]) -> typing.Union[MetaOapg.properties.tkn_rs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["3ds_d"]) -> typing.Union['PayToolsBlAuthenticationThreeDsPresetData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vld"]) -> typing.Union['PciBookingIINLookupLibraryRiskLevel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["3ds"]) -> typing.Union['PayToolsSharedEnumsPerform3ds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crg"]) -> typing.Union[MetaOapg.properties.crg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tkn"]) -> typing.Union['PayToolsBlAuthenticationTokenizationAction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crg_d"]) -> typing.Union['PayToolsBlAuthenticationChargePresetData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vld_rq", "vld_rs", "crg_rq", "crg_rs", "tkn_rs", "3ds_d", "vld", "3ds", "crg", "tkn", "crg_d", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vld_rq: typing.Union['PciBookingIINLookupLibraryCardValidationRequest', schemas.Unset] = schemas.unset,
        vld_rs: typing.Union['PciBookingIINLookupLibraryCardValidationResult', schemas.Unset] = schemas.unset,
        crg_rq: typing.Union['PaymentsChargeRequest', schemas.Unset] = schemas.unset,
        crg_rs: typing.Union['PaymentsOperationResult', schemas.Unset] = schemas.unset,
        tkn_rs: typing.Union[MetaOapg.properties.tkn_rs, None, str, schemas.Unset] = schemas.unset,
        vld: typing.Union['PciBookingIINLookupLibraryRiskLevel', schemas.Unset] = schemas.unset,
        crg: typing.Union[MetaOapg.properties.crg, bool, schemas.Unset] = schemas.unset,
        tkn: typing.Union['PayToolsBlAuthenticationTokenizationAction', schemas.Unset] = schemas.unset,
        crg_d: typing.Union['PayToolsBlAuthenticationChargePresetData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayToolsBlAuthenticationSignedData':
        return super().__new__(
            cls,
            *args,
            vld_rq=vld_rq,
            vld_rs=vld_rs,
            crg_rq=crg_rq,
            crg_rs=crg_rs,
            tkn_rs=tkn_rs,
            vld=vld,
            crg=crg,
            tkn=tkn,
            crg_d=crg_d,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.pay_tools_bl_authentication_charge_preset_data import PayToolsBlAuthenticationChargePresetData
from blue_time_python_sdk.model.pay_tools_bl_authentication_three_ds_preset_data import PayToolsBlAuthenticationThreeDsPresetData
from blue_time_python_sdk.model.pay_tools_bl_authentication_tokenization_action import PayToolsBlAuthenticationTokenizationAction
from blue_time_python_sdk.model.pay_tools_shared_enums_perform3ds import PayToolsSharedEnumsPerform3ds
from blue_time_python_sdk.model.payments_charge_request import PaymentsChargeRequest
from blue_time_python_sdk.model.payments_operation_result import PaymentsOperationResult
from blue_time_python_sdk.model.pci_booking_iin_lookup_library_card_validation_request import PciBookingIINLookupLibraryCardValidationRequest
from blue_time_python_sdk.model.pci_booking_iin_lookup_library_card_validation_result import PciBookingIINLookupLibraryCardValidationResult
from blue_time_python_sdk.model.pci_booking_iin_lookup_library_risk_level import PciBookingIINLookupLibraryRiskLevel
