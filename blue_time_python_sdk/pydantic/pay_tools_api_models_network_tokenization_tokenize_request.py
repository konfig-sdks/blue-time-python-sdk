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

from blue_time_python_sdk.pydantic.pay_tools_api_models_card_base_with_security_code import PayToolsApiModelsCardBaseWithSecurityCode
from blue_time_python_sdk.pydantic.pay_tools_api_models_tokenization_request import PayToolsApiModelsTokenizationRequest

class PayToolsApiModelsNetworkTokenizationTokenizeRequest(BaseModel):
    tokenization_request: typing.Optional[PayToolsApiModelsTokenizationRequest] = Field(None, alias='tokenizationRequest')

    card: typing.Optional[PayToolsApiModelsCardBaseWithSecurityCode] = Field(None, alias='card')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
