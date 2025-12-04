import logging
import time

from page_objects.navbarpom.navbar import NavBar
from page_objects.loginpom.loginpage import LoginPage
from setup.basetest import BaseTest

class TestUserAuthentication(BaseTest):

    def test_login_with_incorrect_credentials(self):
        home = NavBar(self.driver)
        login = LoginPage(self.driver)
        baseurl=self.creds['base_url']
        self.open_url(url=baseurl)
        time.sleep(2)
        logging.info("Jeevee website opened")
        home.open_login_page()
        time.sleep(2)
        logging.info("Login page opened")
        mobile_number=self.creds['invalid_mobile_number']
        password=self.creds['invalid_password']
        login.login(mobile_number=mobile_number, password=password)
        logging.info("Invalid credentials entered")
        login_message = login.incorrect_credentials()
        assert "Username and Password not matching" in login_message, f"Expected success message, got: {login_message}"
        logging.info(f"Invalid Credential message: {login_message}")




