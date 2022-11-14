import time
import random
import re
from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class CONSTANT:
    alreadyRegisteredEmail = "alreadyregistered@gmail.com"


def getEmailWithRandomNumber(email: str):
    return email.split('@')[0] + str(random.randint(0, 999)) + '@' + email.split('@')[1]


def checkValidEmailFormat(email: str):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, email):
        return True
    return False


class RegistrationPage(Page):
    _email_address = (By.XPATH, "//input[@id='reg_email']")
    _password = (By.XPATH, "//input[@id='reg_password']")
    _register_button = (By.XPATH, "//input[@name='register']")
    _register_error_message = (By.XPATH, "//ul[@class='woocommerce-error']")
    _register_success_message = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p[2]")
    _logout_button = (By.XPATH, "//a[text()='Logout']")
    _signOut_button = (By.XPATH, "//a[text()='Sign out']")
    _password_hint = (By.XPATH, "//small[@class='woocommerce-password-hint']")
    _password_strength = (By.XPATH,"//div[contains(@class,'woocommerce-password-strength')]")

    def __init__(self, driver, base_url=None, timeout=10):
        super(Page, self).__init__(driver, timeout)
        self.base_url = base_url

    def enter_email_address(self, email: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._email_address))

        if checkValidEmailFormat(email) and email != CONSTANT.alreadyRegisteredEmail:
            emailWithRandomNumber = getEmailWithRandomNumber(email)
        else:
            emailWithRandomNumber = email
        self.find_element(*self._email_address).send_keys(emailWithRandomNumber)

    def enter_password(self, password: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._password))
        self.find_element(*self._password).send_keys(password)

    def user_enters_reset_password(self, reset_password: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._password))
        self.find_element(*self._password).send_keys(reset_password)

    def click_on_register_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._register_button))
        self.find_element(*self._register_button).click()

    def click_on_logout_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._logout_button))
        self.find_element(*self._logout_button).click()

    def click_logout_button(self):
        self.wait.until(expected_conditions.invisibility_of_element(self._signOut_button))
        self.find_element(*self._logout_button).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self._register_button))

    def get_login_validation_message(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._register_success_message))
        message = self.find_element(*self._register_success_message).text
        return message

    def get_error_validation_message(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self._register_error_message))
            message = self.find_element(*self._register_error_message).text
        except TimeoutException:
            self.wait.until(expected_conditions.visibility_of_element_located(self._password_strength))
            message = self.find_element(*self._password_strength).text
        return message
