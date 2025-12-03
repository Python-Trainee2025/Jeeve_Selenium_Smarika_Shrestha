import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.productdetailpom.productdetaillocators import ProductDetailLocators
from page_objects.productdetailpom.productdetailprops import ProductDetailProps


class ProductDetailPage(ProductDetailProps):

    def __init__(self, driver):
        self.driver = driver

    def get_product_from_homepage(self):
        self.product_homepage.click()


    def add_to_cart(self):
        self.add_to_cart_button.click()

    def added_to_cart_toast(self):
        toast_message=self.added_to_cart_toast.text
        return toast_message

    def stock_info(self):
        stock_message=self.stock_identifier.text
        return stock_message

    def identify_enabled_status(self):
        return self.add_to_cart_button.is_enabled()

    def click_product(self, timeout=10):

        wait = WebDriverWait(self.driver, timeout)

        try:
            el = wait.until(EC.presence_of_element_located(ProductDetailLocators.PRODUCT_HOMEPAGE))
        except TimeoutException:
            raise TimeoutException("Product not found in DOM")
        logging.info("Checkout button present")
        # center element in viewport to avoid fixed headers/footers covering it
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", el)
        time.sleep(6)  # let layout/animations settle and also the toast to disappear
        logging.info("Scrolling into view")

        el.click()
        logging.info("Product from homepage clicked successfully")
