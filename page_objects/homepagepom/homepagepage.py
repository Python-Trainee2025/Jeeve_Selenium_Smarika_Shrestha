from selenium.webdriver import Keys

from page_objects.homepagepom.homepageprops import HomePageProps


class HomePagePage(HomePageProps):

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.user_icon.click()
        self.login_icon.click()

    def send_search_input(self, input_text):
        self.search_input_filed.send_keys(input_text)
        self.search_input_filed.send_keys(Keys.ENTER)



