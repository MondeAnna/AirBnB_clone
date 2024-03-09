#!/usr/bin/python3

"""
Command Line Interface for the product
"""

import cmd


from models import BaseModel


class HBNBCommand(cmd.Cmd):

    """
    Product's Command Line Interface
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Skips to new prompt should input be empty"""

        pass

    def do_EOF(self, line):
        """Exits the programme when user enters `ctrl+d`"""

        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

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
            ** class does'nt exist **
        """

        available_models = ["BaseModel"]

        if not class_name:
            return print("** class name missing **")

        if class_name not in available_models:
            return print("** class doesn't exist **")

        model = BaseModel()
        model.save()
        print(model.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
