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


class PayToolsApiModelsStringTokenOutputModel(BaseModel):
    # The content of the StringToken that was stored in our system
    clear_payload: typing.Optional[typing.Optional[str]] = Field(None, alias='clearPayload')

    # Token ID representing the stringToken
    token: typing.Optional[typing.Optional[str]] = Field(None, alias='token')

    # Date and time the string was stored
    create_time: typing.Optional[datetime] = Field(None, alias='createTime')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
