# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from blue_time_python_sdk.paths.custom_forms.get import GetListRaw
from blue_time_python_sdk.paths.custom_forms_name.delete import RemoveFormRaw
from blue_time_python_sdk.paths.custom_forms_name.put import UploadFormFolderRaw


class CustomFormsApiRaw(
    GetListRaw,
    RemoveFormRaw,
    UploadFormFolderRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
