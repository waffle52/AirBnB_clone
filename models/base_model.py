#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """ Class BaseModel """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = str(datetime.today())
        self.updated_at = str(datetime.today())

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = str(datetime.today())

    def to_dict(self):
        mydict = dict(self.__dict__)
        mydict.update( { "__class__" : "BaseModel"})
        return (mydict)
