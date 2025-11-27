import logging
import time

from page_objects.navbarpom.navbar import NavBar
from page_objects.searchresultpom.searchresultpage import SearchResultPage
from setup.basetest import BaseTest


class TestSearchFunctionality(BaseTest):

    def test_search_item(self):
        search_key='lip balm'
        home = NavBar(self.driver)
        item=SearchResultPage(self.driver)

        self.open_url("https://jeevee.com")
        time.sleep(2)

        home.send_search_input(search_key)
        time.sleep(2)
        name=item.get_all_product_names()
        logging.info(name)

        keyword_parts=search_key.lower().split(" ")

        for product in name:
            lower_name = product.lower()
            # assert ("lip" in lower_name or "balm" in lower_name), \
            #     f"Irrelevant product found: {product}"
            # making it dynamic
            assert any(word in lower_name for word in keyword_parts), \
                f"Irrelevant product found: {product}"

        print(f"\nAll products are relevant to '{search_key}'")

    # def filter_functionality(self):
    #     search_key = 'lip balm'
    #     home = HomePagePage(self.driver)
    #
    #     self.open_url("https://jeevee.com")
    #     time.sleep(2)
    #
    #     home.send_search_input(search_key)
    #     time.sleep(2)

    def test_search_invalid_item(self):
        search_key = 'aqxfv'
        home = NavBar(self.driver)
        item = SearchResultPage(self.driver)

        self.open_url("https://jeevee.com")
        time.sleep(2)

        home.send_search_input(search_key)
        time.sleep(2)
        invalid_item_message=item.get_invalid_item_message()
        logging.info(invalid_item_message)
        time.sleep(2)

