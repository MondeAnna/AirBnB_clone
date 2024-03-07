#!/usr/bin/python3

"""
Test suite for the base_model module
"""

from unittest import TestCase
from unittest import main


from models import BaseModel


class TestBaseModelId(TestCase):
    """Collective testing of attributes related to base model"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.model_00 = BaseModel()
        self.model_01 = BaseModel()

    def test_id_is_str(self):
        """Assert id is str type"""

        is_str = isinstance(self.model_00.id, str)
        self.assertTrue(is_str)

    def test_id_is_unique(self):
        """Assert id is unique to each instance"""

        id_00 = self.model_00.id
        id_01 = self.model_01.id
        self.assertNotEqual(id_00, id_01)

    def test_id_is_quasiimmutable(self):
        """Assert id cannot be unchangeable after instantiation"""

        with self.assertRaises(AttributeError) as error:
            self.model_01.id = "new id"

        expected = "property 'id' of 'BaseModel' object has no setter"
        exception = str(error.exception)

        self.assertEqual(exception, expected)


if __name__ == "__main__":
    main()
