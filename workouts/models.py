from django.db import models

#model for storing a muscle
class Muscle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


#model for storing an exercise, and the muscles it works
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscles = models.ManyToManyField(Muscle, related_name="exercises")
    
    def __str__(self):
        return self.name


#model for storing a workout, and its exercises
class Workout(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


#model for mapping the exercises to a workout, setting sets and reps
class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workout_exercises")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="workout_exercises")

    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return self.workout.name + " - " + self.exercise.name


#model for scheduling a workout to a date
class ScheduledWorkout(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="scheduled")
    date = models.DateField()
    
    def __str__(self):
        return f"{self.workout.name} on {self.date}"
