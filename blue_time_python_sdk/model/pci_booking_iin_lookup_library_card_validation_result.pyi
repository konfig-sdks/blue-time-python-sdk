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


class PciBookingIINLookupLibraryCardValidationResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def riskLevel() -> typing.Type['PciBookingIINLookupLibraryRiskLevel']:
                return PciBookingIINLookupLibraryRiskLevel
            
            
            class cardBrand(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardBrand':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cardType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cardCategory(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardCategory':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class issuerName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'issuerName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class issuerCountry(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'issuerCountry':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class countryByIP(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'countryByIP':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class countryFromBillingAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'countryFromBillingAddress':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            anonymousProxyUsed = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "riskLevel": riskLevel,
                "cardBrand": cardBrand,
                "cardType": cardType,
                "cardCategory": cardCategory,
                "issuerName": issuerName,
                "issuerCountry": issuerCountry,
                "countryByIP": countryByIP,
                "countryFromBillingAddress": countryFromBillingAddress,
                "anonymousProxyUsed": anonymousProxyUsed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["riskLevel"]) -> 'PciBookingIINLookupLibraryRiskLevel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardBrand"]) -> MetaOapg.properties.cardBrand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardType"]) -> MetaOapg.properties.cardType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardCategory"]) -> MetaOapg.properties.cardCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuerName"]) -> MetaOapg.properties.issuerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuerCountry"]) -> MetaOapg.properties.issuerCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryByIP"]) -> MetaOapg.properties.countryByIP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryFromBillingAddress"]) -> MetaOapg.properties.countryFromBillingAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anonymousProxyUsed"]) -> MetaOapg.properties.anonymousProxyUsed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "riskLevel", "cardBrand", "cardType", "cardCategory", "issuerName", "issuerCountry", "countryByIP", "countryFromBillingAddress", "anonymousProxyUsed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["riskLevel"]) -> typing.Union['PciBookingIINLookupLibraryRiskLevel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardBrand"]) -> typing.Union[MetaOapg.properties.cardBrand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardType"]) -> typing.Union[MetaOapg.properties.cardType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardCategory"]) -> typing.Union[MetaOapg.properties.cardCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuerName"]) -> typing.Union[MetaOapg.properties.issuerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuerCountry"]) -> typing.Union[MetaOapg.properties.issuerCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryByIP"]) -> typing.Union[MetaOapg.properties.countryByIP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryFromBillingAddress"]) -> typing.Union[MetaOapg.properties.countryFromBillingAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anonymousProxyUsed"]) -> typing.Union[MetaOapg.properties.anonymousProxyUsed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "riskLevel", "cardBrand", "cardType", "cardCategory", "issuerName", "issuerCountry", "countryByIP", "countryFromBillingAddress", "anonymousProxyUsed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        riskLevel: typing.Union['PciBookingIINLookupLibraryRiskLevel', schemas.Unset] = schemas.unset,
        cardBrand: typing.Union[MetaOapg.properties.cardBrand, None, str, schemas.Unset] = schemas.unset,
        cardType: typing.Union[MetaOapg.properties.cardType, None, str, schemas.Unset] = schemas.unset,
        cardCategory: typing.Union[MetaOapg.properties.cardCategory, None, str, schemas.Unset] = schemas.unset,
        issuerName: typing.Union[MetaOapg.properties.issuerName, None, str, schemas.Unset] = schemas.unset,
        issuerCountry: typing.Union[MetaOapg.properties.issuerCountry, None, str, schemas.Unset] = schemas.unset,
        countryByIP: typing.Union[MetaOapg.properties.countryByIP, None, str, schemas.Unset] = schemas.unset,
        countryFromBillingAddress: typing.Union[MetaOapg.properties.countryFromBillingAddress, None, str, schemas.Unset] = schemas.unset,
        anonymousProxyUsed: typing.Union[MetaOapg.properties.anonymousProxyUsed, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PciBookingIINLookupLibraryCardValidationResult':
        return super().__new__(
            cls,
            *args,
            description=description,
            riskLevel=riskLevel,
            cardBrand=cardBrand,
            cardType=cardType,
            cardCategory=cardCategory,
            issuerName=issuerName,
            issuerCountry=issuerCountry,
            countryByIP=countryByIP,
            countryFromBillingAddress=countryFromBillingAddress,
            anonymousProxyUsed=anonymousProxyUsed,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.pci_booking_iin_lookup_library_risk_level import PciBookingIINLookupLibraryRiskLevel
