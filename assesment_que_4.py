def isLeapYear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else: 
        return False

def season(month, day):
    if (month == 12 and day >= 21) or (month <= 2 and day < 20):
        return "Winter"
    elif month>=3 and month <=5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    else:
        return "Fall"

def next_leap_year(year):
    while True:
        year += 1
        if isLeapYear(year):
            return year

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

season = season(month, day)
print(f"The season for the given date is: {season}")

if isLeapYear(year):
    print(f"{year} is a leap year.")
    days_in_year = 366
else:
    print(f"{year} is not a leap year.")
    next_leap = next_leap_year(year)
    print(f"The next leap year is: {next_leap}")
    days_in_year = 365

print(f"The number of days in {year} is: {days_in_year}")
