import logging

from page_objects.loginpom.loginlocators import LoginLocators
from page_objects.loginpom.loginprops import LoginProps


class LoginPage(LoginProps):
    def __init__(self, driver):
        self.driver = driver

    def login(self,mobile_number,password):
        self.mobile_number_filed.send_keys(mobile_number)
        self.password_field.send_keys(password)
        self.sign_in_button.click()


    def correct_credentials(self):
        login_toast_text= self.login_toast.text
        return login_toast_text

    def incorrect_credentials(self):
        login_error_text= self.login_error_message.text
        return login_error_text

    def clear_mobile_number_fields(self):
        self.mobile_number_filed.clear()

    def clear_password_fields(self):
        self.password_field.clear()