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

    @classmethod
    def all(cls):
        """
        Prints a list of string representations of all instances.
        Where class name is provided, instances are scoped to said
        class. Where no class name is provided, all instance
        representations are printed.
        """

        list_of_kwargs = cls.__get_list_of_instance_kwargs()

        for kwargs in list_of_kwargs:

            kwargs_copy = kwargs.copy()
            kwargs_copy.pop("__class__")

            model = models.MODELS.get(kwargs.get("__class__"))
            instance = model(**kwargs_copy)

            print(instance)

    @classmethod
    def count(cls):
        """Display number of all class specific instances in storage"""

        list_of_kwargs = cls.__get_list_of_instance_kwargs()
        len_ = len(list_of_kwargs)
        print(len_)

    @staticmethod
    def is_valid_instance_id(instance_id):
        """
        Validates instance id as being existant

        Parameter
        ---------
        instance_id : str
            uuid of class instance

        Return
        ------
        bool
            True if uuid matches one of the stored
            instances else False
        """

        keys = storage.all().keys()

        elements = [
            element
            for key in keys
            for element in key.split(".")
        ]

        if not instance_id:
            print("** instance id missing **")
            return False

        if instance_id not in elements:
            print("** no instance found **")
            return False

        return True

    @staticmethod
    def is_valid_model_name(model_name):
        """
        Validates class name as being existant

        Parameter
        ---------
        model_name : str
            the name of the model (class) being
            validated

        Return
        ------
        bool
            True if model name is present in
            the system else False
        """

        if not model_name:
            print("** class name missing **")
            return False

        if model_name not in models.MODELS:
            print("** class doesn't exist **")
            return False

        return True

    def save(self):
        """Update the `updated_at` attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    @classmethod
    def show(cls, instance_id):
        key = f"{cls.__name__}.{instance_id}"
        kwargs = models.storage.all().get(key)

        Model = models.MODELS.get(cls.__name__)
        model = Model(**kwargs)

        print(model)

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

    @classmethod
    def __get_list_of_instance_kwargs(cls):
        """
        Provides list of kwargs needed to spawn each stored
        instance as determined by parent/child making the
        call
        """

        return [
            instance
            for instance in models.storage.all().values()
            if instance.get("__class__") == cls.__name__
        ]

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
