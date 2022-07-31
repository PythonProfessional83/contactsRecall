Program creates dictionary with names and objects, which set and returns data as name, phone, email.
Dictionary is serialized/ pickled with the functions add, change, delete.
Dictionary is deserialized/ unpickled with the function load contacts.
Program consists of the modules:
1. Contact.py, which contains the class contact.
2. contactBook.py, which creats dictionary {name: objects}, pickle dictionary and unpickle dictionary when
   new objects are created, changed or deleted.

UML diagram:
--------------
contact.py
------------------
attributes:
.name, .phone, .email
------------------------------
methods:
__init__(name, phone, email)
set_name(name)
set_phone(phone)
set_email(email)
get_name(name)
get_phone(phone)
get_email(email)
__str__()