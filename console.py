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

    def do_create(self, arg):
        'Create BaseModel instance'
        if arg == "":
            print("** class name missing **")
        elif arg != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ show  """
        new_list = shlex.split(arg)
        if len(new_list) < 1:
            print("** class name missing **")
        elif len(new_list) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            word = str(new_list[0] + "." + new_list[1])
            cls = False
            ide = False
            for obj_id in all_objs.keys():
                if (new_list[0] == obj_id.split(".")[0]):
                    cls = True
                    if (new_list[1] == obj_id.split(".")[1]):
                        ide = True
                        print(all_objs[obj_id])
                        break
            if(cls is False):
                print("** class doesn't exist **")
            elif(ide is False):
                print(" ** no instance found **")

    def do_destroy(self, arg):
        """ destroy information """
        new_list = shlex.split(arg)
        if len(new_list) < 1:
            print("** class name missing **")
        elif len(new_list) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            cls = False
            ide = False
            for obj_id in all_objs.keys():
                if(new_list[0] == obj_id.split(".")[0]):
                    cls = True
                    if(new_list[1] == obj_id.split(".")[1]):
                        ide = True
                        del all_objs[obj_id]
                        break
            if(cls is False):
                print("** class doesn't exist **")
            elif(ide is False):
                print("** no instance found **")

    def do_all(self, arg):
        if arg != "":
            truth = True
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                if(arg in obj_id.split(".")):
                    if(truth is True):
                        print("[\"", end="")
                    obj = all_objs[obj_id]
                    print(obj, end="")
                    truth = False
            if(truth is True):
                print("** class doesn't exist **")
            else:
                print("\"]")
        else:
            i = 0
            all_objs = storage.all()
            print("[\"", end="")
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj, end="")
                if(i + 1 < len(all_objs.keys())):
                    print("\", \"", end="")
                i += 1
            print("\"]")

    def do_update(self, arg):
        """ Update information """
        my_list = shlex.split(arg)
        if (len(my_list) < 1):
            print ("** class name missing **")
        elif (len(my_list) < 2):
            print ("** instance id missing **")
        elif (len(my_list) < 3):
            print ("** attribute name missing **")
        elif (len(my_list) < 4):
            print ("** value missing **")
        else:
            all_objs1 = storage.all()
            word = str(my_list[0] + "." + my_list[1])
            cls = False
            ide = False
            for obj_id in all_objs1.keys():
                if (my_list[0] == obj_id.split(".")[0]):
                    cls = True
                    if (my_list[1] == obj_id.split(".")[1]):
                        ide = True
                        d = {my_list[2] : my_list[3]}
                        all_objs1[obj_id].__init__(**d)
                        break
            if (cls is False):
                print ("** class doesn't exist **")
            elif (ide is False):
                print ("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
