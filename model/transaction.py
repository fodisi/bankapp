#!/usr/bin/env python3


from datetime import datetime

"""Represents a bank transaction, such as deposit, withdrawal, etc."""


class Transaction():
    def __init__(self,
                 date=datetime.now(),
                 description='',
                 amount=0,
                 tx_type='',
                 account_number=0,
                 id_=0):
        self.id = id_
        self.account_number = account_number
        self.date = date
        self.description = description
        self.amount = amount
        self.type_ = tx_type
