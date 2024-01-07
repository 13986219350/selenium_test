from .user_page.home_page import HomePage
from .user_page.login_register_page import LoginRegisterPage


class UserEngine:
    def __init__(self, driver):
        self.driver = driver

    def register_account(self, email, password):
        home_page = HomePage(self.driver)
        home_page.go_to_login_register()
        login_register_page = LoginRegisterPage(self.driver)
        login_register_page.register(email, password)


