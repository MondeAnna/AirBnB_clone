#!/usr/bin/python3

"""
Test suite for the base_model module
"""

from datetime import datetime
from unittest import TestCase
from unittest import main


from models import BaseModel


class TestBaseModel(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.model_00 = BaseModel()
        self.model_01 = BaseModel()


class TestBaseModelId(TestBaseModel):

    """Collective testing of `id` attribute"""

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


class TestBaseModelCreatedAt(TestBaseModel):

    """Collective testing of `created_at` attribute"""

    def test_created_at_is_datetime(self):
        """Assert `created_at` is datetime object"""

        is_datetime = isinstance(self.model_01.created_at, datetime)
        self.assertTrue(is_datetime)

    def test_created_at_is_unique(self):
        """Assert `created_at` is unique to each instance"""

        created_at_00 = self.model_00.created_at
        created_at_01 = self.model_01.created_at
        self.assertNotEqual(created_at_00, created_at_01)

    def test_created_at_is_quasi_immutable(self):
        """Assert `created_at` unchangeable after instantiation"""

        with self.assertRaises(AttributeError) as error:
            self.model_00.created_at = datetime.now()

        expected = "property 'created_at' of 'BaseModel' object has no setter"
        exception = str(error.exception)

        self.assertEqual(exception, expected)


if __name__ == "__main__":
    main()
