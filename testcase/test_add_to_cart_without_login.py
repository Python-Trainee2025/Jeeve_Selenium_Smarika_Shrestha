import time
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.loginpom.loginlocators import LoginLocators
from page_objects.navbarpom.navbar import NavBar
from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest


class TestAddToCartWithoutLogin(BaseTest):
    def test_add_to_cart_without_login(self):
        home = NavBar(self.driver)
        product = SearchResultPage(self.driver)
        cart = ProductDetailPage(self.driver)

        baseurl=self.creds['base_url']
        self.open_url(baseurl)
        home.send_search_input(input_text='lip balm')
        logging.info("Item searched")
        time.sleep(5)

        product.get_product()
        logging.info("Searched item displayed")
        time.sleep(5)
        cart.add_to_cart()
        logging.info("Add to Cart Button clicked")
        time.sleep(5)

        login_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.MOBILE_NUMBER_FIELD)
        )

        assert login_popup.is_displayed(), "Login popup did not appear after clicking Add to Cart"

