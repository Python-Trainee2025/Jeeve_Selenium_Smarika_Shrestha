import time
from page_objects.cartpom.cartpage import CartPage
from page_objects.checkoutpom.checkout import CheckoutPage
from page_objects.loginpom.loginpage import LoginPage
from page_objects.navbarpom.navbar import NavBar
from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest


class TestDemo(BaseTest):
    def test_demo(self):
        nav_obj=NavBar(self.driver)
        login_obj=LoginPage(self.driver)
        search_obj=SearchResultPage(self.driver)
        product_obj=ProductDetailPage(self.driver)
        cart_obj=CartPage(self.driver)
        checkout_obj=CheckoutPage(self.driver)

        self.open_url('https://jeevee.com')
        time.sleep(2)
        nav_obj.send_search_input(input_text='lip balm')
        time.sleep(2)
        search_obj.get_product()
        time.sleep(2)
        product_obj.add_to_cart()
        time.sleep(2)
        login_obj.login(mobile_number='9804917782',password='Smarika@123')
        time.sleep(5)
        product_obj.add_to_cart()
        time.sleep(2)
        nav_obj.clear_search_input()
        nav_obj.send_search_input(input_text='tshirt')
        search_obj.get_product()
        time.sleep(2)
        product_obj.add_to_cart()
        time.sleep(2)
        nav_obj.open_cart_page()
        time.sleep(2)
        cart_obj.increase_item_quantity()
        time.sleep(2)
        cart_obj.decrease_item_quantity()
        time.sleep(2)
        cart_obj.click_checkout_button()
        time.sleep(3)
        checkout_obj.click_edit_address()
        time.sleep(5)
        phone_number = '9841850042'
        checkout_obj.edit_phone_number(phone_number=phone_number)
        time.sleep(3)
        checkout_obj.click_update_address()
        time.sleep(5)

