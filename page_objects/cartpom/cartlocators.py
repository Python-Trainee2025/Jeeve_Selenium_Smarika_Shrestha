from selenium.webdriver.common.by import By

class CartLocators:
    CART_QUANTITY=(By.XPATH, "//div[contains(@class,'w-[26px]') and contains(@class,'text-center')]")
    INCREASE_QUANTITY_BUTTON=(By.CSS_SELECTOR, "div.rounded-full.bg-tPrimary-300.p-1.cursor-pointer:last-of-type")
    REMOVE_ITEM_CROSS_BUTTON=(By.XPATH,
                          "//button[contains(@class,'cursor-pointer') and .//span[contains(@class,'text-error-500')]]")
    REMOVE_ITEM_BUTTON=(By.XPATH,"//button[normalize-space(text())='Remove' and contains(@class,'btn-secondary')]")
    REMOVE_ITEM_TOAST=(By.XPATH,"//div[contains(text(),'Successfully removed the product from cart.')]")
    CHECKOUT_BUTTON=(By.XPATH,"//button[contains(text(),'Checkout')]")
    ADDED_TO_CART_TOAST=(By.XPATH,"//div[@role='alert']//div[text()='Added to the cart successfully']")
    EMPTY_CART=(By.XPATH,"//p[contains(text(),'no items') or contains(text(),'empty')]")
    DECREASE_QUANTITY_BUTTON= (By.XPATH,"//div[contains(@class,'space-x-3')]/div[1][contains(@class,'rounded-full')]")
    # GRAND_TOTAL=(By.XPATH, "//div[contains(@class,'font-bold') and contains(text(),'Rs')]")
    # GRAND_TOTAL=(By.XPATH,"//div[contains(@class,'font-bold') and contains(text(),'Rs')]")
    GRAND_TOTAL=(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[3]/div/div[2]')
    PRICE_PER_ITEM=(By.XPATH,"//span[contains(@class,'text-primary-500') and contains(text(),'Rs.')]")
    CART_ITEM_TITLE = (By.XPATH,
                       "//div[contains(@class,'bg-white') and contains(@class,'border-b')]//div[contains(@class,'text-sm') and contains(@class,'text-base')]")


