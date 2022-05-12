import pytest

from Pages.LoginPage import LoginPage
from Test.Test_Base import BaseTest
from Config.config import TestData


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.get_singup_link_exists()
        assert flag

    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        title = self.loginpage.get_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
