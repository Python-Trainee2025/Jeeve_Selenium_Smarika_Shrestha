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
        logging.info("Product added to cart successfully")
        time.sleep(2)
        navbar.open_cart_page()
        logging.info("Cart page opened")
        time.sleep(3)
        initial_qty=int(cart.read_cart_quantity())
        logging.info(f"Initial Cart quantity:{initial_qty}")
        cart.increase_item_quantity()
        logging.info("Cart quantity increased")
        final_qty=int(cart.read_cart_quantity())
        logging.info(f"Final Cart Quantity after Increment:{final_qty}")
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

    # def test_remove_product_from_cart(self):
    #     navbar=NavBar(self.driver)
    #     cart=CartPage(self.driver)
    #
    #     self.add_product_to_cart()
    #     time.sleep(2)
    #     logging.info("Adding product to cart")
    #     navbar.open_cart_page()
    #     logging.info("Open cart")
    #     product = WebDriverWait(self.driver, 2).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         '//div[contains(@class,\'flex space-x-2 justify-between items-start\')]//span[contains(@class,\'select-none text-lg leading-none flex items-center justify-center\')]//*[name()=\'svg\']'))
    #
    #     )
    #     product.click()
    #
    #     ok_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         '//div[contains(@class,\'translate-y-0 modal relative w-full pointer-events-none transition-all duration- transform\')]//button[contains(@class,\'flex-1\')][normalize-space()=\'Ok\']')))
    #     ok_button.click()
    #     time.sleep(5)
    #
    #
