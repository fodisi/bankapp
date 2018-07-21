#!/usr/bin/env python3


from datetime import datetime
import random

from model.account import Account
from model.client import Client
from model.transaction import Transaction
from view.base_view import BaseView
from view.login_view import LoginView


class AccountView(BaseView):

    def __init__(self):
        super().__init__()

    def __print_statements_header(self, title, account):
        # Configures info to be shown in header
        branch_info = self.fill_with('Branch:', 18)
        branch_info = '{0}{1:08d}'.format(branch_info, account.branch_id)
        account_info = self.fill_with('Account Number:', 18)
        account_info = '{0}{1:08d}'.format(account_info, account.number)
        client_info = self.fill_with('Client:', 18)
        client_info = '{0}{1:<}'.format(client_info, account.client.name)
        date_str = datetime.now().strftime('%Y/%m/%d')
        date_info = self.fill_with('Date:', 18)
        date_info = '{0}{1:<}'.format(date_info, date_str)
        # Prints the header
        self.print_header(title, branch_info, account_info,
                          client_info, date_info)

    def __print_balance(self, account):
        pattern = self.get_line_pattern(BaseView.ALIGN_RIGHT)
        balance = account.get_balance()
        balance_str = 'TOTAL BALANCE: {0:.2f}'.format(balance)
        self.print_empty_header_line()
        print(pattern.format(balance_str))
        self.print_empty_header_line()
        self.print_border_line()
        self.wait_for_user()

    def create_account(self):
        try:
            data = {}
            self.print_header("CREATE NEW ACCOUNT")
            self.print_empty_lines(2)

            # TODO - Validate number and branch_id for integer input
            #number = input(self.fill_with('Account number (number):', 30))
            number_label = self.fill_with('Account number (number):', 30)
            account_number = random.randint(1, 999999)

            branch_id = input(self.fill_with('Branch id (number):', 30))
            data['branch_id'] = int(branch_id)
            data['number'] = account_number
            print('{0}{1:08d}'.format(number_label, account_number))
            data['name'] = input(self.fill_with('Client name:', 30))
            data['email'] = input(self.fill_with('Client email:', 30))
            data['login'] = input(self.fill_with('Client login:', 30))
            pwd = LoginView.input_password(self.fill_with('Password:', 30))
            data['password'] = pwd

            return data

        except Exception as e:
            self.show_message('ERROR', e.args[0], True)

    def show_client_accounts(self, accounts):
        self.print_header("CLIENT ACCOUNT LIST")
        self.print_empty_header_line()

        # Prints column headers
        pattern = '# {0:<6} | {1:<8} | {2:<7} | {3:<15} | {4:<15} | {5:<10} #'
        print(pattern.format('Branch', 'Account',
                             'Cli. Id', 'Name', 'Email', 'Login'))

        # Prints line divider and column values
        self.print_line_divider()
        pattern = '# {0:06d} | {1:08d} | {2:07d} | {3:<15} | {4:<15} | {5:<10} #'
        for account in accounts:
            print(pattern.format(account.branch_id,
                                 account.number,
                                 account.client.id,
                                 account.client.name,
                                 account.client.email,
                                 account.client.login
                                 ))

        self.print_empty_header_line()
        self.print_border_line()
        self.wait_for_user()

    def create_transaction(self, tx_type):
        try:
            data = {}
            self.print_header(tx_type)

            # TODO Validate date and amout for type before conversion
            # and allow user to try again
            date_str = input(self.fill_with('Date (YYYY/MM/DD):', 20))
            data['date'] = datetime.strptime(date_str, '%Y/%m/%d')
            data['description'] = input(self.fill_with('Description:', 20))
            amout_str = input(self.fill_with('Amount:', 20))
            data['amount'] = float(amout_str)

            return data

        except Exception as e:
            self.show_message('Error', e.args[0], True)

    def show_statement(self, account):
        self.__print_statements_header('ACCOUNT STATEMENT', account)

        # Prints table header
        pattern = '# {0:<15} | {1:<30} | {2:^7} | {3:>15} #'
        print(pattern.format('Date', 'Description', 'Type', 'Amount'))

        # Prints table divider and column values
        pattern = '# {0:<15} | {1:<30} | {2:^7} | {3:>15} #'
        self.print_line_divider()
        for tx in account.get_transaction_history():
            print(pattern.format(tx.date.strftime('%Y/%m/%d'),
                                 tx.description,
                                 tx.type_,
                                 '{0:.2f}'.format(tx.amount)
                                 ))

        # Prints the balance and waits for user
        self.print_line_divider()
        self.__print_balance(account)

    def show_balance(self, account):
        # Prints statement header
        self.__print_statements_header('ACCOUNT BALANCE', account)
        # Prints account balance
        self.__print_balance(account)


if __name__ == '__main__':
    view = AccountView()
    view.create_account()
    view.create_transaction('Deposit')
    view.create_transaction('Withdrawal')
