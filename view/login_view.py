#!/usr/bin/env python3


import getpass

from view.base_view import BaseView


class LoginView(BaseView):

    """Allows the user to input a password without showing it in the terminal."""
    @staticmethod
    def input_password(label):
        return getpass.getpass(label)

    def __init__(self):
        super().__init__()

    def show_login(self):
        login, pwd = '', ''

        # Prints header
        self.print_header('LOGIN')
        self.print_empty_lines(2)

        # Asks user for login and password and returns them
        login = input(self.fill_with('Login:', 15))
        pwd = LoginView.input_password(self.fill_with('Password:', 15))
        return login, pwd


if __name__ == '__main__':
    view = LoginView()
    view.show_login()
