from django.contrib import admin

from django.contrib import admin

from .models import Muscle, Exercise, Workout, WorkoutExercise, ScheduledWorkout
 
admin.site.register(Muscle)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
admin.site.register(ScheduledWorkout)