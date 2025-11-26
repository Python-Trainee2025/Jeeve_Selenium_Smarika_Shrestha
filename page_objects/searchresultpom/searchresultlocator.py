from selenium.webdriver.common.by import By


class SearchResultLocator:
    # ITEM_CARD=(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/span[1]')
    # ITEM_NAME=(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/span[1]/div[3]/div[2]')
    ITEM_CARD = (By.XPATH, "//span[contains(@class, 'products_productCard__TgLt6')]")
    ITEM_NAME = (By.XPATH, ".//div[contains(@class, 'text-2-clamp')]")
    INVALID_ITEM_MESSAGE=(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div')

