#!/usr/bin/env python3

from dal.baseDAL import BaseDAL
from model.account import Account


"""Represents an instance of a Account DAL"""


class AccountDAL(BaseDAL):

    def prepare_insert(self, obj):
        return """INSERT INTO accounts
				(
					number,
					branch_id
				)
				VALUES
				(
					{number},
					{branch_id}
				);
				""".format(
            number=obj.number,
            branch_id=obj.branch_id
        )

    def prepare_update(self, obj):
        return """
				UPDATE 
					accounts
				SET 
					branch_id = {branch_id}
				WHERE
					number = {number};
				""".format(
            number=obj.number,
            branch_id=obj.branch_id
        )

    def prepare_delete(self, obj):
        return """
				DELETE FROM
					accounts
				WHERE
					number = {number};
				""".format(
            number=obj.number
        )

    def prepare_select(self, identifier):
        return """
				SELECT
					number,
					branch_id
				FROM
					accounts
				WHERE
					number = {number};
				""".format(
            number=identifier
        )

    def prepare_select_all(self):
        return """
				SELECT
					number,
					branch_id
				FROM
					accounts;
				"""

    def to_object(self, row):
        if len(row) > 0:
            return (Account(number=int(row[0]), branch_id=int(row[1])))

        return None
