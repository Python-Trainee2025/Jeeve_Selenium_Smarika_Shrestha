from page_objects.cartpom.cartpage import CartPage
from page_objects.navbarpom.navbar import NavBar
from setup.basetest import BaseTest
import time


class TestCheckout(BaseTest):
    def test_checkout(self):
        navbar = NavBar(self.driver)
        cart = CartPage(self.driver)

        self.add_product_to_cart()
        time.sleep(2)
        navbar.open_cart_page()
        time.sleep(3)
        cart.click_checkout_button()
        time.sleep(10)