from unittest.mock import *
from pytest_bdd import scenario, given, when, then
import full_retirement_main


# Constants
CURRENT_YEAR = 2020

CONVERTERS = {
    'birth_year': str,
    'birth_month': str,
    'year': str,
    'retire_year': str,
}


class Retirement:
    def __init__(self):
        self.output = ""

    def retire_program(self):
        return full_retirement_main.main()

    def save_output(self, out):
        self.output = out

# Scenarios


@scenario('../features/full_retirement.feature', 'Year too low or high', example_converters=CONVERTERS)
def test_low_high_years():
    pass


@scenario('../features/full_retirement.feature', 'Month too low or high', example_converters=CONVERTERS)
def test_low_high_months():
    pass


@scenario('../features/full_retirement.feature', 'Year and month combo that rolls over', example_converters=CONVERTERS)
def test_rollover():
    pass


# Given / Background

@given('the full_retirement_main program is available', target_fixture='retire_main')
def retire_main():
    return Retirement()


# Whens

@when('the birth year "<year>" is input')
def enter_birth(year, capsys, monkeypatch, retire_main):
    mock_input = Mock()
    mock_input.side_effect = [year, ""]
    monkeypatch.setattr('builtins.input', mock_input)
    retire_main.retire_program()
    out, err = capsys.readouterr()
    retire_main.save_output(out)

@when('the program runs with birth year "<birth_year>" and invalid birth month "<birth_month>"')
def invalid_month(birth_year, birth_month, retire_main, capsys, monkeypatch):
    mock_input = Mock()
    mock_input.side_effect = [birth_year, birth_month, "1", ""]
    monkeypatch.setattr('builtins.input', mock_input)
    retire_main.retire_program()
    out, err = capsys.readouterr()
    retire_main.save_output(out)


@when('the program runs with birth year "<birth_year>" and birth month "<birth_month>"')
def rollover_birth(birth_year, birth_month, retire_main, capsys, monkeypatch):
    mock_input = Mock()
    mock_input.side_effect = [birth_year, birth_month, ""]
    monkeypatch.setattr('builtins.input', mock_input)
    retire_main.retire_program()
    out, err = capsys.readouterr()
    retire_main.save_output(out)


# Thens

@then('program prints: Please enter a valid date between 1900 and 2020')
def reject_year(retire_main):
    assert "Please enter a valid date between 1900 and 2020" in retire_main.output


@then('program prints: Please enter a valid month between 1-12')
def reject_month(retire_main):
    assert "Please enter a valid month between 1-12" in retire_main.output


@then('the month and year of retirement are January of "<retire_year>"')
def rollover_year(retire_main, retire_year):
    assert "January of " + str(retire_year) in retire_main.output
