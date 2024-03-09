#!/usr/bin/python3

"""
Command Line Interface for the product
"""

import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
