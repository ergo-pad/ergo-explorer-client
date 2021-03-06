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

class TokenInfo(object):
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
        'id': 'str',
        'box_id': 'str',
        'emission_amount': 'int',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'decimals': 'int'
    }

    attribute_map = {
        'id': 'id',
        'box_id': 'boxId',
        'emission_amount': 'emissionAmount',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'decimals': 'decimals'
    }

    def __init__(self, id=None, box_id=None, emission_amount=None, name=None, description=None, type=None, decimals=None):  # noqa: E501
        """TokenInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._box_id = None
        self._emission_amount = None
        self._name = None
        self._description = None
        self._type = None
        self._decimals = None
        self.discriminator = None
        self.id = id
        self.box_id = box_id
        self.emission_amount = emission_amount
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if decimals is not None:
            self.decimals = decimals

    @property
    def id(self):
        """Gets the id of this TokenInfo.  # noqa: E501

        ID of the asset  # noqa: E501

        :return: The id of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokenInfo.

        ID of the asset  # noqa: E501

        :param id: The id of this TokenInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def box_id(self):
        """Gets the box_id of this TokenInfo.  # noqa: E501

        Box ID this asset was issued by  # noqa: E501

        :return: The box_id of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._box_id

    @box_id.setter
    def box_id(self, box_id):
        """Sets the box_id of this TokenInfo.

        Box ID this asset was issued by  # noqa: E501

        :param box_id: The box_id of this TokenInfo.  # noqa: E501
        :type: str
        """
        if box_id is None:
            raise ValueError("Invalid value for `box_id`, must not be `None`")  # noqa: E501

        self._box_id = box_id

    @property
    def emission_amount(self):
        """Gets the emission_amount of this TokenInfo.  # noqa: E501

        Number of decimal places  # noqa: E501

        :return: The emission_amount of this TokenInfo.  # noqa: E501
        :rtype: int
        """
        return self._emission_amount

    @emission_amount.setter
    def emission_amount(self, emission_amount):
        """Sets the emission_amount of this TokenInfo.

        Number of decimal places  # noqa: E501

        :param emission_amount: The emission_amount of this TokenInfo.  # noqa: E501
        :type: int
        """
        if emission_amount is None:
            raise ValueError("Invalid value for `emission_amount`, must not be `None`")  # noqa: E501

        self._emission_amount = emission_amount

    @property
    def name(self):
        """Gets the name of this TokenInfo.  # noqa: E501

        Name of the asset  # noqa: E501

        :return: The name of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenInfo.

        Name of the asset  # noqa: E501

        :param name: The name of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TokenInfo.  # noqa: E501

        Description of the asset  # noqa: E501

        :return: The description of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TokenInfo.

        Description of the asset  # noqa: E501

        :param description: The description of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this TokenInfo.  # noqa: E501

        Asset type (token standard)  # noqa: E501

        :return: The type of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TokenInfo.

        Asset type (token standard)  # noqa: E501

        :param type: The type of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def decimals(self):
        """Gets the decimals of this TokenInfo.  # noqa: E501

        Number of decimal places  # noqa: E501

        :return: The decimals of this TokenInfo.  # noqa: E501
        :rtype: int
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this TokenInfo.

        Number of decimal places  # noqa: E501

        :param decimals: The decimals of this TokenInfo.  # noqa: E501
        :type: int
        """

        self._decimals = decimals

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
        if issubclass(TokenInfo, dict):
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
        if not isinstance(other, TokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
