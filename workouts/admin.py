from django.contrib import admin

from django.contrib import admin

from .models import Muscle, Exercise, Routine, Workout, WorkoutExercise
 
admin.site.register(Muscle)
admin.site.register(Exercise)
admin.site.register(Routine)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)