

# Date is given in a "dd-mm-yyyy" format, e.g. 17-04-2018.
# We calculate the weight of that date, by taking all of its digits, multiplying each digit
# with the ones after it, and finally summing up all the results obtained.
# In our case, we have 8 digits: 17032007, so the (weight is
# 1*7 + 1*0 + 1*3 + 1*2 + 1*0 + 1*0 + 1*7 + 7*0 + 7*3 + 7*2 + 7*0 + 7*0 + 7*7 + 0*3 + 0*2 +
# 0*0 + 0*0 + 0*7 + 3*2 + 3*0 + 3*0 + 3*7 + 2*0 + 2*0 + 2*7 + 0*0 + 0*7 + 0*7) = 144.
#
# Our task is to write a program that finds all the magical dates between two specific years
# (inclusively) corresponding to the given weight. Dates must be printed in ascending order
# (by date) in the format "dd-mm-yyyy". We will only use the valid dates in the traditional
# calendar (the leap years have 29 days in February).

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28


def calculate_weight(date_str):
    digits = [int(x) for x in date_str]
    weight = 0

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            weight += digits[i] * digits[j]

    return weight


def find_magical_dates(start_year, end_year, target_weight):
    found = False

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            days = get_days_in_month(month, year)

            for day in range(1, days + 1):
                date_str = f"{day:02d}{month:02d}{year}"
                weight = calculate_weight(date_str)

                if weight == target_weight:
                    print(f"{day:02d}-{month:02d}-{year}")
                    found = True


    if not found:
        print("No")


find_magical_dates(2000, 2020, 144)