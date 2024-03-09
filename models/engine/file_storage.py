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

    def new(self, obj):
        """
        Updates tracked items with the retrieval key of
        <obj class name>.id

        Parameter
        ---------
        obj : BaseModel | subclass(BaseModel)
            object to be tracked
        """

        key = self.__extract_key(obj)
        self.__objects[key] = obj

    @staticmethod
    def __extract_key(obj):
        """
        Updates tracked items with the retrieval key of
        <obj class name>.id

        Parameter
        ---------
        obj : Any
            object to be tracked
        """

        dict_ = obj.to_dict()
        cls = dict_.get("__class__")
        id_ = dict_.get("id")
        return f"{cls}.{id_}"
