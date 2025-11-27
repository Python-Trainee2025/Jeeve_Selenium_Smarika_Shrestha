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
        logging.info(f"Successful login message: {login_message}")

    def test_login_with_incorrect_credentials(self):
        home = NavBar(self.driver)
        login = LoginPage(self.driver)

        self.open_url("https://jeevee.com")
        time.sleep(2)

        home.open_login_page()
        time.sleep(2)
        login.login(mobile_number='9804917783', password='Smarika@123')
        login_message = login.incorrect_credentials()
        logging.info(f"Invalid Credential message: {login_message}")


