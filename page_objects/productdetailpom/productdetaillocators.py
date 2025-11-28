from selenium.webdriver.common.by import By


class ProductDetailLocators:

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to')]")
    ADDED_TO_CART_TOAST=(By.XPATH,  "//*[contains(text(),'added to the cart successfully') or contains(., 'Added to the cart successfully')]")
