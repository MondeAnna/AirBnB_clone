#!/usr/bin/python3

"""
City Module: The definition, documentation and encapsulation of all common
attributes and methods for the City class
"""


from models import BaseModel


class City(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the City class
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
        self.state_id = ""
