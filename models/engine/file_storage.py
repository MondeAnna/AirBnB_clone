#!/usr/bin/python3

"""
File Storage: The definition, documentation and encapsulation of all common
attributes and methods for storing BaseModel instances to the file system
"""


from datetime import datetime
import uuid


class FileStorage:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for storing BaseModel instances to the
    file system
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """Provides all the saved BaseModel objects"""

        return self.__objects
