# #!/usr/bin/env python3


# from model.bank import Bank
# from model.branch import Branch
# from model.account import Account
# #from dal import BankDAL


# if __name__ == '__main__':
	# bank = Bank(1, 'bankname')
	# branch = Branch(1, 'branch1')
	
	# bank.add_branch(branch)
	# print('bank name' + bank.name)
	# print('branch name' + branch.name)
	# print('branches count {0}'.format(len(bank.branches)))
	
	# print('branch {0} exists? {1}'.format(1, bank.branch_exists(1)))
	# print('branch {0} exists? {1}'.format(2, bank.branch_exists(2)))

	# account = Account(1234)

	# account.withdrawal(1, '2018-06-08', 'w1', 100)
	# account.deposit(1, '2018-06-01', 'd1', 1000)
	# account.deposit(1, '2018-06-09', 'd2', 500)
	
	
	# branch.create_account(account)
	
	# print('account balance: {0}'.format(account.get_balance()))
	
	# tx = account.get_transaction_history()
	# for i in tx:
		# print("{date}, {tx_id}, {description}, {amount}, {tx_type}".format(
				# date=i.date, 
				# tx_id=i.id,
				# description=i.description, 
				# amount=i.amount, 
				# tx_type=i.type))
	
