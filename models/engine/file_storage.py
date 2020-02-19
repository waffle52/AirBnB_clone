#!/usr/bin/python3
""" JavaScript Object Notation """
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all function """
        return self.__objects

    def new(self, obj):
        """ to print the new function keys """
        get_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[get_key] = obj

    def save(self):
        """ save the information to the json file """
        my_dict = {}

        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as jfile:
            json.dump(my_dict, jfile)

    def reload(self):
        """ reload the information from the json """
        if (os.path.isfile(self.__file_path)):
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)
