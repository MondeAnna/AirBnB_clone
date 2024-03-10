#!/usr/bin/python3


"""
Test suite for the user module
"""


from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main


from models import BaseModel
from models import User


class TestUser(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.user = User()

    def test_initialisation_has_empty_attr(self):
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    main()
