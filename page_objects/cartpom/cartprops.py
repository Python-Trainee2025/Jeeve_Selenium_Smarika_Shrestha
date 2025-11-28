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

