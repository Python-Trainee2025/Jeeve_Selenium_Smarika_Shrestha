from selenium.webdriver.common.by import By


class LoginLocators:
    MOBILE_NUMBER_FIELD =(By.XPATH,"//input[@name='phone' and @placeholder='Mobile Number *']")
    PASSWORD_FILED=(By.XPATH,"//input[@type='password' and @name='password' and @placeholder='Password *']")
    SIGN_IN_BUTTON=(By.XPATH,"//button[normalize-space(text())='Sign In' and contains(@class,'btn-primary')]")
    LOGIN_TOAST=(By.XPATH,"//div[@role='alert']//div[contains(text(),'Login Success')]")
    LOGIN_ERROR_MESSAGE=(By.XPATH,"//div[normalize-space()='Username and Password not matching']")
