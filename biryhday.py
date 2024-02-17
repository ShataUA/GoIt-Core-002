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


class AddressBook(UserDict):

    def add_record(self, record: Record):
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

