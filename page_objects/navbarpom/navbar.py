from selenium.webdriver import Keys

from page_objects.navbarpom.navbarprops import NavBarProps


class NavBar(NavBarProps):

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.user_icon.click()
        self.login_icon.click()

    def send_search_input(self, input_text):
        self.search_input_filed.send_keys(input_text)
        self.search_input_filed.send_keys(Keys.ENTER)

    def open_cart_page(self):
        self.cart_icon.click()

    def clear_search_input(self):
        self.search_input_filed.clear()



