from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.event_list, name="event_list"),
    path("events/<int:pk>/", views.event_detail, name="event_detail"),
    path("events/create/", views.event_create, name="event_create"),
    path("events/<int:pk>/edit/", views.event_edit, name="event_edit"),
    path("events/<int:pk>/delete/", views.event_delete, name="event_delete"),
    path("events/<int:pk>/book/", views.book_event, name="book_event"),
    path(
        "bookings/<int:pk>/cancel/",
        views.cancel_booking,
        name="cancel_booking",
    ),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
]
