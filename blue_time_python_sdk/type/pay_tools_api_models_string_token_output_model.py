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


class RequiredPayToolsApiModelsStringTokenOutputModel(TypedDict):
    pass

class OptionalPayToolsApiModelsStringTokenOutputModel(TypedDict, total=False):
    # The content of the StringToken that was stored in our system
    clearPayload: typing.Optional[str]

    # Token ID representing the stringToken
    token: typing.Optional[str]

    # Date and time the string was stored
    createTime: datetime

class PayToolsApiModelsStringTokenOutputModel(RequiredPayToolsApiModelsStringTokenOutputModel, OptionalPayToolsApiModelsStringTokenOutputModel):
    pass
