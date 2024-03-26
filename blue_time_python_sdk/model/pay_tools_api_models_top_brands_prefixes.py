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


class PayToolsApiModelsTopBrandsPrefixes(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Top credit card brands for lookup of up to 5 first digits. It covers 90% of the cases
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PayToolsApiModelsTopBrandsPrefixesItem']:
            return PayToolsApiModelsTopBrandsPrefixesItem


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PayToolsApiModelsTopBrandsPrefixes':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )

from blue_time_python_sdk.model.pay_tools_api_models_top_brands_prefixes_item import PayToolsApiModelsTopBrandsPrefixesItem
