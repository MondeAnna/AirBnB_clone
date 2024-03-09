#!/usr/bin/python3


"""
Test suite for saving BaseModel to file system
"""


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
        self.storage_empty = FileStorage()


class TestAll(TestFileStorage):

    """Assert retrieval of all stored BaseModel instances"""

    def test_all_with_empty_storage(self):
        """Assert that a new instance has no saved objects"""

        self.assertEqual(self.storage_empty.all(), {})


if __name__ == "__main__":
    main()
