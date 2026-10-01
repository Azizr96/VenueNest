from django.test import TestCase

# Create your tests here.
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.urls import reverse

from .models import Booking, Event


class EventModelTests(TestCase):

    def setUp(self):
        self.staff = User.objects.create_user(
            username="staff",
            password="testpass123",
            is_staff=True,
        )

        self.event = Event.objects.create(
            title="Django Workshop",
            description="A test event",
            location="Birmingham",
            date=date.today() + timedelta(days=5),
            start_time="10:00",
            capacity=10,
            created_by=self.staff,
        )

    def test_event_string(self):
        self.assertEqual(
            str(self.event),
            "Django Workshop"
        )


class BookingTests(TestCase):

    def setUp(self):
        self.staff = User.objects.create_user(
            username="staff",
            password="testpass123",
            is_staff=True,
        )

        self.user = User.objects.create_user(
            username="normaluser",
            password="testpass123",
        )

        self.event = Event.objects.create(
            title="Python Meetup",
            description="Meet Python developers",
            location="London",
            date=date.today() + timedelta(days=5),
            start_time="12:00",
            capacity=2,
            created_by=self.staff,
        )

    def test_logged_in_user_can_book(self):
        self.client.login(
            username="normaluser",
            password="testpass123",
        )

        response = self.client.post(
            reverse("book_event", args=[self.event.pk])
        )

        self.assertEqual(
            Booking.objects.filter(
                user=self.user,
                event=self.event,
            ).count(),
            1,
        )

        self.assertRedirects(
            response,
            reverse("my_bookings")
        )

    def test_duplicate_booking_is_blocked(self):
        Booking.objects.create(
            user=self.user,
            event=self.event,
        )

        self.client.login(
            username="normaluser",
            password="testpass123",
        )

        self.client.post(
            reverse("book_event", args=[self.event.pk])
        )

        self.assertEqual(
            Booking.objects.filter(
                user=self.user,
                event=self.event,
            ).count(),
            1,
        )

    def test_past_event_cannot_be_booked(self):
        past_event = Event.objects.create(
            title="Old Event",
            description="Past event",
            location="Manchester",
            date=date.today() - timedelta(days=1),
            start_time="09:00",
            capacity=10,
            created_by=self.staff,
        )

        self.client.login(
            username="normaluser",
            password="testpass123",
        )

        self.client.post(
            reverse("book_event", args=[past_event.pk])
        )

        self.assertFalse(
            Booking.objects.filter(
                user=self.user,
                event=past_event,
            ).exists()
        )

    def test_sold_out_event_cannot_be_booked(self):
        second_user = User.objects.create_user(
            username="seconduser",
            password="testpass123",
        )

        sold_out_event = Event.objects.create(
            title="Small Event",
            description="One place only",
            location="Leeds",
            date=date.today() + timedelta(days=3),
            start_time="11:00",
            capacity=1,
            created_by=self.staff,
        )

        Booking.objects.create(
            user=second_user,
            event=sold_out_event,
        )

        self.client.login(
            username="normaluser",
            password="testpass123",
        )

        self.client.post(
            reverse("book_event", args=[sold_out_event.pk])
        )

        self.assertFalse(
            Booking.objects.filter(
                user=self.user,
                event=sold_out_event,
            ).exists()
        )


class PermissionTests(TestCase):

    def setUp(self):
        self.normal_user = User.objects.create_user(
            username="member",
            password="testpass123",
        )

    def test_normal_user_cannot_access_create_event(self):
        self.client.login(
            username="member",
            password="testpass123",
        )

        response = self.client.get(
            reverse("event_create")
        )

        self.assertNotEqual(
            response.status_code,
            200
        )


class AuthenticationTests(TestCase):

    def test_register_page_loads(self):
        response = self.client.get(
            reverse("register")
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_login_page_loads(self):
        response = self.client.get(
            reverse("login")
        )

        self.assertEqual(
            response.status_code,
            200
        )
