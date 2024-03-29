#!/usr/bin/python3

"""
Review Module: The definition, documentation and encapsulation of all common
attributes and methods for the Review class
"""


from models import BaseModel


class Review(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the Review class
    """

    def __init__(self, *args, **kwargs):
        """instantiate public class attributes as empty str"""

        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
