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

class OutputInfo1(object):
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
        'tx_id': 'str',
        'value': 'int',
        'index': 'int',
        'creation_height': 'int',
        'ergo_tree': 'str',
        'address': 'str',
        'assets': 'list[AssetInstanceInfo]',
        'additional_registers': 'dict(str, str)',
        'spent_transaction_id': 'str',
        'main_chain': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'tx_id': 'txId',
        'value': 'value',
        'index': 'index',
        'creation_height': 'creationHeight',
        'ergo_tree': 'ergoTree',
        'address': 'address',
        'assets': 'assets',
        'additional_registers': 'additionalRegisters',
        'spent_transaction_id': 'spentTransactionId',
        'main_chain': 'mainChain'
    }

    def __init__(self, id=None, tx_id=None, value=None, index=None, creation_height=None, ergo_tree=None, address=None, assets=None, additional_registers=None, spent_transaction_id=None, main_chain=None):  # noqa: E501
        """OutputInfo1 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tx_id = None
        self._value = None
        self._index = None
        self._creation_height = None
        self._ergo_tree = None
        self._address = None
        self._assets = None
        self._additional_registers = None
        self._spent_transaction_id = None
        self._main_chain = None
        self.discriminator = None
        self.id = id
        self.tx_id = tx_id
        self.value = value
        self.index = index
        self.creation_height = creation_height
        self.ergo_tree = ergo_tree
        self.address = address
        if assets is not None:
            self.assets = assets
        self.additional_registers = additional_registers
        if spent_transaction_id is not None:
            self.spent_transaction_id = spent_transaction_id
        self.main_chain = main_chain

    @property
    def id(self):
        """Gets the id of this OutputInfo1.  # noqa: E501

        Id of the box  # noqa: E501

        :return: The id of this OutputInfo1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OutputInfo1.

        Id of the box  # noqa: E501

        :param id: The id of this OutputInfo1.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def tx_id(self):
        """Gets the tx_id of this OutputInfo1.  # noqa: E501

        Id of the transaction that created the box  # noqa: E501

        :return: The tx_id of this OutputInfo1.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this OutputInfo1.

        Id of the transaction that created the box  # noqa: E501

        :param tx_id: The tx_id of this OutputInfo1.  # noqa: E501
        :type: str
        """
        if tx_id is None:
            raise ValueError("Invalid value for `tx_id`, must not be `None`")  # noqa: E501

        self._tx_id = tx_id

    @property
    def value(self):
        """Gets the value of this OutputInfo1.  # noqa: E501

        Value of the box in nanoERG  # noqa: E501

        :return: The value of this OutputInfo1.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OutputInfo1.

        Value of the box in nanoERG  # noqa: E501

        :param value: The value of this OutputInfo1.  # noqa: E501
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def index(self):
        """Gets the index of this OutputInfo1.  # noqa: E501

        Index of the output in a transaction  # noqa: E501

        :return: The index of this OutputInfo1.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this OutputInfo1.

        Index of the output in a transaction  # noqa: E501

        :param index: The index of this OutputInfo1.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def creation_height(self):
        """Gets the creation_height of this OutputInfo1.  # noqa: E501

        Height at which the box was created  # noqa: E501

        :return: The creation_height of this OutputInfo1.  # noqa: E501
        :rtype: int
        """
        return self._creation_height

    @creation_height.setter
    def creation_height(self, creation_height):
        """Sets the creation_height of this OutputInfo1.

        Height at which the box was created  # noqa: E501

        :param creation_height: The creation_height of this OutputInfo1.  # noqa: E501
        :type: int
        """
        if creation_height is None:
            raise ValueError("Invalid value for `creation_height`, must not be `None`")  # noqa: E501

        self._creation_height = creation_height

    @property
    def ergo_tree(self):
        """Gets the ergo_tree of this OutputInfo1.  # noqa: E501

        Serialized ergo tree  # noqa: E501

        :return: The ergo_tree of this OutputInfo1.  # noqa: E501
        :rtype: str
        """
        return self._ergo_tree

    @ergo_tree.setter
    def ergo_tree(self, ergo_tree):
        """Sets the ergo_tree of this OutputInfo1.

        Serialized ergo tree  # noqa: E501

        :param ergo_tree: The ergo_tree of this OutputInfo1.  # noqa: E501
        :type: str
        """
        if ergo_tree is None:
            raise ValueError("Invalid value for `ergo_tree`, must not be `None`")  # noqa: E501

        self._ergo_tree = ergo_tree

    @property
    def address(self):
        """Gets the address of this OutputInfo1.  # noqa: E501

        An address derived from ergo tree  # noqa: E501

        :return: The address of this OutputInfo1.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OutputInfo1.

        An address derived from ergo tree  # noqa: E501

        :param address: The address of this OutputInfo1.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def assets(self):
        """Gets the assets of this OutputInfo1.  # noqa: E501


        :return: The assets of this OutputInfo1.  # noqa: E501
        :rtype: list[AssetInstanceInfo]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this OutputInfo1.


        :param assets: The assets of this OutputInfo1.  # noqa: E501
        :type: list[AssetInstanceInfo]
        """

        self._assets = assets

    @property
    def additional_registers(self):
        """Gets the additional_registers of this OutputInfo1.  # noqa: E501


        :return: The additional_registers of this OutputInfo1.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_registers

    @additional_registers.setter
    def additional_registers(self, additional_registers):
        """Sets the additional_registers of this OutputInfo1.


        :param additional_registers: The additional_registers of this OutputInfo1.  # noqa: E501
        :type: dict(str, str)
        """
        if additional_registers is None:
            raise ValueError("Invalid value for `additional_registers`, must not be `None`")  # noqa: E501

        self._additional_registers = additional_registers

    @property
    def spent_transaction_id(self):
        """Gets the spent_transaction_id of this OutputInfo1.  # noqa: E501

        Transaction ID  # noqa: E501

        :return: The spent_transaction_id of this OutputInfo1.  # noqa: E501
        :rtype: str
        """
        return self._spent_transaction_id

    @spent_transaction_id.setter
    def spent_transaction_id(self, spent_transaction_id):
        """Sets the spent_transaction_id of this OutputInfo1.

        Transaction ID  # noqa: E501

        :param spent_transaction_id: The spent_transaction_id of this OutputInfo1.  # noqa: E501
        :type: str
        """

        self._spent_transaction_id = spent_transaction_id

    @property
    def main_chain(self):
        """Gets the main_chain of this OutputInfo1.  # noqa: E501


        :return: The main_chain of this OutputInfo1.  # noqa: E501
        :rtype: bool
        """
        return self._main_chain

    @main_chain.setter
    def main_chain(self, main_chain):
        """Sets the main_chain of this OutputInfo1.


        :param main_chain: The main_chain of this OutputInfo1.  # noqa: E501
        :type: bool
        """
        if main_chain is None:
            raise ValueError("Invalid value for `main_chain`, must not be `None`")  # noqa: E501

        self._main_chain = main_chain

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
        if issubclass(OutputInfo1, dict):
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
        if not isinstance(other, OutputInfo1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other