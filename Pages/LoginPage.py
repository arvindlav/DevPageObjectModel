from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class LoginPage(BasePage):
    """""Page Objects"""""
    Email = (By.ID, "username")
    Password = (By.ID, "password")
    Login_Button = (By.ID, "loginBtn")
    Sign_Up = (By.LINK_TEXT, "Sign up")

    """"Constructor of Page Class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    def get_login_title(self, title):
        return self.get_login_title(title)

    def get_singup_link_exists(self):
        return self.is_visible(self.Sign_Up)

    def do_login(self, username, password):
        self.send_keys(self.Email, username)
        self.send_keys(self.Password, password)
        self.do_click(self.Login_Button)
