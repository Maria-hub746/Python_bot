from collections import UserDict


class Field:
    def __init__(self, name):
        self.value = name


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Name(Field):
    pass

class Phone(Field):
    pass

class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add(self, phone):
        self.phones.append(Phone(phone))

    def change(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add(new_phone)
                self.phones.remove(phone)
                return True

    def delete(self, delete_phone):
        for phone in self.phones:
            if phone.value == delete_phone:
                self.phones.remove(phone)
                return True