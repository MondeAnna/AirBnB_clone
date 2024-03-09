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
        the class name is missing or does not exist, the user
        is informed

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

        class_name, instance_id = self.__split_line(line)

        if not self.__is_valid_class_name(class_name):
            return

        if not self.__is_valid_instance_id(instance_id):
            return

        key = f"{class_name}.{instance_id}"
        storage.all().pop(key)
        storage.save()

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

        class_name, instance_id = self.__split_line(line)

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

    @staticmethod
    def __split_line(line):
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

        if line.count(" "):
            class_name, instance_id, *_ = line.split()
        else:
            class_name = line
            instance_id = ""
        return class_name, instance_id


if __name__ == "__main__":
    HBNBCommand().cmdloop()
