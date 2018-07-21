#!/usr/bin/env python3


from view.base_view import BaseView
from model.branch import Branch


class BranchView(BaseView):

    def __init__(self):
        super().__init__()

    def create_branch(self):
        self.print_header('CREATE NEW BRANCH')
        self.print_empty_lines(2)
        return input('Type the branch name:    ')

    def show_branches(self, branches):
        self.print_header('BRANCH LIST')

        # Prints column headers
        print('# {0:<7} | {1:<67}#'.format('Id', 'Name'))
        # Prints line divider and column values
        self.print_line_divider()
        for branch in branches:
            print('# {0:07d} | {1:<67}#'.format(branch.id, branch.name))

        # Waits for user input
        self.print_empty_header_line()
        self.print_border_line()
        self.wait_for_user()


if __name__ == '__main__':
    view = BranchView()
    view.create_branch()
