Feature: Login to https://practice.automationtesting.in

  @nondestructive @all @negative @login @loginNegative
  Scenario Outline: 1. Login Negative Test Scenarios
    Given user opened base url page
    When user enters email <email>
    And user enters password <password>
    And click on login button
    Then a valid error message <message> should be displayed

    Examples:
      | email                    | password | message                                                                         |
      | varmasdatla123@gmail.com | dummy    | the password you entered for the username varmasdatla123@gmail.com is incorrect |
      | aeeaeaeae@gmail.com      | dummy    | A user could not be found with this email address                               |
      |                          | password | Username is required                                                            |
      | abc                      |          | Password is required                                                            |

  @nondestructive @all @positive @login @loginPositive
  Scenario Outline: 2. Login Positive Test Scenarios
    Given user opened base url page
    When user enters email <email>
    And user enters password <password>
    And click on login button
    Then a valid login message <message> should be displayed

    Examples:
      | email                   | password   | message        |
      | varmasdatla12@gmail.com | Test1@Auto | varmasdatla12 |