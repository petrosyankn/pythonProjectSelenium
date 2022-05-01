from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class AmazonCardSectionClass():
    def __init__(self, driver):
        self.driver = driver

    def delete_one_product(self):
        time.sleep(3)
        deleteButton = self.driver.find_element(*AmazonCardSectiondeleteoneproduct)
        deleteButton.click()

    def delete_all_products(self):
        cardCount = self.driver.find_element(*cardPageCartCount)
        numberOfProductsInCard = int(cardCount.text)
        while numberOfProductsInCard > 0:
            deleteButton = self.driver.find_element(*cardPageDeleteButton)
            deleteButton.click()
            numberOfProductsInCard = -1
            time.sleep(2)









