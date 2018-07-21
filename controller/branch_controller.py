#!/usr/bin/env python3


from dal.branchDAL import BranchDAL
from model.branch import Branch
from view.branch_view import BranchView


class BranchController():
    def __init__(self):
        self.view = BranchView()

    # returns a user type
    def create_branch(self):
        try:
            name = self.view.create_branch()
            branch = Branch(name)
            dal = BranchDAL()
            dal.insert(branch)
            message = 'Branch "{0}" inserted successfully.'
            self.view.show_message('Success',
                                   message.format(branch.name),
                                   True)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)

    def list_branches(self):
        try:
            dal = BranchDAL()
            branches = dal.select_all()
            self.view.show_branches(branches)
        except Exception as e:
            self.view.show_message('Error', e.args[0], True)
