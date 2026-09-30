from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm
from .models import Booking, Event


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
    return render(
        request,
        "events/event_detail.html",
        {"event": event},
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

