import time

from pypom import page
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.remote.webdriver import WebDriver

from test.pages.cart.cart_page import CartPage
from test.pages.login.login_page import HomePage

scenarios('../../features/cart/cart_add.feature')


@given('user opened base url page', target_fixture='home_page')
def user_is_on_landing_page(driver: WebDriver, base_url) -> page:
    driver.maximize_window()
    driver.get(base_url)
    return HomePage(driver)


@when(parsers.parse("user logged in with email <email> and password <password>"), target_fixture='cart_page')
@when(parsers.parse("user logged in with email {email} and password {password}"), target_fixture='cart_page')
def user_enters_email(home_page, driver: WebDriver, email: str, password: str):
    home_page.login(email, password)
    return CartPage(driver)


@when("user clicked on shop page")
def click_on_shop_button(cart_page, base_url, driver: WebDriver):
    cart_page.click_on_shop_page()
    driver.get(base_url + "/shop/")


@when(parsers.parse("user clicked on product <product> item"))
def click_on_shop_button(cart_page, product: str, driver: WebDriver):
    cart_page.click_on_product(product, driver)


@when(parsers.parse("the verify price <price> value displayed"))
def get_validation_message(cart_page, price: str):
    assert price in cart_page.get_product_price()


@when("user clicked on Add to Basket button")
def click_on_shop_button(cart_page):
    cart_page.click_on_add_to_basket()


@when(parsers.parse("verify product <product> added displayed in UI"))
def get_validation_message(cart_page, product: str):
    product_message = "\"" + product + "\" has been added to your basket"
    assert product_message in cart_page.get_product_price()


@when("user clicked on view basket button")
def click_on_view_cart_button(cart_page):
    cart_page.click_on_view_basket()


@then(parsers.parse("verify the total price along with tax <tax>"))
def verify_total_price_with_tax(cart_page, tax: int):
    assert tax == cart_page.get_tax_price()


@when(parsers.parse("updated cart items to {quantity}"))
def update_cart_quantity(cart_page, quantity: str, base_url, driver: WebDriver):
    driver.get(base_url + "/basket/")
    cart_page.user_updated_cart_quantity(quantity)


@when("user removed all cart items")
def click_on_remove_cart_button(cart_page):
    cart_page.click_on_remove_cart()


@then(parsers.parse("verify {message} message is displayed"))
def verify_message_is_displayed(cart_page, message: str):
    assert message in cart_page.get_cart_action_message()


@then(parsers.parse("verify {emptyCartMessage} message is displayed in ui"))
def verify_message_is_displayed_in_ui(cart_page, emptyCartMessage: str):
    assert emptyCartMessage in cart_page.get_empty_cart_message()
