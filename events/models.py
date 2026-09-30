from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_events",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "start_time"]

    def __str__(self):
        return self.title