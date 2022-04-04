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

class AssetInstanceInfo(object):
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
        'token_id': 'str',
        'index': 'int',
        'amount': 'int',
        'name': 'str',
        'decimals': 'int',
        'type': 'str'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'index': 'index',
        'amount': 'amount',
        'name': 'name',
        'decimals': 'decimals',
        'type': 'type'
    }

    def __init__(self, token_id=None, index=None, amount=None, name=None, decimals=None, type=None):  # noqa: E501
        """AssetInstanceInfo - a model defined in Swagger"""  # noqa: E501
        self._token_id = None
        self._index = None
        self._amount = None
        self._name = None
        self._decimals = None
        self._type = None
        self.discriminator = None
        self.token_id = token_id
        self.index = index
        self.amount = amount
        if name is not None:
            self.name = name
        if decimals is not None:
            self.decimals = decimals
        if type is not None:
            self.type = type

    @property
    def token_id(self):
        """Gets the token_id of this AssetInstanceInfo.  # noqa: E501

        Token ID  # noqa: E501

        :return: The token_id of this AssetInstanceInfo.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this AssetInstanceInfo.

        Token ID  # noqa: E501

        :param token_id: The token_id of this AssetInstanceInfo.  # noqa: E501
        :type: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def index(self):
        """Gets the index of this AssetInstanceInfo.  # noqa: E501

        Index of the asset in an output  # noqa: E501

        :return: The index of this AssetInstanceInfo.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this AssetInstanceInfo.

        Index of the asset in an output  # noqa: E501

        :param index: The index of this AssetInstanceInfo.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def amount(self):
        """Gets the amount of this AssetInstanceInfo.  # noqa: E501

        Amount of tokens  # noqa: E501

        :return: The amount of this AssetInstanceInfo.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AssetInstanceInfo.

        Amount of tokens  # noqa: E501

        :param amount: The amount of this AssetInstanceInfo.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def name(self):
        """Gets the name of this AssetInstanceInfo.  # noqa: E501

        Name of a token  # noqa: E501

        :return: The name of this AssetInstanceInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetInstanceInfo.

        Name of a token  # noqa: E501

        :param name: The name of this AssetInstanceInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def decimals(self):
        """Gets the decimals of this AssetInstanceInfo.  # noqa: E501

        Number of decimal places  # noqa: E501

        :return: The decimals of this AssetInstanceInfo.  # noqa: E501
        :rtype: int
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this AssetInstanceInfo.

        Number of decimal places  # noqa: E501

        :param decimals: The decimals of this AssetInstanceInfo.  # noqa: E501
        :type: int
        """

        self._decimals = decimals

    @property
    def type(self):
        """Gets the type of this AssetInstanceInfo.  # noqa: E501

        Type of a token (token standard)  # noqa: E501

        :return: The type of this AssetInstanceInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssetInstanceInfo.

        Type of a token (token standard)  # noqa: E501

        :param type: The type of this AssetInstanceInfo.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(AssetInstanceInfo, dict):
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
        if not isinstance(other, AssetInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other