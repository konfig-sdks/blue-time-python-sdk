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

from blue_time_python_sdk.pydantic.pay_tools_bl_authentication_charge_card_signed_model import PayToolsBlAuthenticationChargeCardSignedModel

class PayToolsApiModelsJwsOutputModel1PayToolsBlAuthenticationChargeCardSignedModelPayToolsBlVersion1000CultureneutralPublicKeyTokennull(BaseModel):
    payload: typing.Optional[PayToolsBlAuthenticationChargeCardSignedModel] = Field(None, alias='payload')

    # The jws (token) value to be used in subsequent card operation methods
    auth_token: typing.Optional[typing.Optional[str]] = Field(None, alias='authToken')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
