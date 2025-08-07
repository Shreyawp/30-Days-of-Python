# Day 16: 30 Days of python programming

## Datetime package

import datetime
print(dir(datetime))
''' 
####################### OUTPUT ##########################
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 
'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 
'tzinfo']
##########################################################
'''

# getting datetime info
from datetime import datetime
#print(dir(datetime))
now = datetime.now()
print(now)          
# >> 2025-07-08 21:07:29.712607

day = now.day
month = now.month
year = now.year
hour = now.hour
min = now.minute
sec = now.second
timestamp = now.timestamp()

print(f'{day}/{month}/{year}, {hour}:{min}:{sec}')
print(f'Timestamp: {timestamp}')
# Timestamp or Unix timestamp is the number of seconds elapsed 
# from 1st of January 1970 UTC.
''' 
####################### OUTPUT ##########################
8/7/2025, 21:10:32
Timestamp: 1751989232.916164
##########################################################
'''

new_year = datetime(2025,1,1)
print(new_year)
# >> 2025-01-01 00:00:00

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
min = new_year.minute
sec = new_year.second
print(f'{day}/{month}/{year}, {hour}:{min}:{sec}')
print(f'Timestamp: {timestamp}')
''' 
####################### OUTPUT ##########################
1/1/2025, 0:0:0
Timestamp: 1751989507.870142
##########################################################
'''

## Formatting Date Output Using strftime()

import pytz     # type: ignore # to provide timezone
now = datetime.now(pytz.timezone("Asia/Kolkata"))
t = now.strftime("%H:%M:%S")
print("Time: ",t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("TIme_one (MM/DD/YYYY h:m:s): ", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time_two: (DD/MM/YYYY h:m:s)", time_two)
''' 
####################### OUTPUT ##########################
Time:  21:20:56
TIme_one (MM/DD/YYYY h:m:s):  07/08/2025, 21:20:56
time_two: (DD/MM/YYYY h:m:s) 08/07/2025, 21:20:56
##########################################################
'''
print("weekday(s): ", now.strftime("%a"))
# >> weekday(s):  Tue
print("weekday: ", now.strftime("%A"))
# >> weekday:  Tuesday
print("weekday(num): ", now.strftime("%w"))
# >> weekday(num):  2

print("Month(s): ", now.strftime("%b"))
# >> Month(s):  Jul
print("Month: ", now.strftime("%B"))
# >> Month:  July

print("Year(s): ", now.strftime("%y"))
# >> Year(s):  25
print("Hour(0-12): ", now.strftime("%I"))
# >> Hour(0-12):  09
print("time(AM/PM): ", now.strftime("%p"))
# >> time(AM/PM):  PM
print("Microsecound: ", now.strftime("%f"))
# >> Microsecound:  443113
print("UTC offset: ", now.strftime("%z"))
# >> UTC offset:  +0530
print("TImezone: ", now.strftime("%Z"))
# >> TImezone:  IST
print("Day num of year: ", now.strftime("%j"))
# >> Day num of year:  189
print("Week num of year (with sun=1): ", now.strftime("%U"))
# >> Week num of year (with sun=1):  27
print("Week num of year (with mon=1): ", now.strftime("%W"))
# >> Week num of year (with mon=1):  27
print("Local ver datetime: ", now.strftime("%c"))
# >> Local ver datetime:  Tue Jul  8 21:35:22 2025
print("Local ver of date: ", now.strftime("%x"))
# >> Local ver of date:  07/08/25
print("Local ver of time: ", now.strftime("%X"))
# >> Local ver of time:  21:35:22
print("mod char: ", now.strftime("%%"))
# >> mod char:  %

## String to Time Using strptime()

date_str = "5 December, 2022"
print("Date string: ", date_str)
# >> Date string:  5 December, 2022

date_obj = datetime.strptime(date_str, "%d %B, %Y")
print("Date object: ", date_obj)
# >> Date object:  2022-12-05 00:00:00

## Using date() from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)
# >> 2020-01-01
print("Current date: ", d.today())
# >> Current date:  2025-07-08

today = date.today()
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)
''' 
####################### OUTPUT ##########################
Current year:  2025
Current month:  7
Current day:  8
##########################################################
'''

## Time Objects to Represent Time
from datetime import time
a = time()
print("a = ", a)
# >> a =  00:00:00
b = time(10,20,30)
print("b = ", b)
# >> b =  10:20:30
c = time(hour=10, minute=50, second=6, microsecond=125)
print("C = ", c)
# >> C =  10:50:06.000125
d = time(4, 25, 38, 9842)
print("d = ", d)
# >> d =  04:25:38.009842

## Difference Between Two Points in Time Using date() and datetime()
today = date(year=2019, day=5, month=12)
new_year = date(year=2020, month=1, day=1)
print("Time left for new year: ", new_year - today)
# >> Time left for new year:  27 days, 0:00:00

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(2020,1,1,0,0,0)
print("Time left for new year: ", t2 - t1)
# >> Time left for new year:  26 days, 23:01:00

## Difference Between Two Points in Time Using timedelta()
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
print("Time diff: ", t1 - t2)
# >> Time diff:  86 days, 22:56:50

## Exercise

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
current = datetime.now()
c_day = current.day
c_month = current.month
c_year = current.year
c_hour = current.hour
c_min = current.minute
c_timestamp = current.timestamp
print(f"{c_day}/{c_month}/{c_year} {c_hour}:{c_min} \n{timestamp}")
''' 
####################### OUTPUT ##########################
8/7/2025 23:29
1751997558.123016
##########################################################
'''

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print("Current date: ", current.strftime("%m/%d/%y , %H:%M:%S"))
# >> Current date:  07/08/25 , 23:31:43

# 3. Today is 5 December, 2019. Change this time string to time.
today = "5 December, 2019"
print("Today: ", datetime.strptime(today, "%d %B, %Y"))
# >> Today:  2019-12-05 00:00:00

# 4. Calculate the time difference between now and new year.
now = datetime.now()
new_year = datetime(2026, 1, 1)
print("time difference between now and new year: ", new_year-now)
# >> time difference between now and new year:  176 days, 0:21:57.210138

# 5. Calculate the time difference between 1 January 1970 and now.
year = datetime(1970,1,1)
print("time difference between 1 January 1970 and now: ", now-year)
# >> time difference between 1 January 1970 and now:  20277 days, 23:40:41.132533

# 6. Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
