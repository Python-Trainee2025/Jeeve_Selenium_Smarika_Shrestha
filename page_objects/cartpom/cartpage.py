from page_objects.cartpom.cartprops import CartProps



class CartPage(CartProps):
    def __init__(self, driver):
        self.driver = driver

    def increase_item_quantity(self):
        self.increase_quantity.click()

    def read_cart_quantity(self):
        return self.cart_quantity.text

    # def remove_cart_item(self):
    #     self.remove_item_button.click()


    # def checkout_of_cart(self):
    #     element = self.checkout_button
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     element.click()





