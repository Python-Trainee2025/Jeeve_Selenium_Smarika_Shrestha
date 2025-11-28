import time
import logging

from page_objects.cartpom.cartpage import CartPage
from page_objects.navbarpom.navbar import NavBar
from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest


class TestAddProductToCart(BaseTest):

    def test_add_product_to_cart(self):
        home=NavBar(self.driver)
        product=SearchResultPage(self.driver)
        cart=ProductDetailPage(self.driver)
        checkout=CartPage(self.driver)

        self.login_user()
        time.sleep(5)
        home.send_search_input(input_text='lip balm')
        product.get_product()
        time.sleep(5)
        cart.add_to_cart()
        time.sleep(5)
        # toast_message=cart.added_to_cart_toast()
        # logging.info(toast_message)
        home.open_cart_page()
        time.sleep(5)



