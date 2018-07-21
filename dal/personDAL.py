#!/usr/bin/env python3


from dal.baseDAL import BaseDAL
from model.person import Person


"""Represents an instance of a Bank"""


class PersonDAL(BaseDAL):

    def prepare_insert(self, obj):
        return """INSERT INTO people
				(
					name,
					email,
					role,
					login,
					password
				)
				VALUES
				(
					'{name}',
					'{email}',
					'{role}',
					'{login}',
					'{password}'
				);
				""".format(
            name=obj.name,
            email=obj.email,
            role=obj.role,
            login=obj.login,
            password=obj.password
        )

    def prepare_update(self, obj):
        return """
				UPDATE 
					people
				SET 
					name = '{name}',
					email = '{email}',
					role = '{role}',
					login = '{login}',
					password = '{password}'
				WHERE
					id={id_};
				""".format(
            name=obj.name,
            email=obj.email,
            role=obj.role,
            login=obj.login,
            password=obj.password,
            id_=obj.id
        )

    def prepare_delete(self, obj):
        return """
				DELETE FROM
					people
				WHERE
					id = {id_};
				""".format(
            id_=obj.id
        )

    def prepare_select(self, identifier):
        return """
				SELECT
					id,
					name,
					email,
					role,
					login,
					password
				FROM
					people
				WHERE
					id = {id};
				""".format(
            id_=identifier
        )

    def prepare_select_all(self):
        return """
				SELECT
					id,
					name,
					email,
					role,
					login,
					password
				FROM
					people;
				"""

    def select_by_role(self, role):
        sql_command = """
						SELECT
							id,
							name,
							email,
							role,
							login,
							password
						FROM
							people
						WHERE
							role = '{role}'
						""".format(
            role=role
        )

        return self.to_list(self.execute_query(sql_command))

    def select_by_login(self, login):
        sql_command = """
						SELECT
							id,
							name,
							email,
							role,
							login,
							password
						FROM
							people
						WHERE
							login = '{login}'
						""".format(
            login=login
        )

        # Executes the command and fetches into result
        result = self.execute_query(sql_command)

        # Result receives a list of rows. Only needs the first row.
        if len(result) > 0:
            return self.to_object(result[0])
        else:
            return None

    def to_object(self, row):
        if len(row) > 0:
            return (Person(id_=int(row[0]),
                           name=row[1],
                           email=row[2],
                           role=row[3],
                           login=row[4],
                           password=row[5]
                           )
                    )

        return None
