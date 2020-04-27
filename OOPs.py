import datetime

def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True

my_date = datetime.date(2020, 7, 17)

print(is_workday(my_date))