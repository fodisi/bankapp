#!/usr/bin/env python3


from dal.personDAL import PersonDAL
from model.manager import Manager
from model.client import Client
from view.person_view import PersonView


class PersonController():
    def __init__(self):
        self.view = PersonView()

    def __to_object(self, data, role):
        name = data[0]
        email = data[1]
        login = data[2]
        pwd = data[3]

        if role == 'Manager':
            return Manager(name=name, email=email, login=login, password=pwd)
        if role == 'Client':
            return Client(name=name, email=email, login=login, password=pwd)
        raise Exception('Invalid person role "{0}".'.format(role))

    def create_person(self, role):
        try:
            data = self.view.create_person(role)
            person = self.__to_object(data, role)
            dal = PersonDAL()
            dal.insert(person)

            message = '{0} "{1}" inserted successfully.'.format(
                role, person.name)
            self.view.show_message('Success', message, True)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)

    def list_people(self, role):
        try:
            dal = PersonDAL()
            person_role = ''
            if role == 'Manager':
                person_role = 'M'
            elif role == 'Client':
                person_role = 'C'
            else:
                raise Exception('Invalid person role "{0}".'.format(role))

            people = dal.select_by_role(person_role)
            self.view.show_people(people, role)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)
