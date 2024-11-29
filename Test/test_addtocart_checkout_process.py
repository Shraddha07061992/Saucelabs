import unittest

from Webapp.Saucelabs.Assertion.Validate_last_page import ThankspageAssertion
from Webapp.Saucelabs.Generic.base import BaseDriver
from Webapp.Saucelabs.Pages.checkout_process_page import CheckoutProcessPage
from Webapp.Saucelabs.Pages.login_page import LoginPage
from Webapp.Saucelabs.Pages.cart_page import CartPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Setup the driver
        self.base_driver = BaseDriver()
        self.base_driver.setup()

        # Create object
        self.login_page = LoginPage(self.base_driver.driver)
        self.cart_page = CartPage(self.base_driver.driver)
        self.checkout_process_page = CheckoutProcessPage(self.base_driver.driver)
        self.assertionthanksmessage = ThankspageAssertion(self.base_driver.driver)

    def test_addtocart_checkoutprocess(self):
        # Step 1: Open saucedemo login page
        self.base_driver.driver.get("https://www.saucedemo.com/")
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login_button()
        print("Login successful!")
        # step 2 : Assertion for login page
        self.assertionthanksmessage.loginsucessMessage()
        # Step 3: Add 3 items to cart
        self.cart_page.add_first_item_to_cart()
        self.cart_page.add_second_item_to_cart()
        self.cart_page.add_third_item_to_cart()
        # Step 4: click on cart
        self.cart_page.click_on_cart_icon()
        # Step 5: Assertion for cart page
        self.assertionthanksmessage.yourcartvalidation()
        self.cart_page.checkout_button()
        # Step 6: Assertion for checkout process page
        self.assertionthanksmessage.checkoutprocessvalidation()
        # Step 7: checkout process
        self.checkout_process_page.enter_firstname("shraddha")
        self.checkout_process_page.enter_lastname("Aher")
        self.checkout_process_page.enter_postaladdress("b1-1206")
        self.checkout_process_page.click_continue_button()
        self.checkout_process_page.click_finish_button()
        # step 8 : Assertion for order placed
        self.assertionthanksmessage.thankyouMessage()
        print("order placed!")

    def tearDown(self):
        # Cleanup after test
        self.base_driver.teardown()