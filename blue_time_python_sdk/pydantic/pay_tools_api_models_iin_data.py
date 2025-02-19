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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class PayToolsApiModelsIinData(BaseModel):
    # The longest match of the first 6 to 11 digits of the card number that we were able to match
    bin: typing.Optional[typing.Optional[str]] = Field(None, alias='bin')

    # The card brand (AMERICAN EXPRESS, VISA, MASTERCARD, JCB etc)
    card_brand: typing.Optional[typing.Optional[str]] = Field(None, alias='cardBrand')

    # The type of card (DEBIT, CREDIT, 'DEBIT OR CREDIT', CHARGE CARD)
    card_type: typing.Optional[typing.Optional[str]] = Field(None, alias='cardType')

    # The category of the card (CLASSIC, BUSINESS, STANDARD, PERSONAL, etc)
    category: typing.Optional[typing.Optional[str]] = Field(None, alias='category')

    # The name of the entity (usually bank) that issued the card
    issuing_organization: typing.Optional[typing.Optional[str]] = Field(None, alias='issuingOrganization')

    # The 2 letter country code (<a href=\"https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes\" target=\"_blank\">ISO 3166-2 <img src=\"https://files.readme.io/b676144-openNewWindow.png\" width=\"10\" /></a>) where the card was issued
    country_code: typing.Optional[typing.Optional[str]] = Field(None, alias='countryCode')

    # The url to the brand logo
    brand_logo_url: typing.Optional[typing.Optional[str]] = Field(None, alias='brandLogoUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
