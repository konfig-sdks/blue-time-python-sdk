# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import blue_time_python_sdk
from blue_time_python_sdk.paths.three_ds_sessions import post
from blue_time_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestThreeDsSessions(ApiTestMixin, unittest.TestCase):
    """
    ThreeDsSessions unit test stubs
        Get a token to start a card operation
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
