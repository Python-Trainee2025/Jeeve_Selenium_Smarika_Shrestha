from page_objects.loginpom.loginlocators import LoginLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginProps(LoginLocators):
    @property
    def mobile_number_filed(self):
        return self.driver.find_element(*LoginLocators.MOBILE_NUMBER_FIELD)

    @property
    def password_field(self):
        return self.driver.find_element(*LoginLocators.PASSWORD_FILED)

    @property
    def sign_in_button(self):
        return self.driver.find_element(*LoginLocators.SIGN_IN_BUTTON)


    @property
    def login_toast(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(LoginLocators.LOGIN_TOAST)
        )

    @property
    def login_error_message(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(LoginLocators.LOGIN_ERROR_MESSAGE)
        )

