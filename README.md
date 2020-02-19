# AirBnb_clone

## Description of project
This project consisits of a console that can create, show, update and delete data that is saved in a JSON file. This allows an easy way to manage data especially with functions that are used over and over to handle the data and convert it. 
## Description of the command interpreter
The command interpreter called console allows us to easily manage JSON data and use it in python to re-use the same structure to hold different data on mutiple property listings that are rentable. The console allows us to eeasily interact and control that data without directly touching it nor formatting it. The console can be lauched like any executable via ./console.py and from there a prompt will be issued waiting for input, the command interpreter can take any of the following available commands: 
| Available commands |
| --- |
|quit - quit out of the interpreter|
|help - see list of commands and what they do with an option|
|create create a new instance of BaseModel|
|show -  Prints the string representation of an instance|
|destroy - Deletes an instance based on the class name and id|
|all - Prints all string representation of all instances based or not on the class name|
|update - Updates an instance based on the class name and id by adding or updating attribute|

## Files
console.py - Console application to handle JSON data.
models/ - Directory of models used for data
tests/ - Directory containing unit tests

## Examples
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit

(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) quit
$

## AUTHORS
Kenneth Fernandez
Kyle Campbell
