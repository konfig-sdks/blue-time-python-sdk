# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from blue_time_python_sdk.paths.payment_gateway_accounts_name.put import AddOrReplace
from blue_time_python_sdk.paths.payment_gateway_accounts.get import GetAll
from blue_time_python_sdk.paths.payment_gateway_accounts_name.get import GetInfo
from blue_time_python_sdk.paths.payment_gateway_accounts_name.delete import RemoveAccount
from blue_time_python_sdk.apis.tags.payment_gateway_accounts_api_raw import PaymentGatewayAccountsApiRaw


class PaymentGatewayAccountsApi(
    AddOrReplace,
    GetAll,
    GetInfo,
    RemoveAccount,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PaymentGatewayAccountsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PaymentGatewayAccountsApiRaw(api_client)
