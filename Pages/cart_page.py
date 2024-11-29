import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for saucelabs cart page
        self.saulabs_1st_item = (By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
        self.saulabs_2nd_item = (By.XPATH, "(//button[contains(text(),'Add to cart')])[2]")
        self.saulabs_3rd_item = (By.XPATH, "(//button[contains(text(),'Add to cart')])[4]")
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.checkout_button_locator = (By.ID, "checkout")

    def element_click(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            element.click()
            print("Clicked on element with locator")
        except:
            print("Cannot click on the element with locator")

    def add_first_item_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.saulabs_1st_item)
        ).click()

    def add_second_item_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.saulabs_2nd_item)
        ).click()

    def add_third_item_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.saulabs_3rd_item)
        ).click()

    def click_on_cart_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()

    def checkout_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button_locator)
        ).click()

