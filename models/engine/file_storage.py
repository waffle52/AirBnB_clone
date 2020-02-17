#!/usr/bin/python3
""" JavaScript Object Notation """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects['obj.__class__.__name__.id'] = obj.__dict__

    def save(self):
        my_dict = {}

        for key, value in self.__objects.items():
            setattr(self, key, value)

        with open(self.__file_path, 'w+') as jfile:
            json.dumps(my_dict, jfile)

    def reload(self):
        if (self.__objects):
            with open(jfile, 'r') as file:
                json_object = json.load(file)

            for key, value in json_object.items():
                setattr(self, key, value)
