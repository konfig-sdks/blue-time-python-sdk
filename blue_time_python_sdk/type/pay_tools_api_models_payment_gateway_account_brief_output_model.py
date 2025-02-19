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


class RequiredPayToolsApiModelsPaymentGatewayAccountBriefOutputModel(TypedDict):
    pass

class OptionalPayToolsApiModelsPaymentGatewayAccountBriefOutputModel(TypedDict, total=False):
    # Name of account
    name: typing.Optional[str]

    # Unique name of the Payment Gateway the account information relates to.
    paymentGatewayName: typing.Optional[str]

    # Date and time the credentials were stored
    creationTime: datetime

class PayToolsApiModelsPaymentGatewayAccountBriefOutputModel(RequiredPayToolsApiModelsPaymentGatewayAccountBriefOutputModel, OptionalPayToolsApiModelsPaymentGatewayAccountBriefOutputModel):
    pass
