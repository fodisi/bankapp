#!/usr/bin/env python3


from dal.client_accountDAL import ClientAccountDAL
from dal.accountDAL import AccountDAL
from dal.transactionDAL import TransactionDAL
from model.client import Client
from model.account import Account
from view.account_view import AccountView


class AccountController():
    def __init__(self):
        self.view = AccountView()

    def __to_client_object(self, data):
        return Client(name=data['name'],
                      email=data['email'],
                      login=data['login'],
                      password=data['password'])

    def __to_account_object(self, data):
        return Account(number=data['number'],
                       branch_id=data['branch_id'])

    def create_account(self):
        try:
            data = self.view.create_account()
            account = self.__to_account_object(data)
            client = self.__to_client_object(data)
            account_dal = AccountDAL()
            client_dal = ClientAccountDAL()

            try:
                # inserts account and client into DB
                account_dal.insert(account)
                client_dal.insert(client)
                # Gets client from DB to refresh its ID info
                client = client_dal.select_by_login(client.login)
                # Inserts client account into DB
                client_dal.insert_client_account(client, account)
            except Exception:
                # Rollback if any insert command went wrong.
                client_dal.delete_client_account(client, account)
                client_dal.delete(client)
                account_dal.delete(account)
                raise

            message = 'Branch|Account: "{0}|{1}" for client "{2}" created successfully.'
            message = message.format(
                account.branch_id, account.number, client.name)
            self.view.show_message('Success', message, True)
        except Exception as e:
            msg_pattern = '{0}\n{1}\n\n{2}'
            main_message = 'Error inserting data into database'
            detail_message = 'Check if branch exists or if account number is already in use.'
            msg = msg_pattern.format(main_message, detail_message, e.args[0])
            self.view.show_message('Error', msg, True)

    def list_client_accounts(self):
        try:
            dal = ClientAccountDAL()
            accounts = dal.select_all_client_accounts()
            self.view.show_client_accounts(accounts)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)

    def create_transaction(self, account, tx_type):
        try:
            data = self.view.create_transaction(tx_type)

            transaction = None
            if tx_type == 'Deposit':
                transaction = account.deposit(
                    date=data['date'],
                    description=data['description'],
                    amount=data['amount']
                )
            elif tx_type == 'Withdrawal':
                transaction = account.withdrawal(
                    date=data['date'],
                    description=data['description'],
                    amount=data['amount']
                )
            else:
                msg = 'Invalid transaction type "{0}".'
                raise Exception(msg.format(tx_type))

            transaction_dal = TransactionDAL()
            transaction_dal.insert(transaction)

            message = 'Transaction recorded successfully.'
            self.view.show_message('Success', message, True)
        except Exception as e:
            main_message = 'Error inserting data into database'
            msg = '{0}\n\n{1}'.format(main_message, e.args[0])
            self.view.show_message('Error', msg, True)

    def list_statement(self, account):
        try:
            self.view.show_statement(account)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)

    def list_balance(self, account):
        try:
            self.view.show_balance(account)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)
