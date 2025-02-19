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

from blue_time_python_sdk.pydantic.payments_card_types import PaymentsCardTypes

class PayToolsSharedModelsCardStoredCard(BaseModel):
    # a Reference to a Tokenized string. A Token should be referenced in the format @TOKEN, e.g \"@nQGywsQE9gbURtrXEjTZwtWqeMdK9nsO\"
    card_token: str = Field(alias='cardToken')

    # Expiration year
    expiration_year: int = Field(alias='expirationYear')

    # Expiration year
    expiration_month: int = Field(alias='expirationMonth')

    # Cardholder name (as apears on card)
    card_holder_name: str = Field(alias='cardHolderName')

    card_type: typing.Optional[PaymentsCardTypes] = Field(None, alias='cardType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
