# coding: utf-8

"""
    Thola

    REST API for Thola.  For more information look at our Github : https://github.com/inexio/thola  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import thola_client
from thola_client.api.identify_api import IdentifyApi  # noqa: E501
from thola_client.rest import ApiException


class TestIdentifyApi(unittest.TestCase):
    """IdentifyApi unit test stubs"""

    def setUp(self):
        self.api = thola_client.api.identify_api.IdentifyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_identify(self):
        """Test case for identify

        Identifies a device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
