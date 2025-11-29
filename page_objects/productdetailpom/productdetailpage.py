import logging

from selenium.webdriver.support.wait import WebDriverWait

from page_objects.productdetailpom.productdetailprops import ProductDetailProps


class ProductDetailPage(ProductDetailProps):

    def __init__(self, driver):
        self.driver = driver


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
