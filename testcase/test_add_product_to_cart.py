import time
import logging

from page_objects.cartpom.cartpage import CartPage
from page_objects.navbarpom.navbar import NavBar
from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest


class TestAddProductToCart(BaseTest):

    def test_add_product_to_cart(self):
        navbar_obj = NavBar(self.driver)
        search_obj = SearchResultPage(self.driver)
        product_obj = ProductDetailPage(self.driver)
        cart_obj = CartPage(self.driver)

        self.login_user()
        time.sleep(5)
        navbar_obj.send_search_input(input_text='lip balm')
        logging.info("Item searched")
        search_obj.get_product()
        logging.info("Searched Item Displayed")
        time.sleep(5)
        product_obj.add_to_cart()
        logging.info("Added Item to Cart")
        time.sleep(5)
        # navbar_obj.open_cart_page()
        # cart_obj.remove_cart_item()
        message = cart_obj.get_added_to_cart_toast()
        assert "Added to the cart successfully" in message, f"Expected success message, got: {message}"
        logging.info("Added to the cart successfully")

    def test_add_multiple_items_to_cart(self):
        navbar_obj = NavBar(self.driver)
        search_obj = SearchResultPage(self.driver)
        product_obj = ProductDetailPage(self.driver)
        cart_obj = CartPage(self.driver)

        self.login_user()
        time.sleep(5)
        navbar_obj.send_search_input(input_text='sunscren')
        logging.info("Item searched")
        search_obj.get_product()
        logging.info("Searched Item Displayed")
        time.sleep(5)
        product_obj.add_to_cart()
        logging.info("Added Item to Cart")
        time.sleep(5)

        navbar_obj.clear_search_input()
        navbar_obj.send_search_input(input_text='face wash')
        logging.info("Item searched")
        search_obj.get_product()
        logging.info("Searched Item Displayed")
        time.sleep(5)
        product_obj.add_to_cart()
        logging.info("Added Item to Cart")
        time.sleep(5)
        message=cart_obj.get_added_to_cart_toast()
        logging.info(message)
        logging.info("Added multiple items to the cart successfully")





