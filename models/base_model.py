#!/usr/bin/python3

"""
Base Module: The definition, documentation and encapsulation of all common
attributes and methods for the project's classes
"""


from datetime import datetime
import uuid


class BaseModel:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the project's classes
    """

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.__init_default()
        else:
            self.__init_kwargs(kwargs)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_ = {
            key.replace("_BaseModel__", ""): value.isoformat()
            if not isinstance(value, str) else value
            for key, value in sorted(self.__dict__.items())
        }

        return {
            "__class__": self.__class__.__name__,
            **dict_,
        }

    def __init_default(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __init_kwargs(self, kwargs):
        dt_attr = ["created_at", "updated_at"]

        for attr, value in kwargs.items():
            if attr in dt_attr:
                format = "%Y-%m-%dT%H:%M:%S.%f"
                value = datetime.strptime(value, format)

            self.__dict__[attr] = value

    def __setattr__(self, name, value):
        if name.count("updated_at"):
            return super().__setattr__(name, value)
        self.__dict__["updated_at"] = datetime.now()
        super().__setattr__(name, value)

    def __str__(self):
        dict_ = {
            key: value
            for key, value in sorted(self.__dict__.items())
        }

        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {dict_}"
