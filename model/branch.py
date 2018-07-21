#!/usr/bin/env python3


"""Represents a bank Branch"""


class Branch():
    def __init__(self, name="", id_=0):
        self.id = id_
        self.name = name
        self.accounts = {}

    def create_account(self, account):
        self.accounts[account.number] = account

    def account_exists(self, number):
        return number in self.accounts
