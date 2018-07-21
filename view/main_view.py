#!/usr/bin/env python3


from model.account import Account
from model.person import Person
from view.base_view import BaseView


class MainView(BaseView):

    def __init__(self):
        super().__init__()

    def show_main_menu(self, profile):
        choice = -1

        self.clear()
        if isinstance(profile, Person):
            self.show_manager_menu(profile)
        elif isinstance(profile, Account):
            self.show_client_menu(profile)
        elif profile in ['admin', 'ADMIN']:
            self.show_admin_menu()
        else:
            raise Exception('Invalid user profile "{0}"'.format(profile))

        try:
            self.print_empty_lines(2)
            choice = int(input('Your option:    '))
        except Exception:
            choice = -1

        return choice

    def show_admin_menu(self):
        pattern = self.get_line_pattern(BaseView.ALIGN_LEFT)
        # Prints header
        self.print_header('WELCOME, ADMIN')
        print(pattern.format('Profile: ADMIN'))

        # Prints menu options
        self.print_empty_header_line()
        print(pattern.format('Choose an option:'))
        self.print_line_divider()
        print(pattern.format('100 - Create Branch'))
        print(pattern.format('101 - View Branch List'))
        print(pattern.format('102 - Create Manager'))
        print(pattern.format('103 - View Manager List'))
        print(pattern.format('  0 - Exit'))
        self.print_empty_header_line()
        self.print_border_line()

    def show_manager_menu(self, manager):
        pattern = self.get_line_pattern(BaseView.ALIGN_LEFT)
        # Prints header
        self.print_header('WELCOME, {0}'.format(manager.name))
        print(pattern.format('Profile: MANAGER'))

        # Prints menu options
        self.print_empty_header_line()
        print(pattern.format('Choose an option:'))
        self.print_line_divider()
        print(pattern.format('200 - Create Account'))
        print(pattern.format('201 - View Account List'))
        print(pattern.format('  0 - Exit'))
        self.print_empty_header_line()
        self.print_border_line()

    def show_client_menu(self, account):
        pattern = self.get_line_pattern(BaseView.ALIGN_LEFT)
        # Prints header
        branch_info = self.fill_with('Branch:', 18)
        branch_info = '{0}{1:08d}'.format(branch_info, account.branch_id)
        account_info = self.fill_with('Account Number:', 18)
        account_info = '{0}{1:08d}'.format(account_info, account.number)
        self.print_header('WELCOME, {0}'.format(account.client.name),
                          "YOUR'RE CONNECTED TO:",
                          branch_info,
						  account_info)

        # Prints menu options
        self.print_empty_header_line()
        print(pattern.format('Choose an option:'))
        self.print_line_divider()
        print(pattern.format('1 - Deposit'))
        print(pattern.format('2 - Withdrawal'))
        print(pattern.format('3 - Account Balance'))
        print(pattern.format('4 - Transaction History'))
        print(pattern.format('0 - Exit'))
        self.print_empty_header_line()
        self.print_border_line()
