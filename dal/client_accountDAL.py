#!/usr/bin/env python3


from dal.personDAL import PersonDAL
from dal.accountDAL import AccountDAL
from dal.transactionDAL import TransactionDAL
from model.client import Client
from model.account import Account


"""Represents an instance of a Person DAL"""


class ClientAccountDAL(PersonDAL):

    def insert_client_account(self, client, account):
        sql_command = """INSERT INTO
							client_accounts
						(
							client_id,
							account_number
						)
						VALUES
						(
							{client_id},
							{account_number}
						);
						""".format(
            client_id=client.id,
            account_number=account.number
        )
        self.execute_non_query(sql_command)

    def delete_client_account(self, client, account):
        sql_command = """
						DELETE FROM
							client_accounts
						WHERE
							client_id = {client_id}
						AND
							account_number = {account_number}
							;
				""".format(
            client_id=client.id,
            account_number=account.number
        )
        self.execute_non_query(sql_command)

    def select_all_client_accounts(self):
        sql_command = """
						SELECT
							ca.client_id,
							p.name,
							p.email,
							p.login,
							p.password,
							ca.account_number,
							a.branch_id
						FROM
							client_accounts ca
						INNER JOIN people p
							ON ca.client_id = p.id
						INNER JOIN accounts a
							ON ca.account_number = a.number;
						"""

        result = self.execute_query(sql_command)

        return self.to_client_account_list(result)

    def select_client_account(self, client_id):
        sql_command = """
						SELECT
							ca.client_id,
							p.name,
							p.email,
							p.login,
							p.password,
							ca.account_number,
							a.branch_id
						FROM
							client_accounts ca
						INNER JOIN people p
							ON ca.client_id = p.id
						INNER JOIN accounts a
							ON ca.account_number = a.number
						WHERE
							ca.client_id = {client_id};
						""".format(client_id=client_id)

        result = self.execute_query(sql_command)

        return self.to_client_account(result[0])

    def to_client_account_list(self, rows):
        objects = []
        for row in rows:
            account = self.to_client_account(row)
            if account != None:
                objects.append(account)

        return objects

    def to_client_account(self, row):
        """ Row indexing (from "select_all_client_accounts")
        0=client_id, 1=client_name, 2=client_email, 3=client_login,
        4=client_password, 5=account_number, 6=account_branch_id """

        accountDAL = AccountDAL()
        account_number = row[5]
        account_branch = row[6]

        account = accountDAL.to_object([account_number, account_branch])
        client = self.__person_to_client(self.to_object(row))

        if client != None and account != None:
            tx_dal = TransactionDAL()
            transactions = tx_dal.select_by_account_number(account.number)
            if transactions != None:
                account.transactions = transactions
            client.accounts[account.number] = account
            account.client = client
            return account

        return None

    def __person_to_client(self, person):
        return Client(id_=person.id,
                      name=person.name,
                      email=person.email,
                      login=person.login,
                      password=person.password
                      )
