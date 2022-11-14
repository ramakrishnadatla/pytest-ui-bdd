import time

from pypom import page
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.remote.webdriver import WebDriver

from test.pages.login.login_page import HomePage

scenarios('../../features/login/home_login.feature')


@given('user opened base url page', target_fixture='login_target')
def user_is_on_landing_page(driver: WebDriver, base_url) -> page:
    driver.maximize_window()
    driver.get(base_url)
    return HomePage(driver)


@when("user clicked on login button")
def click_on_login_button(login_target):
    login_target.click_on_login_button()


@when(parsers.parse("user enters email <email>"))
@when(parsers.parse("user enters email {email}"))
def user_enters_email(login_target, email: str):
    login_target.enter_email_address(email)


@when(parsers.parse("user enters password <password>"))
@when(parsers.parse("user enters password {password}"))
def user_enters_password(login_target, password):
    login_target.enter_password(password)


@when("click on login button")
def click_on_login_button(login_target):
    login_target.click_on_login_button()


@then(parsers.parse("a valid login message <message> should be displayed"))
def get_validation_message(login_target, message):
    assert message in login_target.get_login_validation_message()


@then(parsers.parse("a valid error message <message> should be displayed"))
def get_error_validation_message(login_target, message):
    assert message in login_target.get_error_validation_message()