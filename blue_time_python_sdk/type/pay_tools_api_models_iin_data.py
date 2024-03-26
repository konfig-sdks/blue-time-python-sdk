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


class RequiredPayToolsApiModelsIinData(TypedDict):
    pass

class OptionalPayToolsApiModelsIinData(TypedDict, total=False):
    # The longest match of the first 6 to 11 digits of the card number that we were able to match
    bin: typing.Optional[str]

    # The card brand (AMERICAN EXPRESS, VISA, MASTERCARD, JCB etc)
    cardBrand: typing.Optional[str]

    # The type of card (DEBIT, CREDIT, 'DEBIT OR CREDIT', CHARGE CARD)
    cardType: typing.Optional[str]

    # The category of the card (CLASSIC, BUSINESS, STANDARD, PERSONAL, etc)
    category: typing.Optional[str]

    # The name of the entity (usually bank) that issued the card
    issuingOrganization: typing.Optional[str]

    # The 2 letter country code (<a href=\"https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes\" target=\"_blank\">ISO 3166-2 <img src=\"https://files.readme.io/b676144-openNewWindow.png\" width=\"10\" /></a>) where the card was issued
    countryCode: typing.Optional[str]

    # The url to the brand logo
    brandLogoUrl: typing.Optional[str]

class PayToolsApiModelsIinData(RequiredPayToolsApiModelsIinData, OptionalPayToolsApiModelsIinData):
    pass
