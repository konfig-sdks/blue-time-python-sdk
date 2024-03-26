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


class PayToolsSharedEnumsPerform3ds(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Options for performing #DS
    """


    class MetaOapg:
        enum_value_to_name = {
            "Mandatory": "MANDATORY",
            "Skip": "SKIP",
            "Optional": "OPTIONAL",
        }
    
    @schemas.classproperty
    def MANDATORY(cls):
        return cls("Mandatory")
    
    @schemas.classproperty
    def SKIP(cls):
        return cls("Skip")
    
    @schemas.classproperty
    def OPTIONAL(cls):
        return cls("Optional")
