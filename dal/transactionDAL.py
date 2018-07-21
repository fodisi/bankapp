#!/usr/bin/env python3


from datetime import datetime

from dal.baseDAL import BaseDAL
from model.transaction import Transaction


"""Represents an instance of a Transaction DAL"""


class TransactionDAL(BaseDAL):

    def prepare_insert(self, obj):
        return """INSERT INTO transactions
				(
					account_number,
					date,
					type,
					description,
					amount
				)
				VALUES
				(
					{account_number},
					'{date}',
					'{type_}',
					'{description}',
					{amount}
				);
				""".format(
            account_number=obj.account_number,
            date=obj.date,
            type_=obj.type_,
            description=obj.description,
            amount=obj.amount
        )

    def prepare_update(self, obj):
        return """
				UPDATE 
					transactions
				SET 
					account_number = {account_number},
					date = '{date}',
					type = '{tx_type}',
					description = '{description}',
					amount = {amount}
				WHERE
					id = {id_};
				""".format(
            id_=obj.id,
            account_number=obj.account_number,
            date=obj.date,
            tx_type=obj.type_,
            description=obj.description,
            amount=obj.amount
        )

    def prepare_delete(self, obj):
        return """
				DELETE FROM
					transactions
				WHERE
					id = {id_};
				""".format(
            id_=obj.id
        )

    def prepare_select(self, identifier):
        return """
				SELECT
					id,
					account_number,
					strftime('%Y/%m/%d %H:%M:%S', date),
					type,
					description,
					amount
				FROM
					transactions
				WHERE
					id_ = {identifier};
				""".format(
            id_=identifier
        )

    def prepare_select_all(self):
        return """
				SELECT
					id,
					account_number,
					strftime('%Y/%m/%d %H:%M:%S', date),
					type,
					description,
					amount
				FROM
					transactions;
				"""

    def select_by_type(self, tx_type):
        sql_command = """
						SELECT
							id,
							account_number,
							strftime('%Y/%m/%d %H:%M:%S', date),
							type,
							description,
							amount
						FROM
							transactions
						WHERE
							type = '{tx_type}'
						""".format(
            tx_type=tx_type
        )

        return self.to_list(self.execute_query(sql_command))

    def select_by_account_number(self, account_number):
        sql_command = """
						SELECT
							id,
							account_number,
							strftime('%Y/%m/%d %H:%M:%S', date),
							type,
							description,
							amount
						FROM
							transactions
						WHERE
							account_number = {account_number}
						""".format(
            account_number=account_number
        )

        return self.to_list(self.execute_query(sql_command))

    def to_object(self, row):
        if len(row) > 0:
            return (Transaction(id_=int(row[0]),
                                account_number=int(row[1]),
                                date=datetime.strptime(
                                    row[2], '%Y/%m/%d  %H:%M:%S'),
                                tx_type=row[3],
                                description=row[4],
                                amount=row[5]
                                )
                    )

        return None
