from django.db import models

class Task(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.description}"
