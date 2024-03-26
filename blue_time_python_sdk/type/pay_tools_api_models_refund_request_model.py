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

from blue_time_python_sdk.type.pay_tools_api_models_card_input_model import PayToolsApiModelsCardInputModel
from blue_time_python_sdk.type.pay_tools_api_models_payer_details import PayToolsApiModelsPayerDetails
from blue_time_python_sdk.type.pay_tools_api_models_payment_gateway_account import PayToolsApiModelsPaymentGatewayAccount
from blue_time_python_sdk.type.payments_network_token_schemes import PaymentsNetworkTokenSchemes

class RequiredPayToolsApiModelsRefundRequestModel(TypedDict):
    # The currency of the transaction. Based on the <a href=\"https://en.wikipedia.org/wiki/ISO_4217#Active_codes\" target=\"_blank\">ISO 4217</a> standard.
    currency: str

    # The transaction ID that this operation is referring to.
    refTransId: str

    card: PayToolsApiModelsCardInputModel

    # The amount to be charged (the amount should be in major units - for example, 10.23)
    amount: typing.Union[int, float]

class OptionalPayToolsApiModelsRefundRequestModel(TypedDict, total=False):
    payerDetails: PayToolsApiModelsPayerDetails

    # Your custom reference for this transaction
    myRef: typing.Optional[str]

    # The reference name provided to the stored Payment Gateway Account as set in `PUT /PaymentGatewayAccounts/{name}`.  **Please note**, if you provide us with both this parameter and the raw credentials in the `paymentGatewayAccount` object, this parameter will be ignored and the raw credentials will take precedence.
    paymentGatewayAccountName: typing.Optional[str]

    # Optional parameter if the payment gateway requires authentication using a client certificate. The name of the certificate that was stored in our system via our <a href=\"https://portal.epaytools.com\" target=\"_blank\">users portal</a>
    certificateName: typing.Optional[str]

    paymentGatewayAccount: PayToolsApiModelsPaymentGatewayAccount

    networkTokenBrand: PaymentsNetworkTokenSchemes

class PayToolsApiModelsRefundRequestModel(RequiredPayToolsApiModelsRefundRequestModel, OptionalPayToolsApiModelsRefundRequestModel):
    pass
