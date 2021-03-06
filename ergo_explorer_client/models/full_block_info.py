# coding: utf-8

"""
    Ergo Explorer API v1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FullBlockInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'header': 'HeaderInfo',
        'block_transactions': 'list[TransactionInfo1]',
        'extension': 'BlockExtensionInfo',
        'ad_proofs': 'str'
    }

    attribute_map = {
        'header': 'header',
        'block_transactions': 'blockTransactions',
        'extension': 'extension',
        'ad_proofs': 'adProofs'
    }

    def __init__(self, header=None, block_transactions=None, extension=None, ad_proofs=None):  # noqa: E501
        """FullBlockInfo - a model defined in Swagger"""  # noqa: E501
        self._header = None
        self._block_transactions = None
        self._extension = None
        self._ad_proofs = None
        self.discriminator = None
        self.header = header
        if block_transactions is not None:
            self.block_transactions = block_transactions
        self.extension = extension
        if ad_proofs is not None:
            self.ad_proofs = ad_proofs

    @property
    def header(self):
        """Gets the header of this FullBlockInfo.  # noqa: E501


        :return: The header of this FullBlockInfo.  # noqa: E501
        :rtype: HeaderInfo
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this FullBlockInfo.


        :param header: The header of this FullBlockInfo.  # noqa: E501
        :type: HeaderInfo
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def block_transactions(self):
        """Gets the block_transactions of this FullBlockInfo.  # noqa: E501


        :return: The block_transactions of this FullBlockInfo.  # noqa: E501
        :rtype: list[TransactionInfo1]
        """
        return self._block_transactions

    @block_transactions.setter
    def block_transactions(self, block_transactions):
        """Sets the block_transactions of this FullBlockInfo.


        :param block_transactions: The block_transactions of this FullBlockInfo.  # noqa: E501
        :type: list[TransactionInfo1]
        """

        self._block_transactions = block_transactions

    @property
    def extension(self):
        """Gets the extension of this FullBlockInfo.  # noqa: E501


        :return: The extension of this FullBlockInfo.  # noqa: E501
        :rtype: BlockExtensionInfo
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this FullBlockInfo.


        :param extension: The extension of this FullBlockInfo.  # noqa: E501
        :type: BlockExtensionInfo
        """
        if extension is None:
            raise ValueError("Invalid value for `extension`, must not be `None`")  # noqa: E501

        self._extension = extension

    @property
    def ad_proofs(self):
        """Gets the ad_proofs of this FullBlockInfo.  # noqa: E501

        Serialized hex-encoded AD Proofs  # noqa: E501

        :return: The ad_proofs of this FullBlockInfo.  # noqa: E501
        :rtype: str
        """
        return self._ad_proofs

    @ad_proofs.setter
    def ad_proofs(self, ad_proofs):
        """Sets the ad_proofs of this FullBlockInfo.

        Serialized hex-encoded AD Proofs  # noqa: E501

        :param ad_proofs: The ad_proofs of this FullBlockInfo.  # noqa: E501
        :type: str
        """

        self._ad_proofs = ad_proofs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FullBlockInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FullBlockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
