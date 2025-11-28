from selenium.webdriver.common.by import By

class CartLocators:
    CART_QUANTITY=(By.XPATH, "//div[contains(@class,'w-[26px]') and contains(@class,'text-center')]")
    INCREASE_QUANTITY_BUTTON=(By.CSS_SELECTOR, "div.rounded-full.bg-tPrimary-300.p-1.cursor-pointer:last-of-type")
