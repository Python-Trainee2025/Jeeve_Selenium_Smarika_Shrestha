from page_objects.navbarpom.navbarlocators import NavBarLocators


class NavBarProps(NavBarLocators):

    @property
    def user_icon(self):
        return self.driver.find_element(*NavBarLocators.USER_ICON)

    @property
    def login_icon(self):
        return self.driver.find_element(*NavBarLocators.LOGIN_ICON)

    @property
    def search_input_field(self):
        return self.driver.find_element(*NavBarLocators.SEARCH_INPUT_FIElD)

    # @property
    # def item_card(self):
    #     return self.driver.find_elements(*NavBarLocators.ITEM_CARD)

    @property
    def cart_icon(self):
        return self.driver.find_element(*NavBarLocators.CART_ICON)


