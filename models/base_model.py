#!/usr/bin/python3

"""
Base Module: The definition, documentation and encapsulation of all common
attributes and methods for the project's classes
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the project's classes
    """

    def __init__(self):
        self.__created_at = self.updated_at = datetime.now()
        self.__id = str(uuid4())

    @property
    def id(self):
        return self.__id

    @property
    def created_at(self):
        return self.__created_at

    def save(self):
        self.updated_at = datetime.now()
