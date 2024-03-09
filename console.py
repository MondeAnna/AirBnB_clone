#!/usr/bin/python3

"""
Command Line Interface for the product
"""

import cmd


from models import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """
    Product's Command Line Interface
    """

    __valid_models = ["BaseModel"]
    prompt = "(hbnb) "

    def emptyline(self):
        """Skips to new prompt should input be empty"""

        pass

    def do_create(self, class_name):
        """
        Creates a new instance, saves it and prints the id. If
        the class name is missing, informs the user and if the
        class name does not exist, informs the user.

        Parameter
        ---------
        class_name : str
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

        if not self.__is_valid_class_name(class_name):
            return

        model = BaseModel()
        model.save()
        print(model.id)

    def do_EOF(self, line):
        """Exits the programme when user enters `ctrl+d`"""

        print()
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

            class_name : str
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

        if line.count(" "):
            class_name, instance_id, *_ = line.split()
        else:
            class_name = line
            instance_id = ""

        if not self.__is_valid_class_name(class_name):
            return

        if not self.__is_valid_instance_id(instance_id):
            return

        key = f"{class_name}.{instance_id}"
        model = storage.all().get(key)
        print(model)

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def __is_valid_class_name(self, class_name):
        """Validates class name as being existant"""

        if not class_name:
            print("** class name missing **")
            return False

        if class_name not in self.__valid_models:
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
