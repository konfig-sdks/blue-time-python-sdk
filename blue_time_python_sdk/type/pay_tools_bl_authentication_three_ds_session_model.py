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

from blue_time_python_sdk.type.pay_tools_shared_models_money_model import PayToolsSharedModelsMoneyModel

class RequiredPayToolsBlAuthenticationThreeDsSessionModel(TypedDict):
    # The name of the stored merchant account
    merchantAccountName: str

    amt: PayToolsSharedModelsMoneyModel

class OptionalPayToolsBlAuthenticationThreeDsSessionModel(TypedDict, total=False):
    pass

class PayToolsBlAuthenticationThreeDsSessionModel(RequiredPayToolsBlAuthenticationThreeDsSessionModel, OptionalPayToolsBlAuthenticationThreeDsSessionModel):
    pass
