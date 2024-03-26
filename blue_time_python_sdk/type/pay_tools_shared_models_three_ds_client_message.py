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

from blue_time_python_sdk.type.pay_tools_shared_models_message_type import PayToolsSharedModelsMessageType

class RequiredPayToolsSharedModelsThreeDsClientMessage(TypedDict):
    pass

class OptionalPayToolsSharedModelsThreeDsClientMessage(TypedDict, total=False):
    messageType: PayToolsSharedModelsMessageType

class PayToolsSharedModelsThreeDsClientMessage(RequiredPayToolsSharedModelsThreeDsClientMessage, OptionalPayToolsSharedModelsThreeDsClientMessage):
    pass
