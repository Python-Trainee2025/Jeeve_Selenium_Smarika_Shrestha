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
