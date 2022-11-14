Feature: Registration to https://practice.automationtesting.in

  @nondestructive @all @negative @registration @registrationNegative
  Scenario Outline: 1. Registration Negative Test Scenarios
    Given User opened Registration url page
    When user enters email <email>
    And user enters password <password>
    And click on register button
    Then a valid registration error message <message> should be displayed

    Examples:
      | email                       | password     | message                                                                |
      | alreadyregistered@gmail.com | abcd7@efghij | An account is already registered with your email address. Please login |
      |                             |              | Please provide a valid email address                                   |
      | aeeaeaeae@gmail.com         |              | Please enter an account password                                       |
      | aeeaeaeae@gmail.com         | pas          | Very weak - Please enter a stronger password                           |
      | aeeaeaeae@gmail.com         | passwo       | Weak - Please enter a stronger password                                |
      | abcdegh                     | Rama$123@    | Medium                                                                 |

  @nondestructive @all @positive @registration @registrationPositive
  Scenario Outline: 2. Registration Positive Test Scenarios
    Given User opened Registration url page
    When user enters email <email>
    And user enters password <password>
    And click on register button
    Then a valid registration message <message> should be displayed
    Then user logged out

    Examples:
      | email                 | password     | message                                                                                                                                            |
      | varmasdatla12@gmail.com | Test1@Auto | From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details |
      | varmasdatla@gmail.com | varmasdatla@gmail.com | From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details |