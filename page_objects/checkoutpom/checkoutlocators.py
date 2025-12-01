from selenium.webdriver.common.by import By


class CheckoutLocators:
    EDIT_ADDRESS_BTN=(By.XPATH,"//button[normalize-space(text())='Edit' and contains(@class,'btn-primary')]")
    EDIT_PHONE_NUMBER=(By.XPATH,"//input[@name='phone' and @placeholder='Enter Alternate Number']")
    UPDATE_ADDRESS=(By.XPATH,"//button[normalize-space(text())='Update Address' and contains(@class,'btn-primary')]")
    ALTERNATE_NUMBER=(By.XPATH,"//div[contains(text(),'Alternate No.')]")
