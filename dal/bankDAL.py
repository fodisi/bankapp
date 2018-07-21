# #!/usr/bin/env python3

# from model.bank import Bank
# from dal.baseDAL import BaseDAL


# """Represents an instance of a Bank"""
# class BankDAL(BaseDAL):

	# def prepare_insert(self, obj):
		# return	"""
				# INSERT INTO banks
				# (
					# name
				# )
				# VALUES
				# (
					# '{name}'
				# );
				# """.format(
						# name=obj.name
					# )

	# def prepare_update(self, obj):
		# return 	"""
				# UPDATE 
					# banks
				# SET 
					# name='{name}'
				# WHERE
					# id={id_};
				# """.format(
						# name=obj.name,
						# id_=obj.id
					# )

	# def prepare_delete(self, obj):
		# return 	"""
				# DELETE FROM
					# banks
				# WHERE
					# id={id_};
				# """.format(id_=obj.id)

	# def prepare_select(self, identifier):
		# return	"""
				# SELECT
					# *
				# FROM
					# banks
				# WHERE
					# id={id_};
				# """.format(
						# id_=identifier
					# )

	# def prepare_select_all(self):
		# return 	"""
				# SELECT
					# * 
				# FROM
					# banks;
				# """
	
	# def to_object(self, row):
		# if len(row) > 0:
			# return (Bank(row[0], row[1]))
		
		# return None
