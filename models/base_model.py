#!/usr/bin/python3

"""
Base Module: The definition, documentation and encapsulation of all common
attributes and methods for the project's classes
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:

    """
    The definition, documentation and encapsulation of all common
    attributes and methods for the project's classes
    """

    def __init__(self):
        self.created_at = self.updated_at = datetime.now()
        self.id = str(uuid4())

    def save(self):
        self.updated_at = datetime.now()
