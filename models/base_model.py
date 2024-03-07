#!/usr/bin/python3

"""
Base Module: The definition, documentation and encapsulation of all common
attributes and methods for the project's classes
"""


from uuid import uuid4


class BaseModel:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the project's classes
    """

    def __init__(self):
        self.__id = str(uuid4())

    @property
    def id(self):
        return self.__id
