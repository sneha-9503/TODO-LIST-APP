from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False)

