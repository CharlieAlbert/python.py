# function that checks if the year is leap or not

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """ Return true for leap years and false for non-leap years """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month, year):
    if not 1 <= month <= 12:
        return 'invalid month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2020))
print(days_in_month(2, 2020))
