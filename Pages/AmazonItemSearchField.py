import time
from Locators.LocatorFiles import *
from selenium.webdriver.common.by import By

class AmazonItemSearchFieldClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_item_search_field(self, text):
        time.sleep(3)
       # searchField.clear()
        searchField = self.driver.find_element(*AmazonItemSearchFieldfillitemsearchfield)
        searchField.send_keys(text)

    def press_item_search_button(self):
        amazonItemSearchButton = self.driver.find_element(*AmazonItemSearchFieldpressitemsearchbutton)
        amazonItemSearchButton.click()





