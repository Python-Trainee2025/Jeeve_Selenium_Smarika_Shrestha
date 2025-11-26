from page_objects.homepagepom.homepageloactors import HomePageLocators


class HomePageProps(HomePageLocators):

    @property
    def user_icon(self):
        return self.driver.find_element(*HomePageLocators.USER_ICON)

    @property
    def login_icon(self):
        return self.driver.find_element(*HomePageLocators.LOGIN_ICON)

    @property
    def search_input_filed(self):
        return self.driver.find_element(*HomePageLocators.SEARCH_INPUT_FILED)

    @property
    def item_card(self):
        return self.driver.find_elements(*HomePageLocators.ITEM_CARD)

