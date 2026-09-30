from django.contrib import admin
from .models import Booking, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "date",
        "start_time",
        "capacity",
    )
    list_filter = ("date", "location")
    search_fields = ("title", "location")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event",
        "booked_at",
    )
    search_fields = (
        "user__username",
        "event__title",
    )
