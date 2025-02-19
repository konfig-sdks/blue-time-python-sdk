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


class RequiredPciBookingIINLookupLibraryCardValidationRequest(TypedDict):
    pass

class OptionalPciBookingIINLookupLibraryCardValidationRequest(TypedDict, total=False):
    iin: typing.Optional[str]

    city: typing.Optional[str]

    stateProvince: typing.Optional[str]

    countryCode: typing.Optional[str]

    clientIPAddress: typing.Optional[str]

class PciBookingIINLookupLibraryCardValidationRequest(RequiredPciBookingIINLookupLibraryCardValidationRequest, OptionalPciBookingIINLookupLibraryCardValidationRequest):
    pass
