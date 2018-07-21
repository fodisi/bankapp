#!/usr/bin/env python3


from model.person import Person


"""Represents a bank account Manager"""


class Manager(Person):
    def __init__(self, name='', email='', login='', password='', id_=0):
        super().__init__(name=name,
                         email=email,
                         role='M',
                         login=login,
                         password=password,
                         id_=id_
                         )
        #self.managed_accounts = {}
