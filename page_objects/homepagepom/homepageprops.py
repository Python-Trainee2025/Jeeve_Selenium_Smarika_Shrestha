from page_objects.homepagepom.homepageloactors import HomePageLocators


class HomePageProps(HomePageLocators):

    @property
    def user_icon(self):
        return self.driver.find_element(*HomePageLocators.USER_ICON)

    @property
    def login_icon(self):
        return self.driver.find_element(*HomePageLocators.LOGIN_ICON)

