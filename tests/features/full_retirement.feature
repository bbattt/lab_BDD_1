Feature: Full Retirement Benefits Calculator
  As a currently working person, I want to know what year I will obtain full Social Security Administration benefits.


  Background:
    Given the full_retirement_main program is running

  Scenario Outline: Year too low or high
    When the birth year "<year>" and month "<month>" are input
    Then program prints "Please enter a valid date between 1900 and 2020"
    Examples: Birth Years and Months
      | year | month |
      | 1899 | 1     |
      | 2021 | 1     |


