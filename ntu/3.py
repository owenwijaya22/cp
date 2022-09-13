from calendar import month
from datetime import date
birthdate_A = input('Person A, e.g. (yyyy mm dd): ')
birthdate_B = input('Person B, e.g. (yyyy mm dd): ')

if birthdate_A == birthdate_B:
    print("they are at the same age")

today_year, today_month, today_day = list(map(int, str(date.today()).split('-')))

A_year, A_month, A_day = list(map(int, birthdate_A.split()))
B_year, B_month, B_day = list(map(int, birthdate_B.split()))

print(today_day)

A_age = [today_year - A_year , today_month - A_month, today_day - A_day]
B_age = [today_year - B_year , today_month - B_month, today_day - B_day]

print(A_age, B_age)

