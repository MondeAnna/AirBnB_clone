#!/usr/bin/python3


"""
Test suite for the city module
"""


from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main


from models import BaseModel
from models import City


class TestCity(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.city = City()

    def test_initialisation_has_empty_attr(self):
        """Provide a factory for test instances"""

        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    main()
