#!/usr/bin/env python3


from dal.baseDAL import BaseDAL
from model.branch import Branch


"""Represents an instance of a Bank"""


class BranchDAL(BaseDAL):

    def prepare_insert(self, obj):
        return """INSERT INTO branches
				(
					name
				)
				VALUES
				(
					'{name}'
				);
				""".format(
            name=obj.name
        )

    def prepare_update(self, obj):
        return """
				UPDATE 
					branches
				SET 
					name='{name}'
				WHERE
					id={id_};
				""".format(
            name=obj.name,
            id_=obj.id
        )

    def prepare_delete(self, obj):
        return """
				DELETE FROM
					branches
				WHERE
					id={id_};
				""".format(
            id_=obj.id
        )

    def prepare_select(self, identifier):
        return """
				SELECT
					id,
					name
				FROM
					branches
				WHERE
					id={id};
				""".format(
            id_=identifier
        )

    def prepare_select_all(self):
        return """
				SELECT
					id,
					name
				FROM
					branches;
				"""

    def to_object(self, row):
        if len(row) > 0:
            return (Branch(id_=int(row[0]), name=row[1]))

        return None
