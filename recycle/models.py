from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Recycle(models.Model):
    RECYCLABLES =[
        ('plastic','Plastic'),
        ('glass','Glass'),
        ('metal','Metal'),
        ('paper','Paper')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=RECYCLABLES)
    quantity = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.quantity}kg - {self.date}"

    def formatted_date(self):
        return self.date.strftime("%B %d, %Y, %I:%M %p")