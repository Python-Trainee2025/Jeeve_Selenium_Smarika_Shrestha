import logging
import time

from page_objects.navbarpom.navbar import NavBar
from setup.basetest import BaseTest
from page_objects.cartpom.cartpage import CartPage


class TestCartPage(BaseTest):

    def test_cart_increase_quantity(self):
        navbar=NavBar(self.driver)
        cart=CartPage(self.driver)

        self.add_product_to_cart()
        time.sleep(2)
        navbar.open_cart_page()
        time.sleep(3)
        initial_qty=int(cart.read_cart_quantity())
        logging.info(initial_qty)
        cart.increase_item_quantity()
        final_qty=int(cart.read_cart_quantity())
        logging.info(final_qty)
        time.sleep(2)
        assert final_qty  == initial_qty+ 1, f"Expected {initial_qty + 1}, got {final_qty}"

    def test_remove_cart_item(self):
        navbar=NavBar(self.driver)
        cart=CartPage(self.driver)

        self.add_product_to_cart()
        time.sleep(2)
        logging.info("Adding product to cart")
        navbar.open_cart_page()
        logging.info("Open cart")
        time.sleep(3)
        # cart.remove_cart_item()
        # time.sleep(2)
        # cart.checkout_of_cart()
