#!/usr/bin/python3


"""
Test suite for the console module
"""


from unittest import TestCase
from unittest import main
import cmd


from console import HBNBCommand


class TestUser(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.cmd = HBNBCommand()

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(HBNBCommand, cmd.Cmd))


if __name__ == "__main__":
    main()
