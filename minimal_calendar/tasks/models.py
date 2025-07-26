from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.description}"
