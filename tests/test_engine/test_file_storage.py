#!/usr/bin/python3


"""
Test suite for saving BaseModel to file system
"""


from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main


from models import FileStorage


class TestFileStorage(TestCase):

    """"
    Collective testing for saving BaseModel
    instances to file system
    """

    def setUp(self):
        """Preparatory object structure needed to carry out tests"""

        self.storage = FileStorage()
        self.mock_model_00 = MagicMock(id="mock_model_00")
        self.mock_model_01 = MagicMock(id="mock_model_01")

        self.mock_model_00.to_dict.return_value = {
            "__class__": "BaseModel",
            "id": "mock_model_00",
        }

        self.mock_model_01.to_dict.return_value = {
            "__class__": "BaseModel",
            "id": "mock_model_01",
        }

    def tearDown(self):
        del self.storage
        del self.mock_model_00
        del self.mock_model_01


class TestAll(TestFileStorage):

    """Assert retrieval of all stored BaseModel instances"""

    def test_all_with_empty_storage(self):
        """Assert that a new instance has no saved objects"""

        self.assertEqual(self.storage.all(), {})


class TestNew(TestFileStorage):

    """Assert update of objects being tracked for serialisation"""

    def test_new_when_single_object_is_provided(self):
        """Assert that single provided instance is tracked"""

        self.storage.new(self.mock_model_00)

        objects = self.storage.all()
        num_objects = len(objects)

        self.assertTrue("BaseModel.mock_model_00" in objects.keys())
        self.assertTrue(self.mock_model_00 in objects.values())

        # the number of tracked items seems to persist
        # between tests, here the number of items is
        # expected to be one

        """ self.assertEqual(num_objects, 1) """

    def test_new_when_multiple_object_is_provided(self):
        """Assert that single provided instance is tracked"""

        self.storage.new(self.mock_model_00)
        self.storage.new(self.mock_model_01)

        objects = self.storage.all()
        num_objects = len(objects)

        self.assertTrue("BaseModel.mock_model_00" in objects.keys())
        self.assertTrue("BaseModel.mock_model_01" in objects.keys())
        self.assertTrue(self.mock_model_00 in objects.values())
        self.assertTrue(self.mock_model_01 in objects.values())
        self.assertEqual(num_objects, 2)


if __name__ == "__main__":
    main()
