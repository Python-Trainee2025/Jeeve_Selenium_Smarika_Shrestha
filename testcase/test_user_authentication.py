import logging
import time

from page_objects.navbarpom.navbar import NavBar
from page_objects.loginpom.loginpage import LoginPage
from setup.basetest import BaseTest

class TestUserAuthentication(BaseTest):


    def test_login_with_correct_credentials(self):
        home=NavBar(self.driver)
        login=LoginPage(self.driver)

        self.open_url("https://jeevee.com")
        time.sleep(2)

        home.open_login_page()
        time.sleep(2)
        login.login(mobile_number='9804917782',password='Smarika@123')
        login_message=login.correct_credentials()
        # assert "Login success" in login_message, f"Expected success message, got: {login_message}"
        logging.info(f"Successful login message: {login_message}")

    def test_login_with_incorrect_credentials(self):
        home = NavBar(self.driver)
        login = LoginPage(self.driver)

        self.open_url("https://jeevee.com")
        time.sleep(2)

        home.open_login_page()
        time.sleep(2)
        login.login(mobile_number='9804917782', password='wdsfd')
        login_message = login.incorrect_credentials()
        assert "Username and Password not matching" in login_message, f"Expected success message, got: {login_message}"
        logging.info(f"Invalid Credential message: {login_message}")


