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


class CustomFormsUploadFormFolderRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            ContentType = schemas.StrSchema
            ContentDisposition = schemas.StrSchema
        
            @staticmethod
            def Headers() -> typing.Type['CustomFormsUploadFormFolderRequestHeaders']:
                return CustomFormsUploadFormFolderRequestHeaders
            Length = schemas.Int64Schema
            Name = schemas.StrSchema
            FileName = schemas.StrSchema
            __annotations__ = {
                "ContentType": ContentType,
                "ContentDisposition": ContentDisposition,
                "Headers": Headers,
                "Length": Length,
                "Name": Name,
                "FileName": FileName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContentType"]) -> MetaOapg.properties.ContentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContentDisposition"]) -> MetaOapg.properties.ContentDisposition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Headers"]) -> 'CustomFormsUploadFormFolderRequestHeaders': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Length"]) -> MetaOapg.properties.Length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FileName"]) -> MetaOapg.properties.FileName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ContentType", "ContentDisposition", "Headers", "Length", "Name", "FileName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContentType"]) -> typing.Union[MetaOapg.properties.ContentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContentDisposition"]) -> typing.Union[MetaOapg.properties.ContentDisposition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Headers"]) -> typing.Union['CustomFormsUploadFormFolderRequestHeaders', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Length"]) -> typing.Union[MetaOapg.properties.Length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FileName"]) -> typing.Union[MetaOapg.properties.FileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ContentType", "ContentDisposition", "Headers", "Length", "Name", "FileName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ContentType: typing.Union[MetaOapg.properties.ContentType, str, schemas.Unset] = schemas.unset,
        ContentDisposition: typing.Union[MetaOapg.properties.ContentDisposition, str, schemas.Unset] = schemas.unset,
        Headers: typing.Union['CustomFormsUploadFormFolderRequestHeaders', schemas.Unset] = schemas.unset,
        Length: typing.Union[MetaOapg.properties.Length, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        FileName: typing.Union[MetaOapg.properties.FileName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFormsUploadFormFolderRequest':
        return super().__new__(
            cls,
            *args,
            ContentType=ContentType,
            ContentDisposition=ContentDisposition,
            Headers=Headers,
            Length=Length,
            Name=Name,
            FileName=FileName,
            _configuration=_configuration,
            **kwargs,
        )

from blue_time_python_sdk.model.custom_forms_upload_form_folder_request_headers import CustomFormsUploadFormFolderRequestHeaders
