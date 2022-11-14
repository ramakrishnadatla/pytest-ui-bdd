import time
import random
import re
from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class CartPage(Page):
    _add_to_basket_button = (By.XPATH, "(//a[text()='Add to basket'])[1]")
    _view_cart = (By.XPATH, "//a[@class='wpmenucart-contents']")
    _shop_page = (By.XPATH, "//a[text()='Shop']")
    _product_price = (By.XPATH, "(//span[@class='woocommerce-Price-amount amount'])[1]")
    _item_price = (By.XPATH,"//td[@data-title='Total']/span")
    _checkout_button = (By.XPATH, "//a[@class='checkout-button button alt wc-forward']")
    _update_basket_button = (By.XPATH, "//input[@value='Update Basket']")
    _cart_message_box = (By.XPATH, "//div[@class='woocommerce-message']")
    _item_remove_from_cart = (By.XPATH, "//td/a[@class='remove']")
    _subtotal_amount = (By.XPATH, "//tr/th[text()='Subtotal']/following::span[@class='woocommerce-Price-amount "
                                  "amount'][1]")
    _tax_amount = (By.XPATH, "//tr/th[text()='Tax']/following::span[@class='woocommerce-Price-amount amount'][1]")
    _total_amount = (By.XPATH, "//tr/th[text()='Total']/following::span[@class='woocommerce-Price-amount amount'][1]")
    _view_basket = (By.XPATH, "//a[text()='View Basket']")
    _cart_icon = (By.XPATH, "//a[@class='wpmenucart-contents']")
    _cart_quantity_text_field = (By.XPATH, "//input[@class='input-text qty text']")
    _cart_empty_message = (By.XPATH, "//p[@class='cart-empty']")
    _iframe_close_button = (By.XPATH, "//span[text()='Close']")
    _iframe_id = (By.ID, "ad_iframe")

    def __init__(self, driver, base_url=None, timeout=10):
        super(Page, self).__init__(driver, timeout)
        self.base_url = base_url

    def click_on_shop_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._shop_page))
        self.find_element(*self._shop_page).click()

    def click_on_product(self, product: str, driver):
        path = "//img[@title='" + product + "']/following::a[text()='Add to basket'][1]"
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(expected_conditions.visibility_of_element_located(self._add_to_basket_button))
        self.find_element(By.XPATH, path).click()

    def get_product_price(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._item_price))
        message = self.find_element(*self._item_price).text
        value = message[1:]
        return value

    def click_on_add_to_basket(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._add_to_basket_button))
        self.find_element(*self._add_to_basket_button).click()

    def get_cart_action_message(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._cart_message_box))
        message = self.find_element(*self._cart_message_box).text
        return message

    def get_empty_cart_message(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._cart_empty_message))
        message = self.find_element(*self._cart_empty_message).text
        return message

    def click_on_view_basket(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._cart_icon))
        self.find_element(*self._cart_icon).click()

    def user_updated_cart_quantity(self, quantity: str):
        self.wait.until(expected_conditions.visibility_of_element_located(self._cart_quantity_text_field))
        self.find_element(*self._cart_quantity_text_field).clear()
        self.find_element(*self._cart_quantity_text_field).send_keys(quantity)
        self.wait.until(expected_conditions.visibility_of_element_located(self._update_basket_button))
        self.find_element(*self._update_basket_button).click()

    def get_tax_price(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._tax_amount))
        tax = int(self.find_element(*self._tax_amount).text)
        return tax

    def click_on_remove_cart(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self._item_remove_from_cart))
        self.find_element(*self._item_remove_from_cart).click()

    # def get_error_validation_message(self):
    #     try:
    #         self.wait.until(expected_conditions.visibility_of_element_located(self._register_error_message))
    #         message = self.find_element(*self._register_error_message).text
    #     except TimeoutException:
    #         self.wait.until(expected_conditions.visibility_of_element_located(self._password_strength))
    #         message = self.find_element(*self._password_strength).text
    #     return message
