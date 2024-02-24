from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=25)


