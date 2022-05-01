import time
from Locators.LocatorFiles import *
from selenium.webdriver.common.by import By

class FoundItemPageClass():
    def __init__(self, driver):
        self.driver = driver

    def change_location_button(self):
        changeLocationButton = self.driver.finde_element(*FoundItemPageCangeLocationButton)
        changeLocationButton.click()

    def fill_zip_code_filde(self):
        fillZipCodeFilde = self.driver.finde_element(*FoundItemPageFillZipCodeFilde)
        fillZipCodeFilde.send_keys(text)

    def press_zip_code_apply_button(self):
        pressZipCodeApplyButton = self.driver.finde_element(*FoundItemPagePressZipCodeApply)
        pressZipCodeApplyButton.click()

    def press_add_to_card_button(self):
        pressAddToCardButton = self.driver.finde_element(*FoundItemPagePressAddToCard)
        pressAddToCardButton.click()


