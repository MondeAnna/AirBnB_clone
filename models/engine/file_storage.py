#!/usr/bin/python3

"""
File Storage: The definition, documentation and encapsulation of all common
attributes and methods for storing BaseModel instances to the file system
"""


from datetime import datetime
from pathlib import Path
import json
import uuid


class FileStorage:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for storing BaseModel instances to the
    file system
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Provides all the saved BaseModel objects"""

        return self.__objects

    @property
    def file_path(self):
        return self.__file_path

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
        self.__objects[key] = obj.to_dict()

    def reload(self):
        """Reset tracked objects to contents of `file path"""

        if not Path(self.__file_path).is_file():
            return

        elif not Path(self.__file_path).stat().st_size:
            self.__objects = {}

        else:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

    def save(self):
        """Serialises tracked objects"""

        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

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
