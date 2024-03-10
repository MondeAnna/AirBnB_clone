#!/usr/bin/python3


"""
Test suite for the place module
"""


from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main


from models import BaseModel
from models import Place


class TestPlace(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.place = Place()

    def test_initialisation_has_empty_attr(self):
        """Provide a factory for test instances"""

        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")

        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)

        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.latitude, 0.0)

        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    main()
