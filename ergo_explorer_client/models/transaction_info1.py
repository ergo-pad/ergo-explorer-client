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

class TransactionInfo1(object):
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
        'header_id': 'str',
        'inclusion_height': 'int',
        'timestamp': 'int',
        'index': 'int',
        'confirmations_count': 'int',
        'inputs': 'list[InputInfo1]',
        'data_inputs': 'list[DataInputInfo1]',
        'outputs': 'list[OutputInfo1]'
    }

    attribute_map = {
        'id': 'id',
        'header_id': 'headerId',
        'inclusion_height': 'inclusionHeight',
        'timestamp': 'timestamp',
        'index': 'index',
        'confirmations_count': 'confirmationsCount',
        'inputs': 'inputs',
        'data_inputs': 'dataInputs',
        'outputs': 'outputs'
    }

    def __init__(self, id=None, header_id=None, inclusion_height=None, timestamp=None, index=None, confirmations_count=None, inputs=None, data_inputs=None, outputs=None):  # noqa: E501
        """TransactionInfo1 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._header_id = None
        self._inclusion_height = None
        self._timestamp = None
        self._index = None
        self._confirmations_count = None
        self._inputs = None
        self._data_inputs = None
        self._outputs = None
        self.discriminator = None
        self.id = id
        self.header_id = header_id
        self.inclusion_height = inclusion_height
        self.timestamp = timestamp
        self.index = index
        self.confirmations_count = confirmations_count
        if inputs is not None:
            self.inputs = inputs
        if data_inputs is not None:
            self.data_inputs = data_inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def id(self):
        """Gets the id of this TransactionInfo1.  # noqa: E501

        Transaction ID  # noqa: E501

        :return: The id of this TransactionInfo1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionInfo1.

        Transaction ID  # noqa: E501

        :param id: The id of this TransactionInfo1.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def header_id(self):
        """Gets the header_id of this TransactionInfo1.  # noqa: E501

        ID of the corresponding header  # noqa: E501

        :return: The header_id of this TransactionInfo1.  # noqa: E501
        :rtype: str
        """
        return self._header_id

    @header_id.setter
    def header_id(self, header_id):
        """Sets the header_id of this TransactionInfo1.

        ID of the corresponding header  # noqa: E501

        :param header_id: The header_id of this TransactionInfo1.  # noqa: E501
        :type: str
        """
        if header_id is None:
            raise ValueError("Invalid value for `header_id`, must not be `None`")  # noqa: E501

        self._header_id = header_id

    @property
    def inclusion_height(self):
        """Gets the inclusion_height of this TransactionInfo1.  # noqa: E501

        Height of the block the transaction was included in  # noqa: E501

        :return: The inclusion_height of this TransactionInfo1.  # noqa: E501
        :rtype: int
        """
        return self._inclusion_height

    @inclusion_height.setter
    def inclusion_height(self, inclusion_height):
        """Sets the inclusion_height of this TransactionInfo1.

        Height of the block the transaction was included in  # noqa: E501

        :param inclusion_height: The inclusion_height of this TransactionInfo1.  # noqa: E501
        :type: int
        """
        if inclusion_height is None:
            raise ValueError("Invalid value for `inclusion_height`, must not be `None`")  # noqa: E501

        self._inclusion_height = inclusion_height

    @property
    def timestamp(self):
        """Gets the timestamp of this TransactionInfo1.  # noqa: E501

        Timestamp the transaction got into the network  # noqa: E501

        :return: The timestamp of this TransactionInfo1.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TransactionInfo1.

        Timestamp the transaction got into the network  # noqa: E501

        :param timestamp: The timestamp of this TransactionInfo1.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def index(self):
        """Gets the index of this TransactionInfo1.  # noqa: E501

        Index of a transaction inside a block  # noqa: E501

        :return: The index of this TransactionInfo1.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TransactionInfo1.

        Index of a transaction inside a block  # noqa: E501

        :param index: The index of this TransactionInfo1.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def confirmations_count(self):
        """Gets the confirmations_count of this TransactionInfo1.  # noqa: E501

        Number of transaction confirmations  # noqa: E501

        :return: The confirmations_count of this TransactionInfo1.  # noqa: E501
        :rtype: int
        """
        return self._confirmations_count

    @confirmations_count.setter
    def confirmations_count(self, confirmations_count):
        """Sets the confirmations_count of this TransactionInfo1.

        Number of transaction confirmations  # noqa: E501

        :param confirmations_count: The confirmations_count of this TransactionInfo1.  # noqa: E501
        :type: int
        """
        if confirmations_count is None:
            raise ValueError("Invalid value for `confirmations_count`, must not be `None`")  # noqa: E501

        self._confirmations_count = confirmations_count

    @property
    def inputs(self):
        """Gets the inputs of this TransactionInfo1.  # noqa: E501


        :return: The inputs of this TransactionInfo1.  # noqa: E501
        :rtype: list[InputInfo1]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TransactionInfo1.


        :param inputs: The inputs of this TransactionInfo1.  # noqa: E501
        :type: list[InputInfo1]
        """

        self._inputs = inputs

    @property
    def data_inputs(self):
        """Gets the data_inputs of this TransactionInfo1.  # noqa: E501


        :return: The data_inputs of this TransactionInfo1.  # noqa: E501
        :rtype: list[DataInputInfo1]
        """
        return self._data_inputs

    @data_inputs.setter
    def data_inputs(self, data_inputs):
        """Sets the data_inputs of this TransactionInfo1.


        :param data_inputs: The data_inputs of this TransactionInfo1.  # noqa: E501
        :type: list[DataInputInfo1]
        """

        self._data_inputs = data_inputs

    @property
    def outputs(self):
        """Gets the outputs of this TransactionInfo1.  # noqa: E501


        :return: The outputs of this TransactionInfo1.  # noqa: E501
        :rtype: list[OutputInfo1]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TransactionInfo1.


        :param outputs: The outputs of this TransactionInfo1.  # noqa: E501
        :type: list[OutputInfo1]
        """

        self._outputs = outputs

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
        if issubclass(TransactionInfo1, dict):
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
        if not isinstance(other, TransactionInfo1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
