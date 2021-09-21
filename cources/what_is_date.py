import os

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    d31 = [1, 3, 5, 7, 8, 10, 12]
    if month != 2 and month in d31:
        return 31
    elif month != 2:
        return 30
    elif is_year_leap(year):
        return 29
    else:
        return 28


def day_of_year(year, month, day):
    days = ["Saturday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]

    if day > days_in_month(2000, 12):
        return None

    k = 6 - 2 * (year // 100 % 4)

    if is_year_leap(year):
        data = ((day + month + k) % 7 - 1)
    else:
        data = ((day + month + k) % 7)
    return days[data]


print(day_of_year(2000, 12, 31))
os.system("pause")
