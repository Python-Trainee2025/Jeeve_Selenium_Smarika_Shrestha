from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.productdetailpom.productdetaillocators import ProductDetailLocators


class ProductDetailProps(ProductDetailLocators):

    @property
    def add_to_cart_button(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(ProductDetailLocators.ADD_TO_CART_BUTTON)
        )


    @property
    def added_to_cart_toast(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(*ProductDetailLocators.ADDED_TO_CART_TOAST)
        )
