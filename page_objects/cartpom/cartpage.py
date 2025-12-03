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

    def decrease_item_quantity(self):
            self.decrease_quantity.click()

    def read_cart_quantity(self):
            return self.cart_quantity.text

    def remove_cart_item(self):
        self.remove_item_cross_button.click()
        self.remove_item_button.click()

    def remove_item_message(self):
        remove_message=self.remove_item_toast.text
        return remove_message

    def get_added_to_cart_toast(self):
        toast_message = self.added_to_cart_toast.text
        return toast_message

    def check_empty_cart(self):
        empty_message = self.empty_cart.text
        return empty_message

    def get_price_per_item(self):
        price_per_item = self.price_per_item.text
        return price_per_item

    # def get_cart_item_title(self):
    #     titles=self.cart_item_title()
    #     for title in titles:
    #         logging.info(title.text)

    def get_cart_item_title(self):
        titles = self.cart_item_title
        title_list=[title.text for title in titles]
        return title_list

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


    def check_checkout_button(self, timeout=10):

        wait = WebDriverWait(self.driver, timeout)

        try:
            el = wait.until(EC.presence_of_element_located(CartLocators.CHECKOUT_BUTTON))
        except TimeoutException:
            raise TimeoutException("Checkout button not found in DOM")

        return el.is_enabled()

    def get_grand_total(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        try:
            el = wait.until(EC.presence_of_element_located(CartLocators.GRAND_TOTAL))
        except TimeoutException:
            raise TimeoutException("Grand Total element not found in DOM")

        # logging.info("Grand Total element present")

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", el)
        time.sleep(2)  # Let layout/animations settle
        logging.info("Scrolled Grand Total into view")

        grand_total_text = el.text
        # logging.info(f"Grand Total text: {grand_total_text}")

        return grand_total_text

