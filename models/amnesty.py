#!/usr/bin/python3

"""
Amnesty Module: The definition, documentation and encapsulation of all common
attributes and methods for the Amnesty class
"""


from models import BaseModel


class Amnesty(BaseModel):

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the Amnesty class
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
