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

from blue_time_python_sdk.type.payments_card_types import PaymentsCardTypes

class RequiredPaymentsBankCard(TypedDict):
    pass

class OptionalPaymentsBankCard(TypedDict, total=False):
    type: PaymentsCardTypes

    nameOnCard: typing.Optional[str]

    issueNumber: typing.Optional[str]

    ownerId: typing.Optional[str]

    securityCode: typing.Optional[str]

    number: typing.Optional[str]

    expirationMonth: int

    expirationYear: int

class PaymentsBankCard(RequiredPaymentsBankCard, OptionalPaymentsBankCard):
    pass
