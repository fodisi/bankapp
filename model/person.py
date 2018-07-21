#!/usr/bin/env python3

"""Represents a Person"""


class Person():
    def __init__(self, name='', email='', role='', login='', password='', id_=0):
        self.id = id_
        self.name = name
        self.email = email
        self.role = role
        self.login = login
        self.password = password
