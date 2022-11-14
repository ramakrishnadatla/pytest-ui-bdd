import time

from pypom import page
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.remote.webdriver import WebDriver

from test.pages.registration.registration_page import RegistrationPage

scenarios('../../features/registration/registration.feature')


@given('User opened Registration url page', target_fixture='registration_target')
def user_is_on_landing_page(driver: WebDriver, base_url) -> page:
    driver.maximize_window()
    driver.get(base_url)
    return RegistrationPage(driver)


@when(parsers.parse("user enters email <email>"))
@when(parsers.parse("user enters email {email}"))
def user_enters_email(registration_target, email: str):
    registration_target.enter_email_address(email)


@when(parsers.parse("user enters password <password>"))
@when(parsers.parse("user enters password {password}"))
def user_enters_password(registration_target, password):
    registration_target.enter_password(password)


@when("click on register button")
def click_on_login_button(registration_target):
    registration_target.click_on_register_button()


@then(parsers.parse("a valid registration message <message> should be displayed"))
def get_validation_message(registration_target, message):
    assert message in registration_target.get_login_validation_message()


@then(parsers.parse("a valid registration error message <message> should be displayed"))
def get_error_validation_message(registration_target, message):
    assert message in registration_target.get_error_validation_message()


@then("user logged out")
def click_on_logout_button(registration_target):
    registration_target.click_on_logout_button()