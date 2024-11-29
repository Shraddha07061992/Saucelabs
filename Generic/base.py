
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class BaseDriver:
    def __init__(self):
        self.driver = None

    def setup(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def teardown(self):
        # Close the browser
        if self.driver:
            self.driver.quit()
