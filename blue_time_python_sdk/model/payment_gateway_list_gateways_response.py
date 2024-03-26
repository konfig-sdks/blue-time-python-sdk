# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from blue_time_python_sdk import schemas  # noqa: F401


class PaymentGatewayListGatewaysResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PayToolsApiModelsPaymentGatewayDescriptionModel']:
            return PayToolsApiModelsPaymentGatewayDescriptionModel

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PayToolsApiModelsPaymentGatewayDescriptionModel'], typing.List['PayToolsApiModelsPaymentGatewayDescriptionModel']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PaymentGatewayListGatewaysResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PayToolsApiModelsPaymentGatewayDescriptionModel':
        return super().__getitem__(i)

from blue_time_python_sdk.model.pay_tools_api_models_payment_gateway_description_model import PayToolsApiModelsPaymentGatewayDescriptionModel
