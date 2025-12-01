import time

from selenium.webdriver import Keys

from page_objects.checkoutpom.checkoutprops import CheckoutProps


class CheckoutPage(CheckoutProps):
    def __init__(self, driver):
        self.driver = driver

    def click_edit_address(self):
        self.edit_button.click()

    def edit_phone_number(self,phone_number):
        self.phone_number_field.clear()
        time.sleep(2)
        self.phone_number_field.send_keys(phone_number)
        self.phone_number_field.send_keys(Keys.ENTER)

    def click_update_address(self):
        self.update_address_btn.click()

    def extract_alternate_number(self):
        alternate_number = self.alternate_number_field.text
        return alternate_number