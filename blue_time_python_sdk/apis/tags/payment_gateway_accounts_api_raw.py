# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from blue_time_python_sdk.paths.payment_gateway_accounts_name.put import AddOrReplaceRaw
from blue_time_python_sdk.paths.payment_gateway_accounts.get import GetAllRaw
from blue_time_python_sdk.paths.payment_gateway_accounts_name.get import GetInfoRaw
from blue_time_python_sdk.paths.payment_gateway_accounts_name.delete import RemoveAccountRaw


class PaymentGatewayAccountsApiRaw(
    AddOrReplaceRaw,
    GetAllRaw,
    GetInfoRaw,
    RemoveAccountRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
