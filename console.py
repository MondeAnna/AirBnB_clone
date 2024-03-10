#!/usr/bin/python3

"""
Command Line Interface for the product
"""

from collections import OrderedDict
import cmd


from models import BaseModel
from models import User
from models import storage


class HBNBCommand(cmd.Cmd):

    """
    Product's Command Line Interface
    """

    __MODELS = {
        "BaseModel": BaseModel,
        "User": User,
    }
    prompt = "(hbnb) "

    def emptyline(self):
        """Skips to new prompt should input be empty"""

        pass

    def do_all(self, model_name):
        """
        Prints a list of string representations of all instances.
        Where class name is provided, instances are scoped to said
        class. Where no class name is provided, all instance
        representations are printed.

        Parameter
        ---------
        model_name : str
            name of class to be represented

        Expected
        --------
            (hbnb) all
            (hbnb) all BaseModel

        Non-Existant Class
        ------------------
            (hbnb) all DoesNotExist
            ** class doesn't exist **
        """

        if model_name and model_name not in self.__MODELS:
            return print("** class doesn't exist **")

        if not model_name:
            list_of_kwargs = list(storage.all().values())
        else:
            list_of_kwargs = [
                instance
                for instance in storage.all().values()
                if instance.get("__class__") == model_name
            ]

        for kwargs in list_of_kwargs:
            model = self.__MODELS.get(kwargs.get("__class__"))
            kwargs_new = kwargs.copy()
            kwargs_new.pop("__class__")
            instance = model(**kwargs_new)
            print(instance)

    def do_create(self, model_name):
        """
        Creates a new instance, saves it and prints the id. If
        the class name is missing or does not exist, the user
        is informed

        Parameter
        ---------
        model_name : str
            name of class to create

        Expected
        --------
            (hbnb) create BaseModel

        Missing class name
        ------------------
            (hbnb) create
            ** class name missing **

        Non-Existant Class
        ------------------
            (hbnb) create DoesNotExist
            ** class doesn't exist **
        """

        if not self.__is_valid_model_name(model_name):
            return

        Model = self.__MODELS.get(model_name)
        model = Model()
        model.save()
        print(model.id)

    def do_EOF(self, line):
        """Exits the programme when user enters `ctrl+d`"""

        print()
        return True

    def do_exit(self, line):
        """Exit command to quit the program"""

        return True

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        with the changes saved to storage. If there is an
        issue with the class name or provided id, the user
        is informed

        Expected
        --------
            (hbnb)  destroy BaseModel 1234-1234-1234

        Missing class name
        ------------------
            (hbnb) destroy
            ** class name missing **

        Non-Existant Class
        ------------------
            (hbnb) destroy DoesNotExist
            ** class doesn't exist **

        Missing Instance ID
        ----------
            (hbnb) destroy BaseModel
            ** instance id missing **

        Non-Existant Instance ID
        ----------
            (hbnb) destroy BaseModel 123-456-789
            ** no instance found **
        """

        parsed = self.__parse_line(line)

        if not self.__is_valid_model_name(parsed["model_name"]):
            return

        if not self.__is_valid_instance_id(parsed["instance_id"]):
            return

        key = f"{parsed.get('model_name')}.{parsed.get('instance_id')}"
        storage.all().pop(key)
        storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id. If the class name
        or id are missing, the user is informed.

        Parameter
        ---------
        line : str
            user input expected to be two part expression
            containing

            model_name : str
                name of class to create

            instance_id : str
                id of instance

        Expected
        --------
            (hbnb) show BaseModel 1234-1234-1234

        Missing class name
        ------------------
            (hbnb) show
            ** class name missing **

        Non-Existant Class
        ------------------
            (hbnb) show DoesNotExist
            ** class doesn't exist **

        Missing Instance ID
        ----------
            (hbnb) show BaseModel
            ** instance id missing **

        Non-Existant Instance ID
        ----------
            (hbnb) show BaseModel 123-456-789
            ** no instance found **
        """

        parsed = self.__parse_line(line)

        if not self.__is_valid_model_name(parsed["model_name"]):
            return

        if not self.__is_valid_instance_id(parsed["instance_id"]):
            return

        model = self.__make_model(parsed)
        print(model)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute, which is then sent
        to storage. One attribute can be updated at a time,
        whereby the attribute value is cast into one of
        three type, float, int or str.

        Of note is that `id`, `created_at` and `updated_at`
        cannot be updated.

        Usage
        -----
            update <class name> <id> <attribute name> "<attribute value>"

        Expected
        --------
            (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Missing class name
        ------------------
            (hbnb) update
            ** class name missing **

        Non-Existant Class
        ------------------
            (hbnb) update DoesNotExist
            ** class doesn't exist **

        Missing Instance ID
        ----------
            (hbnb) update BaseModel
            ** instance id missing **

        Non-Existant Instance ID
        ----------
            (hbnb) update BaseModel 123-456-789
            ** no instance found **

        Missing Attribute Name
        ----------
            (hbnb) update BaseModel 123-456-789
            ** attribute name missing **

        Non-Existant Attribute Value
        ----------
            (hbnb) update BaseModel 123-456-789 first_name
            ** value missing **
        """

        parsed = self.__parse_line(line)

        if not self.__is_valid_model_name(parsed["model_name"]):
            return

        if not self.__is_valid_instance_id(parsed["instance_id"]):
            return

        if not parsed["attribute"]:
            return print("** attribute name missing **")

        if not parsed["value"]:
            return print("** value missing **")

        model = self.__make_model(parsed)
        model.save()
        storage.new(model)
        storage.save()

    def __is_valid_model_name(self, model_name):
        """Validates class name as being existant"""

        if not model_name:
            print("** class name missing **")
            return False

        if model_name not in self.__MODELS:
            print("** class doesn't exist **")
            return False

        return True

    def __is_valid_instance_id(self, instance_id):
        """Validates instance id as being existant"""

        keys = storage.all().keys()
        elements = [element for key in keys for element in key.split(".")]

        if not instance_id:
            print("** instance id missing **")
            return False

        if instance_id not in elements:
            print("** no instance found **")
            return False

        return True

    def __make_model(self, parsed):
        """
        Instantiate an object based on provided kwargs

        Parameter
        ---------
        parsed : dict
            parsed user input

        Return
        ------
        object
            instance of available classes as per the
            kwargs
        """

        key = f"{parsed.get('model_name')}.{parsed.get('instance_id')}"
        kwargs = storage.all().get(key)

        if parsed.get("attribute"):
            attr = parsed.get("attribute")
            kwargs[attr] = parsed.get("value")

        model = self.__MODELS.get(parsed["model_name"])

        return model(**kwargs)

    def __parse_line(self, line):
        """
        Separate line into class name and instance id

        Parameter
        ---------
        line : str
            user provided input

        Return
        ------
        tuple[str]
            a paired tuple containing strings representing
            at index 0, the class name and at index 1,
            the instance id
        """

        parsed = OrderedDict({
            "model_name": None,
            "instance_id": None,
            "attribute": None,
            "value": None,
        })

        split = line.split()

        for key, value in zip(parsed, split):
            parsed[key] = value

        parsed["value"] = self.__type_value(parsed["value"])

        return parsed

    @staticmethod
    def __type_value(value):
        """
        Set the type of the value, at present limited to
        `float`, `int` and `str`

        Parameter
        ---------
        value : str
            user provided input

        Return
        ------
        float | int | str
            typed input from user
        """

        for instance in [float, int, str]:
            if isinstance(value, instance):
                return instance(value)

        return value


if __name__ == "__main__":
    HBNBCommand().cmdloop()
