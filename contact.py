# contact.py
'''
Due to this class, created objects will be saved inserted in dictionary and pickled to the file.dat
'''


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # creating setters
    def set_name(self, name):
        self.name = name

    def set_phne(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    # creating getters
    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    # return state of the object's attributes in string format 
    def __str__(self):
        return '\nFrom str method...\n' +\
                'Name and Surname: ' + self.name + \
                '\nPhone number: ' + str(self.phone) + \
                '\nEmail: ' + self.email +\
                '\n'
