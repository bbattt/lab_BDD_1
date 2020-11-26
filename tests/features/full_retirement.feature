Feature: Full Retirement Benefits Calculator
  As a currently working person, I want to know what year I will obtain full Social Security Administration benefits.


  Background:
    Given the full_retirement_main program is available


  Scenario: Non digit year
    When nondigit birth year "A" is input
    Then program prints: Please enter a numerical date between 1900 and 2020


  Scenario: Non digit month
    When birth year "1900" and nondigit birth month "A" are input
    Then program prints: Please enter a numerical month between 1-12


  Scenario Outline: Year too low or high
    When the birth year "<year>" is input
    Then program prints: Please enter a valid date between 1900 and 2020

    Examples: Birth Years and Months
      | year |
      | 1899 |
      | 2021 |


  Scenario Outline: Month too low or high
    When the program runs with birth year "<birth_year>" and invalid birth month "<birth_month>"
    Then program prints: Please enter a valid month between 1-12

    Examples: Birth Year 1900 and Invalid Months
      | birth_year | birth_month |
      | 1900       | 0           |
      | 1900       | 13          |


  Scenario Outline: Year and month combo that rolls over
    When the program runs with birth year "<birth_year>" and birth month "<birth_month>"
    Then the month and year of retirement are January of "<retire_year>"

    Examples: Birth and Retire Years and Months
      | birth_year | birth_month | retire_year |
      | 1900       | 1           | 1965        |
      | 1938       | 11          | 2004        |
      | 1939       | 9           | 2005        |
      | 1940       | 7           | 2006        |
      | 1941       | 5           | 2007        |
      | 1942       | 3           | 2008        |
      | 1943       | 1           | 2009        |
      | 1954       | 1           | 2020        |
      | 1955       | 11          | 2022        |
      | 1956       | 9           | 2023        |
      | 1957       | 7           | 2024        |
      | 1958       | 5           | 2025        |
      | 1959       | 3           | 2026        |
      | 1960       | 1           | 2027        |