import time

from page_objects.navbarpom.navbar import NavBar
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest


class TestAddProductToCart(BaseTest):

    def test_add_product_to_cart(self):
        home=NavBar(self.driver)
        product=SearchResultPage(self.driver)

        self.login_user()
        home.send_search_input(input_text='lip balm')
        product.get_product()
        time.sleep(2)
