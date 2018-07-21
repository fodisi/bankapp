#!/usr/bin/env python3

from view.base_view import BaseView
from view.account_view import AccountView
from view.branch_view import BranchView
from view.login_view import LoginView
from view.person_view import PersonView
from view.main_view import MainView


if __name__ == '__main__':
    # base_view = BaseView(70)
    # base_view.print_header('UNIT TEST')

    # account_view = AccountView()
    # account_view.create_account()
    # # account_view.create_transaction('Deposit')

    # branch_view = BranchView()
    # branch_view.create_branch()

    # login_view = LoginView()
    # login_view.show_login()

    # person_view = PersonView()
    # person_view.create_person('Manager')

    main_view = MainView()
    main_view.show_main_menu('admin')
    input()

    main_view.show_admin_menu()