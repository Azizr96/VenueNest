# VenueNest

VenueNest is a simple Django event booking platform built during a three-day team hackathon.

## Features

- User registration
- Login and logout
- Browse events
- View event details
- Staff event CRUD
- Book an event
- Cancel a booking
- My Bookings page
- Duplicate booking prevention
- Sold-out prevention
- Past-event booking prevention
- Responsive Bootstrap design

## Technologies

- Python
- Django
- PostgreSQL
- Bootstrap
- Git
- GitHub

## Data Models
![VenueNest ER Diagram](../assets/diagram.png)

### Event
- title
- description
- location
- date
- start_time
- capacity
- created_by
- created_at

### Booking
- user
- event
- booked_at

## User Roles

### Visitor
- browse events
- view event details
- register
- login

### Logged-in User
- book events
- cancel bookings
- view My Bookings

### Staff
- create events
- edit events
- delete events

## Testing

Automated tests cover:
- Event model
- booking creation
- duplicate bookings
- sold-out events
- past events
- permissions
- authentication pages

## Local Setup

1. Clone the repository
2. Create virtual environment
3. Install requirements
4. Create env.py
5. Run migrations
6. Start server

## Team

Add all five team members and their roles.

==================================================
STEP 5 — MANUAL TESTING TABLE
==================================================

Add:

| Feature | Test | Expected Result |
|---|---|---|
| Register | Valid user details | Account created |
| Login | Correct credentials | User logged in |
| Events | Open event list | Events displayed |
| Event details | Open event | Details displayed |
| Booking | Book available event | Booking created |
| Duplicate booking | Book same event twice | Blocked |
| Sold out | Book full event | Blocked |
| Past event | Book expired event | Blocked |
| Cancel | Cancel own booking | Booking removed |
| Permissions | Normal user opens create page | Access blocked |
| Staff | Staff opens create page | Page loads |
