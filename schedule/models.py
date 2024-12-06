from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    dayS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    FREQUENCIES = [
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]

    day = models.CharField(max_length=10, choices=dayS)
    time = models.TimeField()
    frequency = models.CharField(max_length=10, choices=FREQUENCIES)

    def __str__(self):
        return f"{self.day} - {self.time} - {self.frequency}"
