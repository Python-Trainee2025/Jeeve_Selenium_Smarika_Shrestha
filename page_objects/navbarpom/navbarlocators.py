from selenium.webdriver.common.by import By


class NavBarLocators:
    # USER_ICON=(By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]')
    # LOGIN_ICON=(By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div[10]')
    # SEARCH_INPUT_FIElD=(By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/div/input')
    CART_ICON=(By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[2]')
    SEARCH_INPUT_FIElD=(By.XPATH,"//input[@placeholder='Search for Products, Medicine...']")
    USER_ICON = (By.XPATH, "//div[contains(@class, 'user_greetings__')]")

    LOGIN_ICON= (By.XPATH, "//div[contains(@class, 'cursor-pointer')]//div[text()='Login']/..")