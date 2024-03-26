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

from blue_time_python_sdk.type.pay_tools_bl_authentication_charge_preset_data import PayToolsBlAuthenticationChargePresetData
from blue_time_python_sdk.type.pay_tools_shared_models_card_stored_card import PayToolsSharedModelsCardStoredCard

class RequiredPayToolsBlAuthenticationCvvSignedDataModel(TypedDict):
    pass

class OptionalPayToolsBlAuthenticationCvvSignedDataModel(TypedDict, total=False):
    card: PayToolsSharedModelsCardStoredCard

    crg_d: PayToolsBlAuthenticationChargePresetData

class PayToolsBlAuthenticationCvvSignedDataModel(RequiredPayToolsBlAuthenticationCvvSignedDataModel, OptionalPayToolsBlAuthenticationCvvSignedDataModel):
    pass
