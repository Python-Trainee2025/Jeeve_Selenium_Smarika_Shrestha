from selenium.webdriver.support.wait import WebDriverWait
from page_objects.searchresultpom.searchresultlocator import SearchResultLocator
from selenium.webdriver.support import expected_conditions as EC

class SearchResultProps(SearchResultLocator):

    @property
    def item_card(self):
        wait = WebDriverWait(self.driver, 8)
        return wait.until(
            EC.presence_of_all_elements_located(SearchResultLocator.ITEM_CARD)
        )

    @property
    def item_name(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(SearchResultLocator.ITEM_NAME)
        )

    @property
    def invalid_item_message(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.presence_of_element_located(SearchResultLocator.INVALID_ITEM_MESSAGE)
        )

    @property
    def searched_product(self):
        wait = WebDriverWait(self.driver, 8)
        return wait.until(
            EC.presence_of_element_located(SearchResultLocator.PRODUCT)
        )




