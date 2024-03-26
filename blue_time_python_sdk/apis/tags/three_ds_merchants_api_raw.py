# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from blue_time_python_sdk.paths.three_ds_merchants_name.get import GetMerchantInfoRaw
from blue_time_python_sdk.paths.three_ds_merchants.get import ListMerchantsRaw
from blue_time_python_sdk.paths.three_ds_merchants_name.delete import RemoveMerchantRaw
from blue_time_python_sdk.paths.three_ds_merchants_name.put import UpdateMerchantInfoRaw


class ThreeDsMerchantsApiRaw(
    GetMerchantInfoRaw,
    ListMerchantsRaw,
    RemoveMerchantRaw,
    UpdateMerchantInfoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
