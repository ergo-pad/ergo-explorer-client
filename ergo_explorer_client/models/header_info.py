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

class HeaderInfo(object):
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
        'parent_id': 'str',
        'version': 'int',
        'height': 'int',
        'epoch': 'int',
        'difficulty': 'str',
        'ad_proofs_root': 'str',
        'state_root': 'str',
        'transactions_root': 'str',
        'timestamp': 'int',
        'n_bits': 'int',
        'size': 'int',
        'extension_hash': 'str',
        'pow_solutions': 'PowSolutionInfo',
        'votes': 'Tuple3ByteByteByte'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parentId',
        'version': 'version',
        'height': 'height',
        'epoch': 'epoch',
        'difficulty': 'difficulty',
        'ad_proofs_root': 'adProofsRoot',
        'state_root': 'stateRoot',
        'transactions_root': 'transactionsRoot',
        'timestamp': 'timestamp',
        'n_bits': 'nBits',
        'size': 'size',
        'extension_hash': 'extensionHash',
        'pow_solutions': 'powSolutions',
        'votes': 'votes'
    }

    def __init__(self, id=None, parent_id=None, version=None, height=None, epoch=None, difficulty=None, ad_proofs_root=None, state_root=None, transactions_root=None, timestamp=None, n_bits=None, size=None, extension_hash=None, pow_solutions=None, votes=None):  # noqa: E501
        """HeaderInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._parent_id = None
        self._version = None
        self._height = None
        self._epoch = None
        self._difficulty = None
        self._ad_proofs_root = None
        self._state_root = None
        self._transactions_root = None
        self._timestamp = None
        self._n_bits = None
        self._size = None
        self._extension_hash = None
        self._pow_solutions = None
        self._votes = None
        self.discriminator = None
        self.id = id
        self.parent_id = parent_id
        self.version = version
        self.height = height
        self.epoch = epoch
        self.difficulty = difficulty
        self.ad_proofs_root = ad_proofs_root
        self.state_root = state_root
        self.transactions_root = transactions_root
        self.timestamp = timestamp
        self.n_bits = n_bits
        self.size = size
        self.extension_hash = extension_hash
        self.pow_solutions = pow_solutions
        self.votes = votes

    @property
    def id(self):
        """Gets the id of this HeaderInfo.  # noqa: E501

        Block/header ID  # noqa: E501

        :return: The id of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HeaderInfo.

        Block/header ID  # noqa: E501

        :param id: The id of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this HeaderInfo.  # noqa: E501

        ID of the parental block/header  # noqa: E501

        :return: The parent_id of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this HeaderInfo.

        ID of the parental block/header  # noqa: E501

        :param parent_id: The parent_id of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def version(self):
        """Gets the version of this HeaderInfo.  # noqa: E501

        Version of the header  # noqa: E501

        :return: The version of this HeaderInfo.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HeaderInfo.

        Version of the header  # noqa: E501

        :param version: The version of this HeaderInfo.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def height(self):
        """Gets the height of this HeaderInfo.  # noqa: E501

        Block/header height  # noqa: E501

        :return: The height of this HeaderInfo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this HeaderInfo.

        Block/header height  # noqa: E501

        :param height: The height of this HeaderInfo.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def epoch(self):
        """Gets the epoch of this HeaderInfo.  # noqa: E501

        Block/header epoch (Epochs are enumerated from 0)  # noqa: E501

        :return: The epoch of this HeaderInfo.  # noqa: E501
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this HeaderInfo.

        Block/header epoch (Epochs are enumerated from 0)  # noqa: E501

        :param epoch: The epoch of this HeaderInfo.  # noqa: E501
        :type: int
        """
        if epoch is None:
            raise ValueError("Invalid value for `epoch`, must not be `None`")  # noqa: E501

        self._epoch = epoch

    @property
    def difficulty(self):
        """Gets the difficulty of this HeaderInfo.  # noqa: E501

        Block/header difficulty  # noqa: E501

        :return: The difficulty of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty of this HeaderInfo.

        Block/header difficulty  # noqa: E501

        :param difficulty: The difficulty of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if difficulty is None:
            raise ValueError("Invalid value for `difficulty`, must not be `None`")  # noqa: E501

        self._difficulty = difficulty

    @property
    def ad_proofs_root(self):
        """Gets the ad_proofs_root of this HeaderInfo.  # noqa: E501

        Hex-encoded root of the corresponding AD proofs  # noqa: E501

        :return: The ad_proofs_root of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._ad_proofs_root

    @ad_proofs_root.setter
    def ad_proofs_root(self, ad_proofs_root):
        """Sets the ad_proofs_root of this HeaderInfo.

        Hex-encoded root of the corresponding AD proofs  # noqa: E501

        :param ad_proofs_root: The ad_proofs_root of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if ad_proofs_root is None:
            raise ValueError("Invalid value for `ad_proofs_root`, must not be `None`")  # noqa: E501

        self._ad_proofs_root = ad_proofs_root

    @property
    def state_root(self):
        """Gets the state_root of this HeaderInfo.  # noqa: E501

        Hex-encoded root of the corresponding state  # noqa: E501

        :return: The state_root of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._state_root

    @state_root.setter
    def state_root(self, state_root):
        """Sets the state_root of this HeaderInfo.

        Hex-encoded root of the corresponding state  # noqa: E501

        :param state_root: The state_root of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if state_root is None:
            raise ValueError("Invalid value for `state_root`, must not be `None`")  # noqa: E501

        self._state_root = state_root

    @property
    def transactions_root(self):
        """Gets the transactions_root of this HeaderInfo.  # noqa: E501

        Hex-encoded root of the corresponding transactions  # noqa: E501

        :return: The transactions_root of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._transactions_root

    @transactions_root.setter
    def transactions_root(self, transactions_root):
        """Sets the transactions_root of this HeaderInfo.

        Hex-encoded root of the corresponding transactions  # noqa: E501

        :param transactions_root: The transactions_root of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if transactions_root is None:
            raise ValueError("Invalid value for `transactions_root`, must not be `None`")  # noqa: E501

        self._transactions_root = transactions_root

    @property
    def timestamp(self):
        """Gets the timestamp of this HeaderInfo.  # noqa: E501

        Timestamp the block/header was created  # noqa: E501

        :return: The timestamp of this HeaderInfo.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this HeaderInfo.

        Timestamp the block/header was created  # noqa: E501

        :param timestamp: The timestamp of this HeaderInfo.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def n_bits(self):
        """Gets the n_bits of this HeaderInfo.  # noqa: E501

        Encoded required difficulty  # noqa: E501

        :return: The n_bits of this HeaderInfo.  # noqa: E501
        :rtype: int
        """
        return self._n_bits

    @n_bits.setter
    def n_bits(self, n_bits):
        """Sets the n_bits of this HeaderInfo.

        Encoded required difficulty  # noqa: E501

        :param n_bits: The n_bits of this HeaderInfo.  # noqa: E501
        :type: int
        """
        if n_bits is None:
            raise ValueError("Invalid value for `n_bits`, must not be `None`")  # noqa: E501

        self._n_bits = n_bits

    @property
    def size(self):
        """Gets the size of this HeaderInfo.  # noqa: E501

        Size of the header in bytes  # noqa: E501

        :return: The size of this HeaderInfo.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this HeaderInfo.

        Size of the header in bytes  # noqa: E501

        :param size: The size of this HeaderInfo.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def extension_hash(self):
        """Gets the extension_hash of this HeaderInfo.  # noqa: E501

        Hex-encoded hash of the corresponding extension  # noqa: E501

        :return: The extension_hash of this HeaderInfo.  # noqa: E501
        :rtype: str
        """
        return self._extension_hash

    @extension_hash.setter
    def extension_hash(self, extension_hash):
        """Sets the extension_hash of this HeaderInfo.

        Hex-encoded hash of the corresponding extension  # noqa: E501

        :param extension_hash: The extension_hash of this HeaderInfo.  # noqa: E501
        :type: str
        """
        if extension_hash is None:
            raise ValueError("Invalid value for `extension_hash`, must not be `None`")  # noqa: E501

        self._extension_hash = extension_hash

    @property
    def pow_solutions(self):
        """Gets the pow_solutions of this HeaderInfo.  # noqa: E501


        :return: The pow_solutions of this HeaderInfo.  # noqa: E501
        :rtype: PowSolutionInfo
        """
        return self._pow_solutions

    @pow_solutions.setter
    def pow_solutions(self, pow_solutions):
        """Sets the pow_solutions of this HeaderInfo.


        :param pow_solutions: The pow_solutions of this HeaderInfo.  # noqa: E501
        :type: PowSolutionInfo
        """
        if pow_solutions is None:
            raise ValueError("Invalid value for `pow_solutions`, must not be `None`")  # noqa: E501

        self._pow_solutions = pow_solutions

    @property
    def votes(self):
        """Gets the votes of this HeaderInfo.  # noqa: E501


        :return: The votes of this HeaderInfo.  # noqa: E501
        :rtype: Tuple3ByteByteByte
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this HeaderInfo.


        :param votes: The votes of this HeaderInfo.  # noqa: E501
        :type: Tuple3ByteByteByte
        """
        if votes is None:
            raise ValueError("Invalid value for `votes`, must not be `None`")  # noqa: E501

        self._votes = votes

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
        if issubclass(HeaderInfo, dict):
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
        if not isinstance(other, HeaderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
