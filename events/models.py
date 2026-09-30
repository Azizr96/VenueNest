from django.db import models
from django.contrib.auth.models import User

# 1. Event model defined FIRST
class Event(models.Model):
    title = models.CharField(max_length=200)
    # ... other Event fields ...

    def __str__(self):
        return self.title


# 2. Booking model defined SECOND
class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "event"],
                name="unique_user_event_booking",
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"