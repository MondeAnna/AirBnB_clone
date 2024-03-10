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

    first_name = last_name = email = password = ""
