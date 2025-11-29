import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.navbarpom.navbar import NavBar
from setup.basetest import BaseTest
from page_objects.cartpom.cartpage import CartPage
from selenium.webdriver.common.by import By



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

    # def test_remove_cart_item(self):
    #     navbar=NavBar(self.driver)
    #     cart=CartPage(self.driver)
    #
    #     self.add_product_to_cart()
    #     time.sleep(2)
    #     logging.info("Adding product to cart")
    #     navbar.open_cart_page()
    #     logging.info("Open cart")
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(
    #             (By.XPATH, "//div[contains(@class,'flex') and contains(@class,'space-x-2')]"))
    #     )
    #     cart.remove_cart_item()
    #     cart.remove_cart_item()
    #     time.sleep(2)
        # cart.checkout_of_cart()
