from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    generated_on = models.DateTimeField(default=timezone.now)
    data = models.TextField()

    def __str__(self):
        return f"{self.user.username} {self.report_type} on {self.generated_on}"

    def formatted_generated_on(self):
        return self.generated_on.strftime("%B %d, %Y, %I:%M %p")