import time

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

        self.open_url('https://jeevee.com')
        home.send_search_input(input_text='lip balm')
        time.sleep(5)

        product.get_product()
        time.sleep(5)
        cart.add_to_cart()
        time.sleep(5)

        login_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.MOBILE_NUMBER_FIELD)
        )

        assert login_popup.is_displayed(), "Login popup did not appear after clicking Add to Cart"

