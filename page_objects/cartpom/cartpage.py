from page_objects.cartpom.cartprops import CartProps


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver = driver

    def increase_item_quantity(self):
        self.increase_quantity.click()

    def read_cart_quantity(self):
        return self.cart_quantity.text