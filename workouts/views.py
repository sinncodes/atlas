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
    #generate the calendar data here.
    context = {
        "today": today,
        "year": year,
        "month": month,
    }

    return render(request, "workouts/calendar.html", context)

