import logging

from page_objects.cartpom.cartpage import CartPage
from page_objects.checkoutpom.checkout import CheckoutPage
from page_objects.navbarpom.navbar import NavBar
from setup.basetest import BaseTest
import time


class TestCheckout(BaseTest):
    # def test_open_checkout(self):
    #     navbar = NavBar(self.driver)
    #     cart = CartPage(self.driver)
    #
    #     self.add_product_to_cart()
    #     time.sleep(2)
    #     navbar.open_cart_page()
    #     time.sleep(3)
    #     cart.click_checkout_button()
    #     time.sleep(10)

    def test_edit_address(self):
        navbar = NavBar(self.driver)
        cart = CartPage(self.driver)
        checkout_obj = CheckoutPage(self.driver)

        self.add_product_to_cart()
        time.sleep(2)
        navbar.open_cart_page()
        time.sleep(3)
        cart.click_checkout_button()
        time.sleep(5)
        checkout_obj.click_edit_address()
        time.sleep(5)
        phone_number='9841850042'
        checkout_obj.edit_phone_number(phone_number=phone_number)
        time.sleep(3)
        checkout_obj.click_update_address()
        time.sleep(5)
        after_edit=checkout_obj.extract_alternate_number()
        logging.info(after_edit)
        updated_number=after_edit.split()[-1]
        logging.info(updated_number)
        assert phone_number==updated_number ," Not a match"