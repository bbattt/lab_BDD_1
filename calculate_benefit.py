def months_to_retire(y: int):
    """
    Uses birth year to determine number of years until retirement age.
    :param y: an int of the birth year
    :return: months
    """
    months = 65 * 12  # the minimum number of months
    if y <= 1937:
        months = months
    elif y <= 1938:
        months += 2
    elif y <= 1939:
        months += 4
    elif y <= 1940:
        months += 6
    elif y <= 1941:
        months += 8
    elif y <= 1942:
        months += 10
    elif 1943 <= y <= 1954:
        months += 12
    elif y <= 1955:
        months += 14
    elif y <= 1956:
        months += 16
    elif y <= 1957:
        months += 18
    elif y <= 1958:
        months += 20
    elif y <= 1959:
        months += 22
    else:
        months += 24
    return months


def calc_retirement_age(months: int):
    """
    Finds the age of full retirement in years and months
    :param months: number of months until retirement
    :return: age year, age months
    """
    total_months = months
    years = total_months // 12
    remaining_months = total_months % 12
    return years, remaining_months


def calc_date(y: int, m: int):
    """
    Uses months_to_retire and calc_retirement_age to find the date full retirement age is reached.
    :param y: an int of the birth year
    :param m: an int of the birth month
    :return: year, month
    """
    birth_year = y
    birth_month = m

    total_months = months_to_retire(birth_year)
    years_to_add, months_to_add = calc_retirement_age(total_months)

    # find retirement year
    retire_year = birth_year + years_to_add

    # find retirement month, correct year if needed
    retire_month = birth_month + months_to_add
    if retire_month > 12:
        retire_year += 1
        retire_month = 12 - retire_month

    return retire_year, retire_month
