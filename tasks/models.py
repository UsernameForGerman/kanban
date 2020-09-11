from django.db import models

TODO = "To Do"
IN_PROGRESS = "In Progress"
DONE = "Done"
SALARY_PER_HOUR = 1000

class Task(models.Model):
    STATUS_CHOICES = (
        (0, TODO),
        (1, IN_PROGRESS),
        (2, DONE)
    )

    name = models.CharField('Name of the task', max_length=256)
    status = models.IntegerField('Status of the task', choices=STATUS_CHOICES)

class TimeStart(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)

class Sum(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
    sum = models.FloatField()



