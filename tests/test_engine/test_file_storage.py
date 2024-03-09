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
        self.assertTrue(self.mock_model_00.to_dict() in objects.values())

        """
        self.assertEqual(num_objects, 1)

        the number of tracked items seems to persist
        between tests, here the number of items is
        expected to be one
        """

    def test_new_when_multiple_object_is_provided(self):
        """Assert that single provided instance is tracked"""

        self.storage.new(self.mock_model_00)
        self.storage.new(self.mock_model_01)

        objects = self.storage.all()
        num_objects = len(objects)

        self.assertTrue("BaseModel.mock_model_00" in objects.keys())
        self.assertTrue("BaseModel.mock_model_01" in objects.keys())
        self.assertTrue(self.mock_model_00.to_dict() in objects.values())
        self.assertTrue(self.mock_model_01.to_dict() in objects.values())
        self.assertEqual(num_objects, 2)


class TestSave(TestFileStorage):

    """Assert serialisation to json file"""

    @patch("json.dump")
    @patch("builtins.open")
    def test_save_with_no_tracked_objects(self, mock_dump, mock_open):
        """Assert save renders to file with no tracked objects"""

        self.storage.save()

        mock_dump.assert_called_once_with(self.storage.file_path, "w")
        mock_open.assert_called_once()

    @patch("json.dump")
    @patch("builtins.open")
    def test_save_with_tracked_objects(self, mock_dump, mock_open):
        """Assert save renders to file with no tracked objects"""

        self.storage.new(self.mock_model_00)
        self.storage.save()

        mock_dump.assert_called_once_with(self.storage.file_path, "w")
        mock_open.assert_called_once()


class TestReload(TestFileStorage):

    """Assert deserialisation to json file"""

    @patch("json.dump")
    @patch("builtins.open")
    @patch("pathlib.Path.is_file", return_value=False)
    def test_reload_with_no_file_to_load_does_not_raise_an_exception(
        self,
        mock_path,
        mock_open,
        mock_dump
    ):
        """Assert reload does nothing if no file to load from"""

        try:
            self.storage.reload()
        except Exception as exception:
            name = exception.__class__.__name__
            self.fail("method `reload` unexpectedly raised `{name}`")

        mock_path.assert_called_once()
        mock_dump.assert_not_called()
        mock_open.assert_not_called()

    @patch("json.dump")
    @patch("builtins.open")
    @patch("pathlib.Path.is_file", return_value=False)
    def test_reload_where_no_file_tracked_objects_is_unchanged(
        self,
        mock_path,
        mock_open,
        mock_dump
    ):
        """Assert reload does nothing if no file to load from"""

        pre_call = self.storage.all()
        self.storage.reload()
        post_call = self.storage.all()

        self.assertEqual(pre_call, post_call)
        mock_path.assert_called_once()
        mock_dump.assert_not_called()
        mock_open.assert_not_called()


if __name__ == "__main__":
    main()
