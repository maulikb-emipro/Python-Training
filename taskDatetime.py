from datetime import timedelta, date, time, datetime
import pytz 

"""    Create Date, Time and Timezone object    """
from pytz import timezone
d=date(1996,12,27)
t=time(19,5,33)

"""    Combines date and time object """
dt=datetime.combine(d,t) 
print(dt)

"""    Addition in Datetime    """
newDate=dt+timedelta(days=13,hours=14)
print(newDate)

"""    Difference of two datetime    """
datetime2=datetime.now()
print(datetime2-dt)
# print(divmod(datetime2, dt))

"""    Multiplication of Time    """
multitd=timedelta(2,16,0,0,2.5,3)*2.5
# multi=t*2.5
print(multitd)

"""    Division of Time    """
dividetd=timedelta(days=2,hours=2.5,minutes=3)/2
print(dividetd)

"""    Name of Current Month    """
month=datetime.now()
print(dt.strftime("%B"))

"""    Year with Century no and without it    """
print(datetime2.strftime("%Y"))
print(datetime2.strftime("%y"))

"""    Time in 12-hour and 24-hour Clock    """
print(datetime2.strftime("%I:%M:%S %p"))
print(datetime2.strftime("%H:%M:%S"))

"""    Adding year, month, hours, minutes and days    """
added=datetime2+timedelta(days=365,hours=2,minutes=147,seconds=120)
print(added)

"""    UTC Date and Time    """
utc1=datetime2.utcnow()
print(utc1)

"""    Day of the Year    """
print(datetime2.strftime("%j"))

"""    Week of the Year    """
print(datetime2.strftime("%U"))

"""    Different format of current Date    """
today=datetime2.date()
print("DD/MM/YY",today.strftime("%d/%m/%y"))
print("DD/MM/YY",today.strftime("%m/%d/%y"))
print("DD/MM/YY",today.strftime("%y/%m/%d"))
print("MM-DD-YY",today.strftime("%m-%d-%y"))
print("DD-MM-YY",today.strftime("%d-%m-%y"))
print("YY-DD-MM",today.strftime("%y-%d-%m"))

"""    Timezone    """
print(datetime2.utcnow())
# print(timezone(timedelta(hours=5,minutes=30)))

print(dt)
new_time=timezone('Asia/Kolkata')
print(pytz.utc.localize(dt).astimezone(new_time))

print(pytz.all_timezones)
