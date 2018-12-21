import calendar
from datetime import datetime, timedelta

"""    Display Full calendar for given Year    """
print(calendar.calendar(2018,3,2,6))

"""    Display Starting weekday - Mon-Sun(0-6)    """
calendar.setfirstweekday(calendar.SUNDAY)
print("First Week day is :",calendar.firstweekday())

"""    Check if the given year is leap    """
print(calendar.isleap(2018))

"""    Counts total leap days between given year range    """
print("There are",calendar.leapdays(2012, 2021),"leap days from 2012 to 2021")

"""    Display full given month    """
print()
print(calendar.month(2018,12,2,1))

"""    Give day name on Given date    """
day=calendar.day_name[calendar.weekday(2018, 12, 27)]
print("Weekday on 27th December, 2018 is",day)

"""    Counts occurences of Weekday    """
c=calendar.Calendar()
date=datetime(2018,12,27)
a=0
while date>datetime(2018,12,1):
    a+=1
    date-=timedelta(7)
    
print("It's",a,"th",day,"of December")

"""    Gives all dates on Saturday for given month    """
daylist=c.monthdatescalendar(2018,12)
saturdays=[date for datelist in daylist for date in datelist if date.weekday()==5 and date.month==12]
print(saturdays)

"""    Gives First day of Month and Total days of Month    """
print(calendar.monthrange(2018, 12))



