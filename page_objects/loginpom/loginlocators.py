from selenium.webdriver.common.by import By


class LoginLocators:
    MOBILE_NUMBER_FIELD =(By.XPATH,'//*[@id="__next"]/div[6]/div[2]/div/main/div/div[1]/div[2]/div[2]/div[1]/div[1]/input')
    PASSWORD_FILED=(By.XPATH,'//*[@id="__next"]/div[6]/div[2]/div/main/div/div[1]/div[2]/div[2]/div[2]/div[1]/input')
    SIGN_IN_BUTTON=(By.XPATH,'//*[@id="__next"]/div[6]/div[2]/div/main/div/div[1]/div[2]/div[2]/button')
    LOGIN_TOAST=(By.XPATH,"//div[@role='alert']//div[contains(text(),'Login Success')]")
    LOGIN_ERROR_MESSAGE=(By.XPATH,'//*[@id="__next"]/div[6]/div[2]/div/main/div/div[1]/div[2]/div[1]/div')
