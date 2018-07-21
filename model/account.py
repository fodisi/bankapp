#!/usr/bin/env python3


from datetime import datetime

from model.transaction import Transaction
from model.client import Client


"""Represents a bank Account"""


class Account():
    def __init__(self, number=0, branch_id=0, client=None):
        self.number = number
        self.branch_id = branch_id
        self.client = client
        self.transactions = []

    def deposit(self, date, description, amount):
        tx = Transaction(date=date,
                         description=description,
                         amount=amount,
                         tx_type='D',
                         account_number=self.number)
        self.transactions.append(tx)
        return tx

    def withdrawal(self, date, description, amount):
        tx = Transaction(date=date,
                         description=description,
                         amount=amount * -1,
                         tx_type='W',
                         account_number=self.number)
        self.transactions.append(tx)
        return tx

    def get_balance(self):
        return sum(tx.amount for tx in self.transactions)

    def get_transaction_history(self):
        history = self.transactions[::]
        history.sort(key=lambda x: x.date)
        return history
