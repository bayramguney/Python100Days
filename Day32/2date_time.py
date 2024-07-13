import datetime as dt


now = dt.datetime.now()  # 2024-07-13 11:54:51.257162
year = now.year  # 2024
month = now.month
day = now.year
day_of_week = now.weekday()    # 5     as Saturday
print(day_of_week)

date_of_birth = dt.datetime(year=2013,month=10,day=25,hour=18)
print(date_of_birth.weekday())     # 4  as friday

