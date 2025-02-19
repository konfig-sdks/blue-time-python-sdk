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


class PayToolsApiModelsPayerDetails(BaseModel):
    # Client IP address
    client_i_p_address: str = Field(alias='clientIPAddress')

    # 2 letter country code (<a href=\"https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes\" target=\"_blank\">ISO 3166-2 <img src=\"https://files.readme.io/b676144-openNewWindow.png\" width=\"10\" /></a>)
    country_code: str = Field(alias='countryCode')

    # 1st address line
    address1: typing.Optional[typing.Optional[str]] = Field(None, alias='address1')

    # 2nd address line
    address2: typing.Optional[typing.Optional[str]] = Field(None, alias='address2')

    # 3rd address line
    address3: typing.Optional[typing.Optional[str]] = Field(None, alias='address3')

    # Postal code or Zip code
    post_code: typing.Optional[typing.Optional[str]] = Field(None, alias='postCode')

    # City
    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    # State or Province
    state_province: typing.Optional[typing.Optional[str]] = Field(None, alias='stateProvince')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
