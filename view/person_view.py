#!/usr/bin/env python3


from model.person import Person
from view.login_view import LoginView
from view.base_view import BaseView


class PersonView(BaseView):

    def __init__(self):
        super().__init__()

    def create_person(self, role):
        data = []
        self.print_header('CREATE NEW {0}:'.format(role.upper()))

        # Asks for personal info.
        self.print_empty_lines(2)
        data.append(input(self.fill_with('Name:', 15)))
        data.append(input(self.fill_with('Email:', 15)))
        data.append(input(self.fill_with('Login:', 15)))
        pwd = LoginView.input_password(self.fill_with('Password:', 15))
        data.append(pwd)
        return data

    def show_people(self, people, role):
        self.print_header('{0} LIST:'.format(role.upper()))

        # Prints column header
        header_pattern = '# {0:<7} | {1:<25} | {2:<25} | {3:<10} #'
        print(header_pattern.format('Id', 'Name', 'Email', 'Login'))
        # Prints column values
        self.print_line_divider()
        pattern = '# {0:07d} | {1:<25} | {2:<25} | {3:<10} #'
        for person in people:
            print(pattern.format(person.id, person.name, person.email, person.login))

        self.print_empty_header_line()
        self.print_border_line()
        self.wait_for_user()


if __name__ == '__main__':
    view = PersonView()
    view.create_person('Manager')
