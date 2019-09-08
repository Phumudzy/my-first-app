from django.shortcuts import render

#from django.http import HttpResponse
from datetime import date
from datetime import datetime
import calendar
from calendar import HTMLCalendar



def index(request,year=date.today().year,month =date.today().month):
   # t = date.today()
   # month = date.strftime(t, '%b')
   # year =t.year
    month = int(month)
    year = int(year)
    if year<1900 or year>2099:
        year=date.today().year

    month_name = calendar.month_name[month]
    title = "Myclub event calendar-- %s %s"%(month_name,year)
    cal = HTMLCalendar().formatmonth(year, month)
   # return HttpResponse("<h1>%s</h1><p>%s</p>"%(title,cal))
    return render(request, 'calendar_base.html', {'title': title, 'cal': cal})
