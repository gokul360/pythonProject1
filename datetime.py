import _datetime as dt
todaydate=dt.date.today()
print("today's date:",todaydate)

new=dt.date(2023,4,22)
print(new)
print("year:",new.year)

curent_time=dt.datetime.now()
print(curent_time)


dob=dt.datetime(2000,4,29,4,25,56)
print(dob)
print("date:",dob.day)
print("seconds",dob.second)
print("hour",dob.hour)
print(curent_time.time)
print(curent_time.date())
current=dt.datetime.now()
print(current)
birthday=dt.datetime(2023,4,29,4,35,44)
difference=current-birthday
print(difference )
c=dt.datetime.now()
print(c)
s=c.strftime("%a,%b,%d,%y")
print(s)
print(s)