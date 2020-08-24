
from datetime import date, timedelta

my_date = date(1000,1,1)
print(my_date)

print(my_date < date.today())

my_date = my_date.replace(year=2000, month=12)
print(my_date)

my_date_2 = date.today() - timedelta(days=12)
print(my_date_2)

print(my_date_2.year)

str_date = my_date_2.strftime('%Y/%m/%d')
print(str_date)
print(type(my_date_2))