Feature: Login, Add Cart , Update Cart , Remove Cart Test Scenarios to https://practice.automationtesting.in

  @nondestructive @all @shop @cart
  Scenario Outline: 1. Login, Add Cart , Update Cart , Remove Cart Test
    Given user opened base url page
    When user logged in with email varmasdatla12@gmail.com and password Test1@Auto
    And user clicked on shop page
    And user clicked on product <product> item
    And user clicked on view basket button
    And the verify price <price> value displayed
    And updated cart items to 2
    Then verify Basket updated. message is displayed
    When user removed all cart items
    Then verify Your basket is currently empty. message is displayed in ui

    Examples:
      | product              | price |
      | Mastering JavaScript | 350   |
      | Selenium Ruby        | 500   |