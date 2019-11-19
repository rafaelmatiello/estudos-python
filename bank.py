class Account(object):

    def __init__(self, number):
        self.__number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value


    def get_total(self):
        return self.__total


class Bank1Account(object):

    def __init__(self, number):
        self.__number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value
        self.__total -= 1


    def get_total(self):
        return self.__total


class Bank2Account(object):

    def __init__(self, number):
        self.__number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value
        self.__total -= 2

    def get_total(self):
        total = self.__total
        return total


class Bank3Account(Bank1Account):

    def __init__(self, number, cvv):
        super(Bank3Account, self).__init__( number)
        self.__cvv = cvv


    def withdraw(self, value):
        self._Bank1Account__total -= value
        self._Bank1Account__total -= 2


