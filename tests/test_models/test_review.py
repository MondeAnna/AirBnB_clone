#!/usr/bin/python3


"""
Test suite for the review module
"""


from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main


from models import BaseModel
from models import Review


class TestReview(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.review = Review()

    def test_initialisation_has_empty_attr(self):
        """Provide a factory for test instances"""

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    main()
