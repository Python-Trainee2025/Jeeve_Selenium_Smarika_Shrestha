import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException)
from page_objects.cartpom.cartlocators import CartLocators
from page_objects.cartpom.cartprops import CartProps


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver = driver

    def increase_item_quantity(self):
            self.increase_quantity.click()

    def read_cart_quantity(self):
            return self.cart_quantity.text

    def remove_cart_item(self):
        self.remove_item_button.click()

    def get_added_to_cart_toast(self):
        toast_message = self.added_to_cart_toast.text
        return toast_message



    def click_checkout_button(self, timeout=10):

        wait = WebDriverWait(self.driver, timeout)

        try:
            el = wait.until(EC.presence_of_element_located(CartLocators.CHECKOUT_BUTTON))
        except TimeoutException:
            raise TimeoutException("Checkout button not found in DOM")
        logging.info("Checkout button present")
        # center element in viewport to avoid fixed headers/footers covering it
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", el)
        time.sleep(6)  # let layout/animations settle and also the toast to disappear
        logging.info("Scrolling into view")

        el.click()
        logging.info("Checkout button clicked successfully")



