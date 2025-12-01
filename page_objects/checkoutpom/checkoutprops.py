from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.checkoutpom.checkoutlocators import CheckoutLocators


class CheckoutProps(CheckoutLocators):
    @property
    def edit_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(CheckoutLocators.EDIT_ADDRESS_BTN))

    @property
    def phone_number_field(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(CheckoutLocators.EDIT_PHONE_NUMBER))

    @property
    def update_address_btn(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(CheckoutLocators.UPDATE_ADDRESS))

    @property
    def alternate_number_field(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(CheckoutLocators.ALTERNATE_NUMBER))



