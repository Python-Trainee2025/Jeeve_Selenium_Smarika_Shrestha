from selenium.webdriver.common.by import By


class ProductDetailLocators:
    PRODUCT_HOMEPAGE=(By.XPATH, "//span[contains(@class,'products_productCard')]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    ADDED_TO_CART_TOAST=(By.XPATH,  "//*[contains(text(),'added to the cart successfully') or contains(., 'Added to the cart successfully')]")
    STOCK_IDENTIFIER=(By.XPATH,"//div[contains(text(),'Stock')]")
