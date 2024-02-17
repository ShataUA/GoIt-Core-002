from datetime import datetime
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
        if self.is_valid(value):
            self.__value = value
        else:
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
        if self.is_valid(value):
                self.__value = value
        else:
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
        if self.is_valid(value):
            if value is not None:
                self.__value = value
            else:
                self.__value = None
        else:
            raise ValueError

class Address(Field):
    def __init__(self, value):
        super().__init__(value)


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
        if self.is_valid(value):
            if value is not None:
                self.__value = datetime.strptime(value, '%d-%m-%Y').date()
            else:
                self.__value = None
        else:
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
        if self.is_valid(value):
            if value is not None:
                self.__value = value
            else:
                self.__value = None
        else:
            raise ValueError
        
