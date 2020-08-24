from datetime import datetime, timedelta,timezone, date
import time

my_date = datetime(2020,11,11,18,15,25)
print(my_date, type(my_date))

now_datetime = datetime.now()
utc_datetime = datetime.utcnow()
print(now_datetime,utc_datetime)

print(now_datetime.year, now_datetime.month,now_datetime.microsecond)

#文字列から変換
timestr = '2020/12/12 16:40'

dt = datetime.strptime(timestr, '%Y/%m/%d %H:%M')
print(dt,type(dt))

#文字列へ変換
date_str = dt.strftime('%Y/%m/%d')
print(date_str, type(date_str))

print(datetime.now() - timedelta(days=10))
my_date = datetime(2020,11,11,18,15,25)

local_date = my_date.replace(tzinfo=timezone.utc).astimezone()
print(my_date, local_date)

#date => datetime

date_obj = date.today()
datetime_obj = datetime(date_obj.year,date_obj.month, date_obj.day)
print(datetime_obj)

datetime_obj = datetime.now()
date_obj = datetime_obj.date()
print(date_obj)

#timeモジュール
print(time.time())
for x in range(10):
    print(x)
    time.sleep(1)