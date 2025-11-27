from selenium.webdriver.support.wait import WebDriverWait

from page_objects.searchresultpom.searchresultlocator import SearchResultLocator
from page_objects.searchresultpom.searchresultprops import SearchResultProps



class SearchResultPage(SearchResultProps):
    def __init__(self, driver):
        self.driver = driver

    def get_all_product_names(self):
        names = []
        for card in self.item_card:
            name = card.find_element(
                *SearchResultLocator.ITEM_NAME
            ).text
            names.append(name)
        return names

    def get_invalid_item_message(self):
        message=self.invalid_item_message.text
        return message

    def get_product(self):
        self.searched_product.click()
