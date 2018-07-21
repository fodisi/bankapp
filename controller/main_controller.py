#!/usr/bin/env python3


from dal.personDAL import PersonDAL
from dal.client_accountDAL import ClientAccountDAL
from controller.branch_controller import BranchController
from controller.person_controller import PersonController
from controller.account_controller import AccountController
from view.main_view import MainView
from view.login_view import LoginView


class MainController():
    def __init__(self):
        self.view = MainView()

    def start_session(self):
        # profile may be:
        # - a string if loging is invalid OR user is ADMIN
        # - an Account object, if a customer performed a successful login
        # - a person object, if a manager performed a successful login
        profile = self.login()
        if profile == 'invalid':
            return

        option = -1
        while option != 0:
            # Shows main menu according to profile
            option = self.view.show_main_menu(profile)
            # client - account deposit
            if option == 1:
                AccountController().create_transaction(profile, 'Deposit')
            # client - account withdrawal
            elif option == 2:
                AccountController().create_transaction(profile, 'Withdrawal')
            # client - account balance
            elif option == 3:
                AccountController().list_balance(profile)
            # client - account history
            elif option == 4:
                AccountController().list_statement(profile)
            # admin - create branch
            elif option == 100:
                BranchController().create_branch()
            # admin - list branches
            elif option == 101:
                BranchController().list_branches()
            # admin - create manager
            elif option == 102:
                PersonController().create_person('Manager')
            # admin - list managers
            elif option == 103:
                PersonController().list_people('Manager')
            # manager-create account
            elif option == 200:
                AccountController().create_account()
            # manager-list accounts
            elif option == 201:
                AccountController().list_client_accounts()
            elif option != 0:
                self.view.show_message('Error', 'Invalid option. Please try again.', True)


    def login(self):
        user, password = LoginView().show_login()

        if user in ['admin', 'ADMIN']:
            return user

        # Validates login with DB.
        person_dal = PersonDAL()
        person = person_dal.select_by_login(user)

        if person != None:
            # Validates input agains database info.
            valid_login = person.login == user and person.password == password

            # For clients, gets the Client Account object and returns it
            if valid_login and person.role == 'C':
                account_dal = ClientAccountDAL()
                client_account = account_dal.select_client_account(person.id)
                if client_account != None:
                    return client_account
            
            # For manager, gets the Manager object and returns it
            if valid_login and person.role == 'M':
                return person

        self.view.show_message('Error', 'Invalid login.', True)
        return 'invalid'
