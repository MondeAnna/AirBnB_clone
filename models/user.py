#!/usr/bin/python3

"""
User Module: The definition, documentation and encapsulation of all common
attributes and methods for the User class
"""


from models import BaseModel


class User(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the User class
    """

    def __init__(self, *args, **kwargs):
        """instantiate public class attributes as empty str"""

        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""

        super().__init__(*args, **kwargs)
