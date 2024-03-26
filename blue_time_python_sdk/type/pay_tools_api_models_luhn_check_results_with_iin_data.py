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

from blue_time_python_sdk.type.pay_tools_api_models_iin_data import PayToolsApiModelsIinData

class RequiredPayToolsApiModelsLuhnCheckResultsWithIinData(TypedDict):
    pass

class OptionalPayToolsApiModelsLuhnCheckResultsWithIinData(TypedDict, total=False):
    iinData: PayToolsApiModelsIinData

    # Indicates a successful luhn check
    luhnValid: bool

    # Error description
    error: typing.Optional[str]

class PayToolsApiModelsLuhnCheckResultsWithIinData(RequiredPayToolsApiModelsLuhnCheckResultsWithIinData, OptionalPayToolsApiModelsLuhnCheckResultsWithIinData):
    pass
