import pytest
from pytest_bdd import scenarios, parsers, given, when, then
import full_retirement_main

# Constants
CURRENT_YEAR = 2020

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'year': int,
    'month': int,
}


@scenarios('../features/full_retirement.feature', example_converters=CONVERTERS)


@given('the full_retirement_main program is running')
def retire_main():
    return full_retirement_main


@when('the birth year "<year>" and month "<month>" are input', extra_types=EXTRA_TYPES)
def enter_birth(retire_main, year, month, capsys):
    input_nums = [year, month]

    def mock_input(s):
        return input_nums.pop(0)

    retire_main.input = mock_input

    retire_main.main()

    captured = capsys.readouterr()
    return captured.out


@then('program prints: Please enter a valid date between 1900 and 2020')
def reject_year(enter_birth):
    assert
