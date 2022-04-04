# coding: utf-8

"""
    Ergo Explorer API v1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_v1_addresses_p1_balance_confirmed(self):
        """Test case for get_api_v1_addresses_p1_balance_confirmed

        """
        pass

    def test_get_api_v1_addresses_p1_balance_total(self):
        """Test case for get_api_v1_addresses_p1_balance_total

        """
        pass

    def test_get_api_v1_addresses_p1_transactions(self):
        """Test case for get_api_v1_addresses_p1_transactions

        """
        pass

    def test_get_api_v1_assets(self):
        """Test case for get_api_v1_assets

        """
        pass

    def test_get_api_v1_assets_search_bytokenid(self):
        """Test case for get_api_v1_assets_search_bytokenid

        """
        pass

    def test_get_api_v1_blocks(self):
        """Test case for get_api_v1_blocks

        """
        pass

    def test_get_api_v1_blocks_byglobalindex_stream(self):
        """Test case for get_api_v1_blocks_byglobalindex_stream

        """
        pass

    def test_get_api_v1_blocks_headers(self):
        """Test case for get_api_v1_blocks_headers

        """
        pass

    def test_get_api_v1_blocks_p1(self):
        """Test case for get_api_v1_blocks_p1

        """
        pass

    def test_get_api_v1_boxes_byaddress_p1(self):
        """Test case for get_api_v1_boxes_byaddress_p1

        """
        pass

    def test_get_api_v1_boxes_byergotree_p1(self):
        """Test case for get_api_v1_boxes_byergotree_p1

        """
        pass

    def test_get_api_v1_boxes_byergotreetemplatehash_p1(self):
        """Test case for get_api_v1_boxes_byergotreetemplatehash_p1

        """
        pass

    def test_get_api_v1_boxes_byergotreetemplatehash_p1_stream(self):
        """Test case for get_api_v1_boxes_byergotreetemplatehash_p1_stream

        """
        pass

    def test_get_api_v1_boxes_byglobalindex_stream(self):
        """Test case for get_api_v1_boxes_byglobalindex_stream

        """
        pass

    def test_get_api_v1_boxes_bytokenid_p1(self):
        """Test case for get_api_v1_boxes_bytokenid_p1

        """
        pass

    def test_get_api_v1_boxes_p1(self):
        """Test case for get_api_v1_boxes_p1

        """
        pass

    def test_get_api_v1_boxes_unspent_byaddress_p1(self):
        """Test case for get_api_v1_boxes_unspent_byaddress_p1

        """
        pass

    def test_get_api_v1_boxes_unspent_byergotree_p1(self):
        """Test case for get_api_v1_boxes_unspent_byergotree_p1

        """
        pass

    def test_get_api_v1_boxes_unspent_byergotreetemplatehash_p1(self):
        """Test case for get_api_v1_boxes_unspent_byergotreetemplatehash_p1

        """
        pass

    def test_get_api_v1_boxes_unspent_byergotreetemplatehash_p1_stream(self):
        """Test case for get_api_v1_boxes_unspent_byergotreetemplatehash_p1_stream

        """
        pass

    def test_get_api_v1_boxes_unspent_byglobalindex_stream(self):
        """Test case for get_api_v1_boxes_unspent_byglobalindex_stream

        """
        pass

    def test_get_api_v1_boxes_unspent_bylastepochs_stream(self):
        """Test case for get_api_v1_boxes_unspent_bylastepochs_stream

        """
        pass

    def test_get_api_v1_boxes_unspent_bytokenid_p1(self):
        """Test case for get_api_v1_boxes_unspent_bytokenid_p1

        """
        pass

    def test_get_api_v1_boxes_unspent_stream(self):
        """Test case for get_api_v1_boxes_unspent_stream

        """
        pass

    def test_get_api_v1_epochs_params(self):
        """Test case for get_api_v1_epochs_params

        """
        pass

    def test_get_api_v1_info(self):
        """Test case for get_api_v1_info

        """
        pass

    def test_get_api_v1_mempool_boxes_unspent(self):
        """Test case for get_api_v1_mempool_boxes_unspent

        """
        pass

    def test_get_api_v1_mempool_transactions_byaddress_p1(self):
        """Test case for get_api_v1_mempool_transactions_byaddress_p1

        """
        pass

    def test_get_api_v1_networkstate(self):
        """Test case for get_api_v1_networkstate

        """
        pass

    def test_get_api_v1_networkstats(self):
        """Test case for get_api_v1_networkstats

        """
        pass

    def test_get_api_v1_tokens(self):
        """Test case for get_api_v1_tokens

        """
        pass

    def test_get_api_v1_tokens_bysymbol_p1(self):
        """Test case for get_api_v1_tokens_bysymbol_p1

        """
        pass

    def test_get_api_v1_tokens_p1(self):
        """Test case for get_api_v1_tokens_p1

        """
        pass

    def test_get_api_v1_tokens_search(self):
        """Test case for get_api_v1_tokens_search

        """
        pass

    def test_get_api_v1_transactions_byglobalindex_stream(self):
        """Test case for get_api_v1_transactions_byglobalindex_stream

        """
        pass

    def test_get_api_v1_transactions_byinputsscripttemplatehash_p1(self):
        """Test case for get_api_v1_transactions_byinputsscripttemplatehash_p1

        """
        pass

    def test_get_api_v1_transactions_p1(self):
        """Test case for get_api_v1_transactions_p1

        """
        pass

    def test_post_api_v1_boxes_search(self):
        """Test case for post_api_v1_boxes_search

        """
        pass

    def test_post_api_v1_boxes_unspent_search(self):
        """Test case for post_api_v1_boxes_unspent_search

        """
        pass

    def test_post_api_v1_boxes_unspent_search_union(self):
        """Test case for post_api_v1_boxes_unspent_search_union

        """
        pass

    def test_post_api_v1_mempool_transactions_submit(self):
        """Test case for post_api_v1_mempool_transactions_submit

        """
        pass


if __name__ == '__main__':
    unittest.main()
