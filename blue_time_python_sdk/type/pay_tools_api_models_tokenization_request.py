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

from blue_time_python_sdk.type.network_token_card_source import NetworkTokenCardSource
from blue_time_python_sdk.type.pay_tools_api_models_network_tokenization_payer import PayToolsApiModelsNetworkTokenizationPayer

class RequiredPayToolsApiModelsTokenizationRequest(TypedDict):
    pass

class OptionalPayToolsApiModelsTokenizationRequest(TypedDict, total=False):
    # Iso-369-1 2-letter language code
    consumerLanguage: typing.Optional[str]

    cardHolder: PayToolsApiModelsNetworkTokenizationPayer

    # Device score
    deviceScore: int

    # Account score
    accountScore: int

    # Device latitude -90 to 90
    deviceLocationLat: typing.Optional[typing.Union[int, float]]

    # Device longitude -90 to 90
    deviceLocationLon: typing.Optional[typing.Union[int, float]]

    # Ip address of device
    deviceIpAddress: typing.Optional[str]

    cardSource: NetworkTokenCardSource

class PayToolsApiModelsTokenizationRequest(RequiredPayToolsApiModelsTokenizationRequest, OptionalPayToolsApiModelsTokenizationRequest):
    pass
