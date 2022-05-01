import time
from Locators.LocatorFiles import *
from selenium.webdriver.common.by import By

class SearchResultPageClass():
    def __init__(self, driver):
        self.driver = driver

    def scroll (self):
         time.sleep(4)
         self.driver.execute_script("window.scrollto(0, 0)")

    def finde_certain_item_button(self):
        findeCertainItemButton = self.driver.finde_element(*SearchResultPagefindecertainitembutton)
        findeCertainItemButton.click()


