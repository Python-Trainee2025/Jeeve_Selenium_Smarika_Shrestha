from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.cartpom.cartlocators import CartLocators


class CartProps(CartLocators):

    @property
    def increase_quantity(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(CartLocators.INCREASE_QUANTITY_BUTTON)
        )

    @property
    def cart_quantity(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(CartLocators.CART_QUANTITY)
        )

    @property
    def remove_item_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(CartLocators.REMOVE_ITEM_BUTTON))

    @property
    def checkout_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(CartLocators.CHECKOUT_BUTTON))

    @property
    def added_to_cart_toast(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(CartLocators.ADDED_TO_CART_TOAST))








