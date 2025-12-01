import logging
import time
from page_objects.cartpom.cartpage import CartPage
from page_objects.navbarpom.navbar import NavBar
from setup.basetest import BaseTest


class TestEmptyCart(BaseTest):
    def test_empty_cart(self):
        nav_obj=NavBar(self.driver)
        cart_obj=CartPage(self.driver)

        self.login_user()
        time.sleep(3)
        nav_obj.open_cart_page()
        empty_cart_message=cart_obj.check_empty_cart()
        logging.info(empty_cart_message)
        time.sleep(5)
        is_enabled=cart_obj.check_checkout_button()
        logging.info(f'Button Enabled: {is_enabled}')

        if "no items" in empty_cart_message:
            assert not is_enabled, f"Expected button disabled for Out of Stock, but got enabled"
        elif "In Stock" in empty_cart_message:
            assert is_enabled, f"Expected button enabled for In Stock, but got disabled"


