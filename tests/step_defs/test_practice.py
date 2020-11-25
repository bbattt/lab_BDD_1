import pytest
from unittest import mock
from unittest.mock import *
from nose.tools import *
import io
#from full_retirement_main import main
import mock
from calculate_benefit import *

'''
def foo():
    print("Something")


@patch('sys.stdout', new_callable=io.StringIO)
def test_foo_one(mock_stdout):
    foo()
    assert mock_stdout.getvalue() == 'Something\n'
'''


def practice():
    birth_year = True
    while birth_year is not False:
        input_year = input("Enter year of to exit")
        if input_year == "":
            birth_year = False
        else:
            print("Please enter a valid date between 1900 and 2020")


def full_practice():
    birth_year = True
    current_year = 2020
    while birth_year is not False:
        # reset birth_year and birth_month
        birth_year = 0
        birth_month = 0

        input_year = input("\nEnter the year of birth or to exit ")
        if input_year == "":
            birth_year = False
        else:
            try:
                birth_year = int(input_year)
                if birth_year < 1900 or birth_year > current_year:
                    print("Please enter a valid date between 1900 and {}".format(current_year))
                else:
                    while birth_month == 0:
                        input_month = input("Enter the month of birth ")
                        try:
                            birth_month = int(input_month)
                            if birth_month < 1 or birth_month > 12:
                                birth_month = 0
                        except ValueError:
                            print("Please enter a valid month between 1-12")

                    # retirement age
                    needed_months = months_to_retire(birth_year)
                    age_year, age_month = calc_retirement_age(needed_months)
                    print("your full retirement age is {} and {} months".format(age_year, age_month))

                    # name for month
                    month_name = ["not a month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

                    # retirement year and month
                    retire_year, retire_month = calc_date(birth_year, birth_month)
                    print("this will be in {} of {}".format(month_name[retire_month], retire_year))

            except ValueError:
                print("Please enter a valid date")


# @when('the birth year "<year>" is input', extra_types=EXTRA_TYPES)
def test_enter_birth(capsys, monkeypatch):
    year = "1899"
    mock_input = Mock()
    mock_input.side_effect = [year, ""]
    monkeypatch.setattr('builtins.input', mock_input)
    full_practice()
    output = capsys.readouterr()
    assert output.out == "Please enter a valid date between 1900 and 2020\n"


'''
def test_mock():
    mock = Mock()
    mock.side_effect = [3, 2, 1]
    assert mock() == 3
    assert mock() == 2
    assert mock() == 1
'''