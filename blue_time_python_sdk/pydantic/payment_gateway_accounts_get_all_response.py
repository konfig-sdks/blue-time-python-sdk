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

from blue_time_python_sdk.pydantic.pay_tools_api_models_payment_gateway_account_brief_output_model import PayToolsApiModelsPaymentGatewayAccountBriefOutputModel

PaymentGatewayAccountsGetAllResponse = typing.List[PayToolsApiModelsPaymentGatewayAccountBriefOutputModel]
