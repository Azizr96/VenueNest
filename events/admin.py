from django.contrib import admin
from .models import Event


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