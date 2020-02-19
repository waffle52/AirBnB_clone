#!/usr/bin/python3
""" Console file """
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """ Command class """
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        'Send end of file to quit program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        raise SystemExit

    def emptyline(self):
        pass

    """def do_create(self, arg):
        'Create BaseModel instance'
        if arg == "":
            print("** class name missing **")
        elif arg != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            print(my_model.id)
            my_model.save()"""

    """def do_show(self, arg):
        new_list = shlex.split(arg)
        all_objs = storage.all()
        if new_list[0] == "":
            print ("** class name missing **")
        elif new_list[1] == "":
            print ("** instance id missing **")
        elif id != "":
            print ("** no instance found **")
        elif id != "":
            print ("** class doesn't exist **")
        else:
            all_objs = storage.all()
            word = arg + id
            obj_id = all_objs[word]
            print ("test: {}".format(obj_id))"""

    """def do_destroy(self, arg):
        #num = dict(arg.split(" "))
        #arg = arg.split(" ")[0]
        print("test: {}".format(num))
        if arg == "" or arg is None:
            print ("** class name missing **")
        elif num == "":
            print ("** instance id missing **")
        all_objs = storage.all()
        cls = False
        ide = False
        for obj_id in all_objs.keys():
            if (arg == obj_id.split(".")):
                cls = True
                if (num == obj_id.split(".")[1]):
                    ide = True
                    del all_objs[obj_id]
                    my_model.save()
        if (cls == False):
            print ("** class doesn't exist **")
        elif (ide == False):
            print ("** no instance found **")
        """

    """def do_all(self, arg):
        if arg != "":
            truth = True
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                if (arg in obj_id.split(".")):
                    if (truth is True):
                        print("[\"", end="")
                    obj = all_objs[obj_id]
                    print(obj, end="")
                    truth = False
            if (truth is True):
                print("** class doesn't exist **")
            else:
                print("\"]")
        else:
            all_objs = storage.all()
            print("[\"", end="")
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj, end="")
            print("\"]")"""

    """def do_update(self, arg):
       """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
