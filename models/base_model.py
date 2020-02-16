#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Class BaseModel """

    def __init__(self):
        """ initialize variables """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ return string with info on class """
        name = self.__class__.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """ func to update time """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ func to createa dictionary of of class elements """
        mydict = dict(self.__dict__)
        mydict.update({"__class__": "BaseModel"})
        created = mydict.get("created_at").strftime("%Y-%m-%dT%H:%M:%S.%f")
        mydict.update({"created_at": created})
        update = mydict.get("updated_at").strftime("%Y-%m-%dT%H:%M:%S.%f")
        mydict.update({"updated_at": update})
        return (mydict)
