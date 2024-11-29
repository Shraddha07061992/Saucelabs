import time
from Webapp.Saucelabs.Pages.checkout_process_page import CheckoutProcessPage

class ThankspageAssertion(CheckoutProcessPage):
    def thankyouMessage(self):
        thanks_message = 'Thank you for your order!'
        time.sleep(1)
        assert thanks_message == self.get_text(self.selector_thanks_message)

    def loginsucessMessage(self):
        loginsucess_message = 'Swag Labs'
        time.sleep(1)
        assert loginsucess_message == self.get_text(self.selector_loginsucess_validation)

    def yourcartvalidation(self):
        yourcart_validation = 'Your Cart'
        time.sleep(1)
        assert yourcart_validation == self.get_text(self.selector_yourcart_validation)

    def checkoutprocessvalidation(self):
        checkoutprocess_validation = 'Checkout: Your Information'
        time.sleep(1)
        assert checkoutprocess_validation == self.get_text(self.selector_checkout_validation)
