import calendar
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.utils.safestring import mark_safe


def index(request):
    return HttpResponse("INDEX")

def calendar_view(request, year=None, month=None):
    today = timezone.localdate()
    year = year or today.year
    month = month or today.month 

    if not 1 <= month <= 12:
        raise Http404("Invalid month")

    cal = calendar.Calendar(firstweekday=0)
    weeks = cal.monthdatescalendar(year, month)

    return render(request, "workouts/calendar.html", {
        "weeks": weeks,
        "month_name": calendar.month_name[month],
        "year": year,
        "today_day": today,
    })

