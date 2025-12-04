import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.cartpom.cartpage import CartPage
from page_objects.checkoutpom.checkout import CheckoutPage
from page_objects.loginpom.loginlocators import LoginLocators
from page_objects.loginpom.loginpage import LoginPage
from page_objects.navbarpom.navbar import NavBar
from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest
from selenium.webdriver.support import expected_conditions as EC


class TestDemo(BaseTest):
    def test_user_purchase_flow(self):
        nav_obj=NavBar(self.driver)
        login_obj=LoginPage(self.driver)
        search_obj=SearchResultPage(self.driver)
        product_obj=ProductDetailPage(self.driver)
        cart_obj=CartPage(self.driver)
        checkout_obj=CheckoutPage(self.driver)

        baseurl=self.creds['base_url']
        self.open_url(baseurl)
        logging.info('Jeeve website opened')
        time.sleep(8)

        #add to cart without login
        nav_obj.send_search_input(input_text='lip balm')
        logging.info('Search key entered')
        search_obj.get_product()
        logging.info('Search product found')
        time.sleep(5)
        product_obj.add_to_cart()
        logging.info('Trying to add product to cart')
        login_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.MOBILE_NUMBER_FIELD)
        )

        assert login_popup.is_displayed(), "Login popup did not appear after clicking Add to Cart"
        time.sleep(8)

        #login with valid credential
        login_obj.clear_mobile_number_fields()
        login_obj.clear_password_fields()
        mobile_number = self.creds['valid_mobile_number']
        password=self.creds['valid_password']
        login_obj.login(mobile_number=mobile_number,password=password)
        login_message = login_obj.correct_credentials()
        logging.info(f"Toast message: {login_message}")
        assert "Login Success" in login_message, f"Expected success message, got: {login_message}"
        logging.info('Login successful')
        time.sleep(5)

        #add item from homepage to cart
        product_obj.add_to_cart()
        logging.info('Item added to cart')
        time.sleep(5)

        #product searched by sending key to search field
        nav_obj.clear_search_input()
        logging.info('Clear search input')
        nav_obj.send_search_input(input_text='sunscreen')
        logging.info('Search key entered')
        search_obj.get_product()
        logging.info('Search product found')
        time.sleep(3)
        product_obj.add_to_cart()
        logging.info('Item added to cart')
        time.sleep(5)

        #open cart page
        nav_obj.open_cart_page()
        logging.info('Cart page opened')
        time.sleep(5)

        #list cart items
        title = cart_obj.get_cart_item_title()
        logging.info(f"Title: {title}")
        time.sleep(5)

        #check if the change is reflected in the quantity
        initial_qty = int(cart_obj.read_cart_quantity())
        logging.info(f"Initial Cart quantity:{initial_qty}")
        cart_obj.increase_item_quantity()
        logging.info("Cart quantity increased")
        final_qty = int(cart_obj.read_cart_quantity())
        logging.info(f"Final Cart Quantity after Increment:{final_qty}")
        time.sleep(5)

        #remove item from cart
        title_before_removal = cart_obj.get_cart_item_title()
        logging.info(f"Items before removal: {title_before_removal}")
        removed_item = title_before_removal[0]
        logging.info(f"Removed item: {removed_item}")
        cart_obj.remove_cart_item()
        logging.info("Item removed from cart successfully")
        time.sleep(2)
        remove_toast = cart_obj.remove_item_message()
        logging.info(remove_toast)
        time.sleep(2)
        title_after_removal = cart_obj.get_cart_item_title()
        logging.info(f"Item after removal: {title_after_removal}")
        time.sleep(2)

        #open checkout page
        cart_obj.click_checkout_button()
        logging.info("Checkout button clicked")
        time.sleep(10)
        logging.info("Checkout page opened")

        #edit address page
        checkout_obj.click_edit_address()
        logging.info("Edit Address Page opened")
        time.sleep(5)
        phone_number = '9841850042'
        checkout_obj.edit_phone_number(phone_number=phone_number)
        logging.info("New Phone Number entered")
        time.sleep(3)
        checkout_obj.click_update_address()
        logging.info("Address updated")
        time.sleep(5)
        after_edit = checkout_obj.extract_alternate_number()
        logging.info("Alternate Number Extracted")
        logging.info(after_edit)
        updated_number = after_edit.split()[-1]
        logging.info(updated_number)
        logging.info("User Purchase flow completed")

        # cart_obj.increase_item_quantity()
        # logging.info('Cart Item quantity increased')
        # time.sleep(5)
        # cart_obj.decrease_item_quantity()
        # logging.info('Cart Item quantity decreased')
        # time.sleep(5)
        # cart_obj.click_checkout_button()
        # logging.info('Checkout page opened')
        # time.sleep(5)
        # checkout_obj.click_edit_address()
        # logging.info('Edit address clicked')
        # time.sleep(5)
        # phone_number = '9841850042'
        # checkout_obj.edit_phone_number(phone_number=phone_number)
        # logging.info('Updated phone number entered')
        # time.sleep(3)
        # checkout_obj.click_update_address()
        # logging.info('Address updated')
        # time.sleep(5)

