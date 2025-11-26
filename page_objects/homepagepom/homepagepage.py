from page_objects.homepagepom.homepageprops import HomePageProps


class HomePagePage(HomePageProps):

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.user_icon.click()
        self.login_icon.click()


