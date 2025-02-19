# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from blue_time_python_sdk.type.pci_booking_iin_lookup_library_risk_level import PciBookingIINLookupLibraryRiskLevel

class RequiredPciBookingIINLookupLibraryCardValidationResult(TypedDict):
    pass

class OptionalPciBookingIINLookupLibraryCardValidationResult(TypedDict, total=False):
    description: typing.Optional[str]

    riskLevel: PciBookingIINLookupLibraryRiskLevel

    cardBrand: typing.Optional[str]

    cardType: typing.Optional[str]

    cardCategory: typing.Optional[str]

    issuerName: typing.Optional[str]

    issuerCountry: typing.Optional[str]

    countryByIP: typing.Optional[str]

    countryFromBillingAddress: typing.Optional[str]

    anonymousProxyUsed: bool

class PciBookingIINLookupLibraryCardValidationResult(RequiredPciBookingIINLookupLibraryCardValidationResult, OptionalPciBookingIINLookupLibraryCardValidationResult):
    pass
