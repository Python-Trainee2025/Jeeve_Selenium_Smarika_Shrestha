import logging
import time
import json

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
        # Load credentials
        creds_path = r"C:\Users\smshrestha\Desktop\Trainee\Jeeve\creds\creds.json"

        with open(creds_path, "r") as f:
            self.creds = json.load(f)

    def teardown_method(self):
        self.driver.quit()

    def login_user(self):
        home=NavBar(self.driver)
        login=LoginPage(self.driver)
        baseurl=self.creds['base_url']
        self.open_url(baseurl)
        home.open_login_page()
        mobile_number=self.creds['valid_mobile_number']
        password=self.creds['valid_password']
        login.login(mobile_number=mobile_number,password=password)

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

