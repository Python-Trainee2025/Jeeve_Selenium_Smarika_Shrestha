import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.navbarpom.navbar import NavBar
from page_objects.loginpom.loginpage import LoginPage
from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from page_objects.searchresultpom.searchresultpage import SearchResultPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
# logger.info("Logger initialized for test_logs")
class BaseTest:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("guest")
        prefs={

            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection_enabled": False


        }
        chrome_options.add_experimental_option("prefs",prefs)

        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def login_user(self):
        home=NavBar(self.driver)
        login=LoginPage(self.driver)
        self.open_url('https://jeevee.com')
        home.open_login_page()
        login.login(mobile_number='9804917782',password='Smarika@123')

    def add_product_to_cart(self):
        home=NavBar(self.driver)
        product=SearchResultPage(self.driver)
        cart=ProductDetailPage(self.driver)

        self.login_user()
        home.send_search_input(input_text='lip balm')
        logging.info('key sent')
        product.get_product()
        logging.info('product displayed')
        cart.add_to_cart()
        logging.info('Successfully added product to cart')


    def open_url(self, url):
        self.driver.get(url)

