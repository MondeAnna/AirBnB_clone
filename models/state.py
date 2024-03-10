#!/usr/bin/python3

"""
Stae Module: The definition, documentation and encapsulation of all common
attributes and methods for the State class
"""


from models import BaseModel


class State(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the State class
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
