import time
import unittest
from selenium import webdriver
from Pages.MainPage import MainPageClass
from Pages.MyAccountHomePage import MyAccountHomePageClass
from Pages.AmazonCardSection import AmazonCardSectionClass
from Pages.AmazonItemSearchField import AmazonItemSearchFieldClass
from Pages.SearchResultPage import SearchResultPageClass
from Pages.FoundItemPage import FoundItemPageClass




class AmazonSimpleTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        self.MyAccountHomePage = MyAccountHomePageClass(self.driver)
        self.AmazonCardSection = AmazonCardSectionClass(self.driver)
        self.AmazonItemSearchField = AmazonItemSearchFieldClass(self.driver)
        self.SearchResultPage = SearchResultPageClass(self.driver)
        self.FoundItemPage = FoundItemPageClass(self.driver)



    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/")
        self.mainPage.press_amazon_SignIn_account_Button()
        self.mainPage.fill_signin_field("kimkrugeractress@gmail.com")

        time.sleep(4)
        self.mainPage.press_amazon_continue_Button()

        time.sleep(3)
        self.mainPage.fill_password_field("kim2002++")

        time.sleep(5)
        self.mainPage.press_amazon_checkbox_field()

        time.sleep(5)
        self.mainPage.press_amazon_SignIn_Button()

        time.sleep(5)
        self.MyAccountHomePage.press_amazon_bucket_Button()

        time.sleep(3)
        self.AmazonCardSection.delete_one_product()

        time.sleep(3)
        self.AmazonItemSearchField.fill_item_search_field("jbl bluetooth headphones")

        time.sleep(3)
        self.AmazonItemSearchField.press_item_search_button()

        time.sleep(2)
        self.SearchResultPage.scroll("window.scrollto(0, 0)")

        time.sleep(3)
        self.SearchResultPage.finde_certain_item_button()

        time.sleep(3)
        self.FoundItemPage.change_location_button()

        time.sleep(3)
        self.FoundItemPage.fill_zip_code_filde("19701")

        time.sleep(3)
        self.FoundItemPage.press_zip_code_apply_button()

        time.sleep(3)
        self.FoundItemPage.press_add_to_card_button()





    def tearDown(self):
        time.sleep(4)
        self.driver.close()