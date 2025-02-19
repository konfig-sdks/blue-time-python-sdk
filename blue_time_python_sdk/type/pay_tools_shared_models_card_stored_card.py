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

class RequiredPayToolsSharedModelsCardStoredCard(TypedDict):
    # a Reference to a Tokenized string. A Token should be referenced in the format @TOKEN, e.g \"@nQGywsQE9gbURtrXEjTZwtWqeMdK9nsO\"
    cardToken: str

    # Expiration year
    expirationYear: int

    # Expiration year
    expirationMonth: int

    # Cardholder name (as apears on card)
    cardHolderName: str

class OptionalPayToolsSharedModelsCardStoredCard(TypedDict, total=False):
    cardType: PaymentsCardTypes

class PayToolsSharedModelsCardStoredCard(RequiredPayToolsSharedModelsCardStoredCard, OptionalPayToolsSharedModelsCardStoredCard):
    pass
