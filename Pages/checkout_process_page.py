from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators for saucelabs checkout cart page
        self.firstname_input_locator = (By.ID, "first-name")
        self.lastname_input_locator = (By.ID, "last-name")
        self.postal_input_locator = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.selector_thanks_message = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")
        self.selector_loginsucess_validation = (By.XPATH, "//div[contains(text(),'Swag Labs')]")
        self.selector_yourcart_validation = (By.XPATH, "//span[contains(text(),'Your Cart')]")
        self.selector_checkout_validation = (By.XPATH, "//span[contains(text(),'Checkout: Your Information')]")


    def enter_firstname(self, firstname):
        firstname_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.firstname_input_locator)
        )
        firstname_input.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.lastname_input_locator)
        )
        lastname_input.send_keys(lastname)

    def enter_postaladdress(self, postalcode):
        postalcode_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_input_locator)
        )
        postalcode_input.send_keys(postalcode)

    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()

    def click_finish_button(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        )
        finish_button.click()

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
        )
        return element.text
