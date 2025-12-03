import logging
import time

from page_objects.navbarpom import navbar
from page_objects.navbarpom.navbar import NavBar
from setup.basetest import BaseTest
from page_objects.cartpom.cartpage import CartPage




class TestCartPage(BaseTest):

    def list_cart_items(self):
        navbar_obj = NavBar(self.driver)
        cart_obj = CartPage(self.driver)

        self.add_product_to_cart()
        logging.info("Product added to cart successfully")
        time.sleep(2)
        navbar_obj.open_cart_page()
        logging.info("Cart page opened")
        title = cart_obj.get_cart_item_title()
        logging.info(f"Title: {title}")

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

    def test_change_reflected_in_price_when_quantity_increased(self):
        navbar = NavBar(self.driver)
        cart = CartPage(self.driver)

        self.add_product_to_cart()
        logging.info("Product added to cart successfully")
        time.sleep(2)
        navbar.open_cart_page()
        logging.info("Cart page opened")
        time.sleep(5)
        logging.info(cart.get_price_per_item())
        price_per_piece = cart.get_price_per_item()
        item_price = price_per_piece.split()[-1]
        logging.info(f"Price per Item:{item_price}")
        ini_grand_total=cart.get_grand_total()
        initial_grand_total=ini_grand_total.split()[-1]
        logging.info(f"Grand Total before quantity increment:{initial_grand_total}")
        cart.increase_item_quantity()
        logging.info("Cart quantity increased")
        f_grand_total = cart.get_grand_total()
        final_grand_total = f_grand_total.split()[-1]
        logging.info(f"Grand Total after quantity increment:{final_grand_total}")
        assert float(final_grand_total) == float(initial_grand_total) + float(item_price), f"Expected {ini_grand_total + item_price}, got {final_grand_total}"


    def test_remove_item_from_cart(self):
        navbar_obj = NavBar(self.driver)
        cart_obj=CartPage(self.driver)

        self.add_product_to_cart()
        logging.info("Product added to cart successfully")
        time.sleep(2)
        navbar_obj.open_cart_page()
        logging.info("Cart page opened")
        title_before_removal=cart_obj.get_cart_item_title()
        logging.info(f"Items before removal: {title_before_removal}")
        removed_item=title_before_removal[0]
        logging.info(f"Removed item: {removed_item}")
        cart_obj.remove_cart_item()
        logging.info("Item removed from cart successfully")
        time.sleep(2)
        remove_toast=cart_obj.remove_item_message()
        logging.info(remove_toast)
        time.sleep(2)
        title_after_removal=cart_obj.get_cart_item_title()
        logging.info(f"Item after removal: {title_after_removal}")
        time.sleep(2)
        assert removed_item not in title_after_removal




