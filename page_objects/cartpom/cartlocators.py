from selenium.webdriver.common.by import By

class CartLocators:
    CART_QUANTITY=(By.XPATH, "//div[contains(@class,'w-[26px]') and contains(@class,'text-center')]")
    INCREASE_QUANTITY_BUTTON=(By.CSS_SELECTOR, "div.rounded-full.bg-tPrimary-300.p-1.cursor-pointer:last-of-type")
    REMOVE_ITEM_BUTTON=(By.XPATH, "//button[contains(@class,'cursor-pointer') and .//svg]")
    CHECKOUT_BUTTON=(By.XPATH,"//button[contains(text(),'Checkout')]")
    ADDED_TO_CART_TOAST=(By.XPATH,"//div[@role='alert']//div[text()='Added to the cart successfully']")


