from collections import UserDict
from datetime import datetime, date
import pickle
import re


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @staticmethod
    def is_valid(value):
        if value:
            return True

    @value.setter
    def value(self, value):
        self.__value = value if self.is_valid(value) else None
        if not self.is_valid(value):
            raise ValueError

    def __str__(self):
        return str(self.value)


class FirstName(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if value.isalpha():
            return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value if self.is_valid(value) else None
        if not self.is_valid(value):
            raise ValueError


class SecondName(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if value is None or value.isalpha():
            return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value if (self.is_valid(value) and value is not None) else None
        if not self.is_valid(value):
            raise ValueError


class Address(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if value.isdigit() and len(value) == 10:
            return True


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if value is None or datetime.strptime(value, '%d-%m-%Y').date():
            return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = datetime.strptime(value, '%d-%m-%Y').date() if (self.is_valid(value) and value is not None) else None
        if not self.is_valid(value):
            raise ValueError
        

class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if value is None or re.match(r"\b[A-Za-z]{1,}[A-Za-z0-9._]{1,}@[A-Za-z0-9]+\.[A-Za-z]{2,}\b|[A-Za-z]{1,}[A-Za-z0-9._]{1,}@[A-Za-z0-9]+\.[A-Za-z]{2,}\b", value):
            return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value if (self.is_valid(value) and value is not None) else None
        if not self.is_valid(value):
            raise ValueError
        

class Record:
    def __init__(self, name, birthday=None, address=None, email=None):
        self.name = FirstName(name)
        self.phones = []
        self.birthday = Birthday(birthday)
        self.email = Email(email)
        self.address = Address(address)

    @property
    def days_to_birthday(self):
        if self.birthday is None:
            raise AttributeError
        else:
            current_date = date.today()
            current_year = current_date.year
            user_date = self.birthday.value.replace(year=current_year)
            delta = user_date.toordinal() - current_date.toordinal()
            if delta == 0:
                return 0
            elif delta > 0:
                return delta
            else:
                user_date = self.birthday.value.replace(year=current_year + 1)
                delta = user_date.toordinal() - current_date.toordinal()
                return delta

    def add_birthday(self, birthday):
        if self.birthday.value is None:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError



    def add_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                raise ValueError
        else:
            new_phone = Phone(number)
            self.phones.append(new_phone)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                new_phone = Phone(new_number)
                target_index = self.phones.index(phone)
                self.phones[target_index] = new_phone
                return new_phone
        else:
            raise ValueError

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        else:
            return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)},"
                f" birthday: {self.birthday.value}")


class AddressBook(UserDict):

    def add_contact(self, record: Record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            raise ValueError

    def birthday_in_a_given_number_of_days(self, number):
        birthday_people = []
        for record in self.data.values():
            if number == record.days_to_birthday:
                birthday_people.append(record.name.value)
        return birthday_people

    def find_info(self, info: str):
        # find users whose name or phone number matches the entered info
        request = []
        if info.isalpha():  # if only letters in info, find usernames
            for key, value in self.data.items():
                if info in key:
                    request.append(f"Contact name: {value.name}, phones: {'; '.join(p.value for p in value.phones)},"
                                   f" birthday: {value.birthday.value}")
        elif info.isdigit():  # if only digits in info, find in phone numbers
            for key, value in self.data.items():
                for phone in value.phones:
                    if info in phone.value and key not in request:
                        request.append(
                            f"Contact name: {value.name}, phones: {'; '.join(p.value for p in value.phones)},"
                            f" birthday: {value.birthday.value}")
        return request

    def find(self, username):
        if username not in self.data:
            return None
        else:
            return self.data[username]

    def delete(self, username):
        if username in self.data:
            del self.data[username]

    def iterator(self, n):
        page = []

        for value in self.data.values():
            page.append(f'{value}')
            if len(page) == n:
                yield page
                page = []
        yield page

    def save_to_file(self, filename):
        with open(filename, 'wb') as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filename):
        with open(filename, 'rb') as fh:
            return pickle.load(fh)

