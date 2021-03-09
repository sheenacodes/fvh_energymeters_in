# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Observation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, value: str=None, timestamp: datetime=None):  # noqa: E501
        """Observation - a model defined in Swagger

        :param value: The value of this Observation.  # noqa: E501
        :type value: str
        :param timestamp: The timestamp of this Observation.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            'value': str,
            'timestamp': datetime
        }

        self.attribute_map = {
            'value': 'value',
            'timestamp': 'timestamp'
        }

        self._value = value
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'Observation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Observation of this Observation.  # noqa: E501
        :rtype: Observation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this Observation.


        :return: The value of this Observation.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Observation.


        :param value: The value of this Observation.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this Observation.


        :return: The timestamp of this Observation.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this Observation.


        :param timestamp: The timestamp of this Observation.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp
