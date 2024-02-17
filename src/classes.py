from collections import UserDict
from datetime import datetime, date


class Record:
    def __init__(self, name, birthday=None, address=None, email=None):
        self.name = Name(name)
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
                return f'Today is your birthday! Congratulations!'
            elif delta > 0:
                return f'{delta} days left until your birthday'
            else:
                user_date = self.birthday.value.replace(year=current_year + 1)
                delta = user_date.toordinal() - current_date.toordinal()
                return f'{delta} days left until your birthday'

    def add_birthday(self, birthday):
        if self.birthday is None:
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
            if number in record.days_to_birthday:
                birthday_people.append(record.name.value)
        return birthday_people

