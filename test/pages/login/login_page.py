import time

from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class HomePage(Page):
    _email_address = (By.XPATH, "//input[@id='username']")
    _password = (By.XPATH, " //input[@id='password']")
    _login_button = (By.XPATH, "//input[@name='login']")
    _login_myAccount_button = (By.XPATH, "//a[contains(text(),'My Account')]")
    _login_error_message = (By.XPATH, "//ul[@class='woocommerce-error']")
    _login_success_message = (By.XPATH,"//div[@class='woocommerce-MyAccount-content']")

    def __init__(self, driver, base_url=None, timeout=10):
        super(Page, self).__init__(driver, timeout)
        self.base_url = base_url

    def click_on_a_button_to_enable_login_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._login_myAccount_button))
        self.find_element(*self._login_myAccount_button).click()

    def enter_email_address(self, email: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._email_address))
        self.find_element(*self._email_address).send_keys(email)

    def enter_password(self, password: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._password))
        self.find_element(*self._password).send_keys(password)

    def user_enters_reset_password(self, reset_password: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._password))
        self.find_element(*self._password).send_keys(reset_password)

    def click_on_login_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._login_button))
        self.find_element(*self._login_button).click()

    def login(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        self.click_on_login_button()
        self.wait.until(expected_conditions.invisibility_of_element(self._login_button))

    def click_cart_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._cart_button))
        self.find_element(*self._cart_button).click()
        self.wait.until(expected_conditions.invisibility_of_element(self._cart_button))

    def click_logout_button(self):
        self.wait.until(expected_conditions.invisibility_of_element(self._cart_button))
        self.find_element(*self._loggedIn_name).click()
        self.find_element(*self._logout_button).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self._login_button))

    def get_login_validation_message(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._login_success_message))
        message = self.find_element(*self._login_success_message).text
        return message

    def get_error_validation_message(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._login_error_message))
        message = self.find_element(*self._login_error_message).text
        return message

