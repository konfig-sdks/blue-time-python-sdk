# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from blue_time_python_sdk.paths.three_ds_sessions_challenge_status.get import GetChallengeStatusRaw
from blue_time_python_sdk.paths.three_ds_sessions.post import GetTokenStartOperationRaw
from blue_time_python_sdk.paths.three_ds_sessions_fingerprint_callback_session_id.post import HandleFingerprintCallbackRaw
from blue_time_python_sdk.paths.three_ds_sessions_mpi_challenge_callback_session_id.get import HandleMpiChallengeCallbackRaw
from blue_time_python_sdk.paths.three_ds_sessions_op_validate.get import PerformValidationOperationRaw


class ThreeDsSessionsApiRaw(
    GetChallengeStatusRaw,
    GetTokenStartOperationRaw,
    HandleFingerprintCallbackRaw,
    HandleMpiChallengeCallbackRaw,
    PerformValidationOperationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
