from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for saucelabs login page
        self.username_input_locator = (By.ID, "user-name")
        self.password_input_locator = (By.NAME, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input_locator)
        )
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input_locator)
        )
        password_input.send_keys(password)

    def click_login_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        next_button.click()
