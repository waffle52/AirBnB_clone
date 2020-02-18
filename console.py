#!/usr/bin/python3
import cmd, sys

class HBNBCommand(cmd.Cmd):
    intro = "hello"
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        'Send end of file to quit program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
