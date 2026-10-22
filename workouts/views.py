from django.shortcuts import render
from datetime import date
from django.http import HttpResponse

def index(request):
    return HttpResponse("INDEX")


def workouts(request):
    response = "workouts page displaying the users workouts"
    return HttpResponse(response)

def calendar_view(request, year=None, month=None):
    today = date.today()

    #default to the current month.
    if year is None or month is None:
        year = today.year
        month = today.month

    #generate the calendar data here.
    context = {
        "today": today,
        "year": year,
        "month": month,
    }

    return render(request, "workouts/calendar.html", context)

from django.http import Http404
from django.utils import timezone


def day_view(request, year, month, day):
    try:
        selected_date = date(year, month, day)
    except ValueError:
        raise Http404("Invalid date")

    today = timezone.localdate()

    if selected_date == today:
        day_type = "today"
    elif selected_date < today:
        day_type = "past"
    else:
        day_type = "future"

    context = {
        "selected_date": selected_date,
        "day_type": day_type,
    }

    return render(request, "myapp/day.html", context)
