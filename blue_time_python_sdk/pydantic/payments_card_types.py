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


PaymentsCardTypes = Literal["Visa", "AMEX", "BC", "MasterCard", "MC_Alaska", "MC_Canada", "CarteBlanche", "UnionPay", "Discover", "DinersClub", "CartaSi", "CarteBleue", "Dankort", "Delta", "Electron", "JCB", "Maestro", "Switch", "Solo", "Lazer", "Elo", "Hipercard", "enRoute", "UATP"]
