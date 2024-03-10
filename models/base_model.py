#!/usr/bin/python3

"""
Base Module: The definition, documentation and encapsulation of all common
attributes and methods for the project's classes
"""


from importlib import import_module
from datetime import datetime
import datetime as dt
import uuid


models = import_module("models")


class BaseModel:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the project's classes
    """

    def __init__(self, *args, **kwargs):
        """
        Spawns an existing object or generates a new one

        Parameters
        ----------
        args : Any
            unused

        kwargs : Any
            keyword-to-value pairings used to deserialise
            and spawn existing objects
        """

        if not kwargs:
            self.__init_default()
        else:
            self.__init_kwargs(kwargs)

    def save(self):
        """Update the `updated_at` attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Serialises BaseModel's attributes into a `dict`"""

        dict_ = {
            key: value.isoformat()
            if isinstance(value, dt.datetime) else value
            for key, value in sorted(self.__dict__.items())
        }

        return {
            "__class__": self.__class__.__name__,
            **dict_,
        }

    def __init_default(self):
        """Generates a new BaseModel object"""

        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        models.storage.new(self)

    def __init_kwargs(self, kwargs):
        """
        Spawns an existing object

        Parameters
        ----------
        kwargs : Any
            keyword-to-value pairings used to deserialise
            and spawn existing objects
        """

        dt_attr = ["created_at", "updated_at"]

        for attr, value in kwargs.items():

            if attr in dt_attr:
                format = "%Y-%m-%dT%H:%M:%S.%f"
                value = datetime.strptime(value, format)

            self.__dict__[attr] = value

    def __setattr__(self, name, value):
        """
        Customised process when creating or updating an
        attribute, principally to update the `updated_at`
        attribute to the time of use

        Parameters
        ----------
        name : str
            the name of the attribute

        value : Any
            the value being assigned to the provided
            attribute
        """

        if name.count("updated_at"):
            return super().__setattr__(name, value)
        self.__dict__["updated_at"] = datetime.now()
        super().__setattr__(name, value)

    def __str__(self):
        """String representation of BaseModel instance"""

        dict_ = {
            key: value
            for key, value in sorted(self.__dict__.items())
        }

        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {dict_}"
