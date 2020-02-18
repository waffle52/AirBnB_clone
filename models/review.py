#!/usr/bin/python3
""" Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class with the BaseModel inherits """
    place_id = ""
    user_id = ""
    text = ""
