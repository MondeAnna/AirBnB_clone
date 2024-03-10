#!/usr/bin/python3

"""
Amenity Module: The definition, documentation and encapsulation of all common
attributes and methods for the Amenity class
"""


from models import BaseModel


class Amenity(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """instantiate public class attributes as empty str"""

        self.name = ""
        super().__init__(*args, **kwargs)
