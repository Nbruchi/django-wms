from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    WEEK_DAYS = [
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

    week_day = models.CharField(max_length=10, choices=WEEK_DAYS)
    day_time = models.TimeField()
    frequency = models.CharField(max_length=10, choices=FREQUENCIES)

    def __str__(self):
        return f"{self.week_day} - {self.day_time} - {self.frequency}"
