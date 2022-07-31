# contactBook.py
'''
Creats dictionary {name: objects}, pickle dictionary and unpickle dictionary when
new objects are created, changed or deleted.
'''
import pickle  # zmień ściekę, skopiuj plik dat do init folder
import contact  # previous created module with the class

# Globals
FILE = '/Users/xxx/Python projects/Python Projects/Intro_to_python_for_computer_since/10_Object_orientated_programming/Contactscontact.dat'

# Globals for menu
FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
CONTACTS = 5
QUIT = 6


def main():
    myContacts = loadContacts()  # returns dict {name: object}

    # intializing while loop
    choice = 0
    while choice != QUIT:
        choice = menu()  # returns choice nr

        # using if elif statement, which enables to choose only one option
        # repeated if statement enables to choose as many options as comply with the conditions
        if choice == FIND:
            # passinf myContacts loaded from the file or empty ductionary if the file doesn't exist
            find(myContacts)
            print()
        elif choice == ADD:
            add(myContacts)
            print()
        elif choice == CHANGE:
            change(myContacts)
            print()
        elif choice == DELETE:
            deletee(myContacts)
            print()
        elif choice == CONTACTS:
            listAll(myContacts)
            print()


def loadContacts():

    try:
        inputFile = open(FILE, 'rb')
        dictionary = pickle.load(inputFile)  # load dictionary if exists
    except IOError:  # if file doesn't exist
        dictionary = {}

    return dictionary


def menu():
    print()
    print('Choose the option')
    print('1.Find conctact.')
    print('2.Add contact.')
    print('3.Change contact.')
    print('4.Delete contact.')
    print('5.List all contacts')
    print('6.Exit.')
    print()

    # ensuring that choice is integer in the right range
    flag = True
    while flag:
        try:
            print()
            choice = int(input('Enter the your choice: '))

            while choice < FIND or choice > QUIT:
                print()
                choice = int(input('Enter2 correct nr: '))

            flag = False
        except ValueError:
            pass

    return choice


def find(myContacts):
    print()
    name = input('Enter searching name: ')

    try:
        if name in myContacts:
            print()
            print(myContacts[name])  # print status of the object __str__()
        else:
            print()
            print('Name was not found in data base.')
    except UnboundLocalError:
        pass


def add(myContacts):
    print()
    name = input('Enter the name: ')

    if name in myContacts:
        print('Name already exists!')
    else:
        phone = int(input('Enter phone nr: '))
        email = input('Enter email: ')
        print()

        # creating the object
        data = contact.Contact(name, phone, email)

        # adding data object to the dictionary
        myContacts[name] = data

        # saving dictionary
        save(myContacts)


def change(myContacts):
    print()
    name = input('Enter the name to be changed: ')

    if name in myContacts:  # name by defaylt is key value in dictionary
        flag = True

        while flag:
            try:
                phone = int(input('Enter phone nr: '))
                flag = False
            except ValueError:
                pass
        email = input('Enter new email address: ')

        data = contact.Contact(name, phone, email)

        # passing object to dictionary to update old data
        myContacts[name] = data

    else:
        print("Name doesn't exist in data base!")
        print()


def deletee(myContacts):
    print()
    name = input('Enter the name to be deleted from data base: ')

    if name in myContacts:  # if key in dictionary
        del myContacts[name]
        print('Person was deleted!')
    else:
        print("Name doesn't exist in data base.")


def listAll(myContacts):
    # I must loop through dictionary and display __str__method of each object
    for name in myContacts.values():  # each vakue is the object
        print(name)  # print status of the object


def save(myContacts):
    outputFile = open(FILE, 'wb')

    # pickle the file
    pickle.dump(myContacts, outputFile)


main()


'''
output:
(base) xxx air-2 Python Projects % python -u "/Users/xxx/Python projects/Python Projects/Intro_to_python_for_computer_since/10_Object_orientated_programming/Contacts/contactBook.py"

Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 5

From str method...
Name and Surname: Kik Klop
Phone number: 334422
Email: kk@wp.pl


From str method...
Name and Surname: Jack Man
Phone number: 2211
Email: aaw@ww.pl


From str method...
Name and Surname: Gorge Kik
Phone number: 2234
Email: de@www.com



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 1

Enter searching name: Kik Kop

Name was not found in data base.


Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 1

Enter searching name: Kik Klop


From str method...
Name and Surname: Kik Klop
Phone number: 334422
Email: kk@wp.pl



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 1

Enter searching name: Gorge Kik


From str method...
Name and Surname: Gorge Kik
Phone number: 2234
Email: de@www.com



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 3

Enter the name to be changed: ss dd
Name doesn't exist in data base!



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 3

Enter the name to be changed: Gorge Kit
Name doesn't exist in data base!



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 3

Enter the name to be changed: Gorge Kik
Enter phone nr: 343434
Enter new email address: gorge@pl.com


Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 5

From str method...
Name and Surname: Kik Klop
Phone number: 334422
Email: kk@wp.pl


From str method...
Name and Surname: Jack Man
Phone number: 2211
Email: aaw@ww.pl


From str method...
Name and Surname: Gorge Kik
Phone number: 343434
Email: gorge@pl.com



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 2

Enter the name: Gorge Kik
Name already exists!


Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 2

Enter the name: To Delete
Enter phone nr: 234455
Enter email: delete@del.com



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 5

From str method...
Name and Surname: Kik Klop
Phone number: 334422
Email: kk@wp.pl


From str method...
Name and Surname: Jack Man
Phone number: 2211
Email: aaw@ww.pl


From str method...
Name and Surname: Gorge Kik
Phone number: 343434
Email: gorge@pl.com


From str method...
Name and Surname: To Delete
Phone number: 234455
Email: delete@del.com



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 4

Enter the name to be deleted from data base: dde
Name doesn't exist in data base.


Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 4

Enter the name to be deleted from data base: To Delete
Person was deleted!


Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 5

From str method...
Name and Surname: Kik Klop
Phone number: 334422
Email: kk@wp.pl


From str method...
Name and Surname: Jack Man
Phone number: 2211
Email: aaw@ww.pl


From str method...
Name and Surname: Gorge Kik
Phone number: 343434
Email: gorge@pl.com



Choose the option
1.Find conctact.
2.Add contact.
3.Change contact.
4.Delete contact.
5.List all contacts
6.Exit.


Enter the your choice: 
'''
