#!/usr/bin/python3


"""
Test suite for the base_model module
"""


from unittest.mock import MagicMock
from unittest.mock import patch
from datetime import datetime
from unittest import TestCase
from unittest import main
import uuid


from models import BaseModel


class TestBaseModel(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.model_00 = BaseModel()
        self.model_01 = BaseModel()


class TestId(TestBaseModel):

    """Collective testing of `id` attribute"""

    def test_id_is_str(self):
        """Assert id is str type"""

        id_ = self.model_00.id
        self.assertIsInstance(id_, str)

    def test_id_is_unique(self):
        """Assert id is unique to each instance"""

        id_00 = self.model_00.id
        id_01 = self.model_01.id
        self.assertNotEqual(id_00, id_01)


class TestCreatedAt(TestBaseModel):

    """Collective testing of `created_at` attribute"""

    def test_created_at_is_datetime(self):
        """Assert `created_at` is datetime object"""

        created_at = self.model_01.created_at
        self.assertIsInstance(created_at, datetime)

    def test_created_at_is_unique(self):
        """Assert `created_at` is unique to each instance"""

        created_at_00 = self.model_00.created_at
        created_at_01 = self.model_01.created_at
        self.assertNotEqual(created_at_00, created_at_01)


class TestUpdatedAt(TestBaseModel):

    """Collective testing of `updated_at` attribute"""

    def test_updated_at_is_datetime(self):
        """Assert `updated_at` is datetime object"""

        updated_at = self.model_00.updated_at
        self.assertIsInstance(updated_at, datetime)

    def test_updated_at_altered_by_augmenting_object(self):
        """Assert change to object affects `updated_at`"""

        original_datetime = self.model_01.updated_at
        self.model_01.change = 5
        updated_datetime = self.model_01.updated_at

        self.assertNotEqual(original_datetime, updated_datetime)


class TestSaveMethod(TestBaseModel):

    """Collective testing of `save` method"""

    def test_calling_save_alters_updated_at_attr(self):
        original = self.model_00.updated_at
        self.model_00.save()
        updated = self.model_00.updated_at

        self.assertNotEqual(original, updated)


class TestMockedInit(TestCase):

    @patch("models.base_model.uuid", wraps=uuid)
    @patch("models.base_model.datetime", wraps=datetime)
    def setUp(self, mock_dt, mock_uuid):
        mock_uuid.uuid4.return_value = "unique id"

        self.init_time = datetime.now()
        mock_dt.now.return_value = self.init_time
        self.init_time_str = self.init_time.isoformat()

        self.model = BaseModel()


class TestToDict(TestMockedInit):

    """Collective testing of `to_dict` method"""

    def test_to_dict(self):
        """Assert serialisation of an unaltered instance"""

        expected = {
            "__class__": "BaseModel",
            "created_at": self.init_time_str,
            "id": "unique id",
            "updated_at": self.init_time_str,
        }

        self.assertEqual(self.model.to_dict(), expected)

    @patch("models.base_model.datetime", wraps=datetime)
    def test_to_dict_with_added_attr(self, mock_dt):
        """Assert serialisation of an altered instance"""

        now = datetime.now()
        mock_dt.now.return_value = now
        now_str = now.isoformat()

        self.model.new_attr = "new attribute"

        expected = {
            "__class__": "BaseModel",
            "created_at": self.init_time_str,
            "id": "unique id",
            "new_attr": "new attribute",
            "updated_at": now_str,
        }

        self.assertEqual(self.model.to_dict(), expected)


class TestStrProperty(TestMockedInit):

    """Collective testing of `__str__` property"""

    def test_str_property(self):
        """Assert string representation of an unaltered instance"""

        dict_ = {
            "created_at": self.init_time,
            "id": "unique id",
            "updated_at": self.init_time,
        }

        expected = f"[BaseModel] (unique id) {dict_}"
        actual = str(self.model)

        self.assertEqual(actual, expected)

    @patch("models.base_model.datetime", wraps=datetime)
    def test_str_property_with_added_attr(self, mock_dt):
        """Assert string representation of an altered instance"""

        now = datetime.now()
        mock_dt.now.return_value = now

        self.model.new_attr = "new attribute"

        dict_ = {
            "created_at": self.init_time,
            "id": "unique id",
            "new_attr": "new attribute",
            "updated_at": now,
        }

        expected = f"[BaseModel] (unique id) {dict_}"
        actual = str(self.model)

        self.assertEqual(actual, expected)


class TestKwargInstantiation(TestCase):

    """Collective testing of `__init__` property"""

    kwargs = {
        "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
        "created_at": "2017-09-28T21:03:54.052298",
        "my_number": 89,
        "updated_at": "2017-09-28T21:03:54.052302",
        "name": "My_First_Model"
    }

    def test_properties_of_newly_created_instance(self):
        """Assert spawing of an instance"""

        model = BaseModel(**self.kwargs)

        expected_created_at = datetime(2017, 9, 28, 21, 3, 54, 52298)
        expected_updated_at = datetime(2017, 9, 28, 21, 3, 54, 52302)

        self.assertEqual(model.created_at, expected_created_at)
        self.assertEqual(model.updated_at, expected_updated_at)
        self.assertEqual(model.my_number, self.kwargs.get("my_number"))
        self.assertEqual(model.name, self.kwargs.get("name"))
        self.assertEqual(model.id, self.kwargs.get("id"))


if __name__ == "__main__":
    main()
