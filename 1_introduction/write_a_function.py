def is_leap(year):
    leap = True
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return leap
    else:
        return not leap
check_year = int(input("Year: "))
print(is_leap(check_year))

