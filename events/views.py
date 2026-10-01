from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm
from .models import Booking, Event
from datetime import date
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    events = Event.objects.all()[:3]
    return render(request, "events/home.html", {"events": events})


def event_list(request):
    events = Event.objects.all()
    return render(
        request,
        "events/event_list.html",
        {"events": events},
    )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)

    booking = None

    if request.user.is_authenticated:
        booking = Booking.objects.filter(
            user=request.user,
            event=event,
        ).first()

    booked_count = event.bookings.count()
    spaces_remaining = max(event.capacity - booked_count, 0)
    is_sold_out = spaces_remaining == 0
    is_past = event.date < date.today()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "booking": booking,
            "spaces_remaining": spaces_remaining,
            "is_sold_out": is_sold_out,
            "is_past": is_past,
        },
    )


@user_passes_test(lambda user: user.is_staff)
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, "Event created successfully.")
            return redirect("event_detail", pk=event.pk)
    else:
        form = EventForm()

    return render(
        request,
        "events/event_form.html",
        {
            "form": form,
            "page_title": "Create Event",
        },
    )


@user_passes_test(lambda user: user.is_staff)
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect("event_detail", pk=event.pk)
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "events/event_form.html",
        {
            "form": form,
            "page_title": "Edit Event",
        },
    )


@user_passes_test(lambda user: user.is_staff)
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect("event_list")

    return render(
        request,
        "events/event_confirm_delete.html",
        {"event": event},
    )

@login_required
def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method != "POST":
        return redirect("event_detail", pk=event.pk)

    if event.date < date.today():
        messages.error(request, "Past events cannot be booked.")
        return redirect("event_detail", pk=event.pk)

    if Booking.objects.filter(
        user=request.user,
        event=event,
    ).exists():
        messages.warning(request, "You have already booked this event.")
        return redirect("event_detail", pk=event.pk)

    if event.bookings.count() >= event.capacity:
        messages.error(request, "This event is sold out.")
        return redirect("event_detail", pk=event.pk)

    Booking.objects.create(
        user=request.user,
        event=event,
    )

    messages.success(request, "Your booking is confirmed.")
    return redirect("my_bookings")

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(
        Booking,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking cancelled.")

    return redirect("my_bookings")


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user
    ).select_related("event")

    return render(
        request,
        "events/my_bookings.html",
        {"bookings": bookings},
    )



def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your account has been created."
            )

            return redirect("home")

    else:
        form = UserCreationForm()

    return render(
        request,
        "events/register.html",
        {"form": form},
    )