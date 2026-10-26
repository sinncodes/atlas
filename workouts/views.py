import calendar
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.utils.safestring import mark_safe
import datetime


def index(request):
    return HttpResponse("INDEX")

def calendar_view(request, year=None, month=None):
    today = timezone.localdate()
    year = year or today.year
    month = month or today.month 

    if not 1 <= month <= 12:
        raise Http404("Invalid month")

    cal = calendar.Calendar(firstweekday=0)
    weeks = calendar.Calendar(firstweekday=0).monthdayscalendar(year, month)

    return render(request, "workouts/calendar.html", {
        "weeks": weeks,
        "month_name": calendar.month_name[month],
        "year": year,
        "month": month,
        "today_day": today,
    })

def day_view(request, year, month, day):
    try:
        date = datetime.date(year, month, day)
    except ValueError:
        raise Http404("Invalid date")

    return render(request, "workouts/day.html", {"date": date})
