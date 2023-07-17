from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)
    complete_date = models.DateField()
    is_expired = models.BooleanField(default=False)

