from django.urls import path

from . import views

app_name = "workouts"

urlpatterns = [
    #index page
    path("", views.index, name="index"),
    #calendar page
    path("calendar/", views.calendar_view, name="calendar"),

    path(
        "calendar/<int:year>/<int:month>/",
        views.calendar_view,
        name="calendar_month",
    ),
    path(
        "calendar/<int:year>/<int:month>/<int:day>/",
        views.day_view,
        name="day",
    ),
]
    
