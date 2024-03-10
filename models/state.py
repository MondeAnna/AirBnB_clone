#!/usr/bin/python3

"""
State Module: The definition, documentation and encapsulation of all common
attributes and methods for the State class
"""


from models import BaseModel


class State(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the State class
    """

    def __init__(self, *args, **kwargs):
        """instantiate public class attributes as empty str"""

        self.name = ""
        super().__init__(*args, **kwargs)
