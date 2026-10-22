from django.db import models
from django.conf import settings

class Muscle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscles = models.ManyToManyField(Muscle, related_name="exercises")

    
    def __str__(self):
        return self.name

class Routine(models.Model):
    name = models.CharField(max_length=50)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="routines"
    )


    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=50)
    routine = models.ForeignKey(
        Routine,
        on_delete=models.CASCADE,
        related_name="workouts"
    )

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="workout_exercises"
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="workout_exercises"
    )
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.workout.name + " - " + self.exercise.name

"""workout.workout_exercises.all() to get all workout's exercises,
routine.workouts.all() to get all workouts in a routine
user.routines.all() to retrieve all users routines"""