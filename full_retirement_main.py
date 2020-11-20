from calculate_benefit import *

current_year = 2020

def main():
    birth_year = 0
    birth_month = 0

    print("Social Security Retirement Age Calculator")

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
                        except:
                            print("Please enter a valid month between 1-12")

                    # retirement age
                    needed_months = months_to_retire(birth_year)
                    age_year, age_month = calc_retirement_age(needed_months)
                    print("your full retirement age is {} and {} months".format(age_year, age_month))

                    # name for month
                    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

                    # retirement year and month
                    retire_year, retire_month = calc_date(birth_year, birth_month)
                    print("this will be in {} of {}".format(month_name[retire_month - 1], retire_year))

            except:
                print("Please enter a valid date")


main()
