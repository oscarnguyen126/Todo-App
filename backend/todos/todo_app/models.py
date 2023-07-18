from django.db import models
from users.models import User


class Todo(models.Model):
    description = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)
    complete_date = models.DateField()
    is_expired = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE, null=True, blank=True)
