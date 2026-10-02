# VenueNest

**Developers:**  
[Rauhan Aziz](https://github.com/Azizr96) ·
[Shruti Jindal](https://github.com/shrutijind) ·
[Davy](https://github.com/davy-berry) ·
[Mohammed Chaudhary](https://github.com/nasim-orion/) ·
[Marcel Szymczak](https://github.com/xmarcelx2018-cmd)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Azizr96/VenueNest)](https://github.com/Azizr96/VenueNest/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Azizr96/VenueNest)](https://github.com/Azizr96/VenueNest/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Azizr96/VenueNest)](https://github.com/Azizr96/VenueNest)
[![Deployment](https://img.shields.io/badge/deployment-Heroku-purple)](https://venuenest-c59f0cde663d.herokuapp.com/)

VenueNest is a responsive event-booking web application built with Django. It allows visitors to browse upcoming events, registered users to book and manage events, and staff users to create, edit and delete event records.

The project was developed collaboratively during a team hackathon using Agile practices, feature branches and pull requests. The objective was to deliver a practical MVP demonstrating full-stack Django development, authentication, relational database design, CRUD functionality, booking validation, responsive design, version control and cloud deployment.

VenueNest was chosen because an event-booking system provides a realistic but achievable development challenge. It requires multiple user roles, protected functionality, database relationships, validation rules and a clear booking flow while remaining suitable for a short hackathon timeframe.

**Live site:** [VenueNest on Heroku](https://venuenest-c59f0cde663d.herokuapp.com/)

![VenueNest responsive mockup](assets/home.png)

---

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

- Provide visitors with a simple way to discover upcoming events.
- Allow registered users to book events and manage their own bookings.
- Give staff users protected tools for creating and maintaining event information.
- Prevent invalid booking behaviour such as duplicate bookings, overbooking and booking past events.

**Primary User Needs**

- Visitors need to browse events without creating an account first.
- Registered users need a straightforward registration and login process.
- Registered users need an easy way to make, view and cancel bookings.
- Users need clear feedback when an action cannot be completed.
- Staff users need protected event-management controls.
- The interface needs to work clearly on mobile, tablet and desktop devices.

**Project Goals**

- Deliver a usable event-booking MVP.
- Demonstrate Django authentication, permissions and CRUD.
- Use relational database models for events and bookings.
- Apply defensive booking logic to protect data integrity.
- Build a responsive interface with Bootstrap and custom CSS.
- Deploy successfully to Heroku using PostgreSQL, Gunicorn and WhiteNoise.

#### 2. Scope

The project scope was deliberately kept focused so that the complete booking journey could be delivered within the hackathon timeframe.

**Must-Have Functionality**

- User registration.
- User login and logout.
- Browse upcoming events.
- View event details.
- Staff-only event creation.
- Staff-only event editing.
- Staff-only event deletion.
- Authenticated event booking.
- My Bookings page.
- Booking cancellation.
- Duplicate-booking prevention.
- Capacity and sold-out protection.
- Past-event booking protection.
- Responsive Bootstrap interface.
- PostgreSQL database.
- Heroku deployment.

**Should-Have / Future Functionality**

- Event search.
- Event category filtering.
- Staff attendee lists.
- Event images.
- Additional event-discovery and management features.

#### 3. Structure

**Information Architecture**

- **Home** — project introduction and entry point.
- **Events** — list of available events.
- **Event Detail** — event information and booking actions.
- **Register / Login** — authentication for visitors.
- **My Bookings** — booking management for authenticated users.
- **Create Event** — staff-only event creation.
- **Edit / Delete Event** — staff-only management actions.
- **Logout** — ends the authenticated session.

**Primary User Flows**

1. Visitor opens VenueNest → browses events → views an event.
2. Visitor registers → becomes authenticated → books an event.
3. Registered user opens My Bookings → reviews bookings → cancels if required.
4. Staff user logs in → creates, edits or deletes events.
5. Booking rules are checked before a booking is saved.

#### 4. Skeleton

The interface is built around a small number of reusable page patterns and Bootstrap components.

**Core Screens**

- Home.
- Register.
- Login.
- Events list.
- Event detail.
- Create event.
- Edit event.
- Delete confirmation.
- My Bookings.

### Wireframes

Wireframes were created for the main responsive breakpoints.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![Home mobile](assets/mobile.png) | ![Home tablet](assets/tablet.png) | ![Home desktop](assets/desktop.png) |
| Register / Login | — | ![Login tablet](assets/logintab.png) | ![Login desktop](assets/login.png) |

#### 5. Surface

VenueNest uses Bootstrap for page layout, navigation, cards, forms and buttons, supported by custom CSS for project-specific presentation.

The interface aims to remain consistent across all pages through:

- clear headings;
- consistent spacing;
- reusable cards;
- obvious call-to-action buttons;
- visible success/error messages;
- responsive layouts.

### Colour Scheme

VenueNest uses a restrained Bootstrap-led colour palette to keep the interface clear, familiar and easy to navigate. The repository's custom stylesheet defines the page background, form borders and muted footer text, while Bootstrap classes provide the main action colours used throughout the navigation and forms.

| Colour | Hex | Use |
| --- | --- | --- |
| **Bootstrap Primary Blue** | `#0D6EFD` | Primary actions such as **Register**, **Create Event** and other `btn-primary` controls. |
| **Bootstrap Dark** | `#212529` | High-contrast actions such as **Logout** and dark text elements. |
| **Light Background** | `#F8F9FA` | Main page background and light navigation areas. |
| **Muted Grey** | `#6C757D` | Secondary/muted text, footer text and secondary interface elements. |
| **Form Border Grey** | `#CED4DA` | Borders around form inputs, selects and text areas. |
| **White** | `#FFFFFF` | Card and component backgrounds supplied through Bootstrap where applicable. |

The palette was intentionally kept simple. Blue is used for primary calls to action, darker tones distinguish secure/session actions, and neutral greys provide hierarchy without distracting from event content. The light background also helps Bootstrap cards, forms and buttons remain visually distinct.

> The explicit custom colours `#F8F9FA`, `#CED4DA` and `#6C757D` are defined in `events/static/events/css/style.css`. The primary, dark and white interface colours come from the Bootstrap 5.3.3 classes used in the templates.

### Typography

VenueNest uses Bootstrap's default system font stack for readability, consistency and fast loading across operating systems.

---

## User Stories

| ID | Target | Expectation | Outcome |
| --- | --- | --- | --- |
| **US-01** | As a visitor | I want to create an account | so that I can book events. |
| **US-02** | As a registered user | I want to log in | so that I can access booking features. |
| **US-03** | As an authenticated user | I want to log out | so that I can securely end my session. |
| **US-04** | As a visitor | I want to view available events | so that I can see what is coming up. |
| **US-05** | As a visitor | I want to view event details | so that I can decide whether I want to attend. |
| **US-06** | As a staff user | I want to create events | so that new events can be advertised. |
| **US-07** | As a staff user | I want to edit events | so that event information remains accurate. |
| **US-08** | As a staff user | I want to delete events | so that cancelled or unwanted events can be removed. |
| **US-09** | As a registered user | I want to book an event | so that I can reserve a place. |
| **US-10** | As a registered user | I want to view my bookings | so that I can keep track of events I plan to attend. |
| **US-11** | As a registered user | I want to cancel my booking | so that my place can be released if I can no longer attend. |
| **US-12** | As a user | I want to search events | so that I can find relevant events more quickly. |
| **US-13** | As a user | I want to filter events by category | so that I can browse relevant event types. |
| **US-14** | As a staff user | I want to view event attendees | so that I can see booking numbers and remaining capacity. |
| **US-15** | As a visitor | I want to see event images | so that event listings are more visually engaging. |

---

## Features

### Existing Features

| Feature | Description | Screenshot |
| --- | --- | --- |
| **Home Page** | Introduces VenueNest and provides access to the main event-booking journey. | ![Home page](assets/features/home.png) |
| **Registration** | Visitors can access the registration form to create an account. | ![Registration](assets/features/register.png) |
| **Login** | Registered users can authenticate securely. | ![Login](assets/features/login.png) |
| **Events List** | Visitors can browse available events. | ![Events list](assets/features/events.png) |
| **Event Detail** | Users can view event information, availability and booking actions. | ![Event detail](assets/features/event-detail.png) |
| **Book Event** | Authenticated users can reserve a place on an available event. | ![Book event](assets/features/book-event.png) |
| **My Bookings** | Authenticated users can review their current bookings. | ![My Bookings](assets/features/my-bookings.png) |
| **Cancel Booking** | Users can cancel their own booking. | ![Cancel booking](assets/features/cancel-booking.png) |
| **Duplicate Booking Protection** | The interface prevents users from booking an event they have already booked. | ![Duplicate booking protection](assets/features/duplicate-booking.png) |
| **Sold-Out Protection** | Booking controls are removed when an event has no remaining spaces. | ![Sold-out event](assets/features/sold-out.png) |
| **Past Event Protection** | Past events display a message and cannot be booked through the interface. | ![Past event](assets/features/past-event.png) |
| **User Navigation** | Authenticated standard users see Events, My Bookings and Logout controls. | ![Standard user navigation](assets/features/user-navbar.png) |
| **Staff Navigation** | Staff users receive additional event-management controls. | ![Staff navigation](assets/features/staff-navbar.png) |
| **Create Event** | Staff users can create new events. | ![Create event](assets/features/create-event.png) |
| **Edit Event** | Staff users can update existing event information. | ![Edit event](assets/features/edit-event.png) |
| **Delete Event** | Staff users can confirm deletion of an event. | ![Delete event](assets/features/delete-event.png) |
| **Delete Confirmation** | Successful deletion is confirmed to the staff user. | ![Event deleted successfully](assets/features/delete-event-complete.png) |


### Future Features

- Event search.
- Category filtering.
- Staff attendee lists.
- Event images.
- Email booking confirmations.
- Event status management.
- Enhanced user profiles.

---

## Tools & Technologies

| Tool / Technology | Use |
| --- | --- |
| **Python** | Back-end programming language. |
| **Django** | Main web framework. |
| **HTML5** | Page structure and semantic markup. |
| **CSS3** | Custom styling. |
| **JavaScript** | Client-side behaviour where applicable. |
| **Bootstrap** | Responsive layout and reusable UI components. |
| **PostgreSQL** | Production relational database. |
| **WhiteNoise** | Static-file serving in production. |
| **Gunicorn** | Production WSGI server. |
| **Heroku** | Cloud deployment. |
| **Git** | Local version control. |
| **GitHub** | Repository hosting, pull requests and collaboration. |
| **GitHub Projects** | Agile/Kanban task management. |
| **VS Code** | Development environment. |
| **W3C Validator** | HTML validation. |
| **W3C CSS Validator** | CSS validation. |
| **CI Python Linter / Flake8** | Python style validation. |
| **JSHint** | JavaScript validation where applicable. |
| **Chrome Lighthouse** | Performance, accessibility, best-practices and SEO audits. |

---

## Database Design

### Data Model

VenueNest uses Django's built-in `User` model with custom `Event` and `Booking` models.

- One staff user can create many events.
- One user can have many bookings.
- One event can have many bookings.
- A database constraint prevents the same user from booking the same event more than once.

<p align="center">
  <img src="assets/diagram.png" alt="VenueNest ER Diagram" width="600">
</p>

---

## Agile Development Process

### GitHub Projects

GitHub Projects was used to manage the hackathon using a Kanban-style Agile workflow.

The board was used to track:

- user stories;
- feature development;
- priorities;
- work in progress;
- completed tasks.

Add project-board screenshot here if available.

### GitHub Issues

GitHub Issues was used to document individual user stories and development tasks.

The team used MoSCoW prioritisation:

- **Must Have** — essential to the MVP.
- **Should Have** — valuable but not essential.
- **Could Have** — desirable if time allowed.
- **Won't Have / Future** — outside the current hackathon scope.

### Team Workflow

| Team Member | Responsibility |
| --- | --- |
| **Rauhan Aziz** | Project management, integration, deployment, fixing bugs, documentation |
| **Shruti Jindal** | Event functionality / agreed team feature work, documentation |
| **Davy** | Booking functionality / agreed team feature work. |
| **Mohammed Chaudhary** | Authentication / agreed team feature work. |
| **Marcel Szymczak** | Responsive frontend and UI polish. |

Feature work was developed on separate branches and integrated into `main` through pull requests and squash merges.

---

# Testing

VenueNest was tested using manual functional testing and external validation tools. Testing was performed against the deployed Heroku application wherever possible.

The testing strategy includes:

- manual functional testing;
- defensive/access-control testing;
- responsive testing;
- browser compatibility testing;
- Lighthouse audits;
- HTML validation;
- CSS validation;
- Python style validation;
- JavaScript validation where applicable.

No automated unit-test suite is included in the project.

## Manual Functional Testing

### Authentication and Navigation

| Test | Expected Outcome | Result | Evidence |
| --- | --- | --- | --- |
| Register page displays correctly | Registration form is available to visitors. | **Pass** | ![Register](assets/features/register.png) |
| Register with valid details | Account is created and user becomes authenticated. | **Not submitted during this test run** | Registration page only: ![Register](assets/features/register.png) |
| Login with valid credentials | User is authenticated and redirected successfully. | **Pass** | ![Login](assets/features/login.png) |
| Logout | User session ends successfully. | **Pass during user journey** | Navigation state before logout: ![Authenticated user navigation](assets/features/user-navbar.png) |
| Guest navigation | Guest only sees permitted navigation options. | **Pass** | ![Guest home/navigation](assets/features/home.png) |
| Authenticated navigation | User sees Events, My Bookings and Logout. | **Pass** | ![Authenticated user navigation](assets/features/user-navbar.png) |
| Staff navigation | Staff user sees Create Event and event-management controls. | **Pass** | ![Staff navigation](assets/features/staff-navbar.png) |

### Event Management

| Test | Expected Outcome | Result | Evidence |
| --- | --- | --- | --- |
| View events | Event list loads successfully. | **Pass** | ![Events](assets/features/events.png) |
| View event detail | Selected event is displayed correctly. | **Pass** | ![Event detail](assets/features/event-detail.png) |
| Create event as staff | Event can be created by a staff user. | **Pass** | ![Create event](assets/features/create-event.png) |
| Edit event as staff | Changes are saved and displayed. | **Pass** | ![Edit event](assets/features/edit-event.png) |
| Delete event as staff | Event is deleted after confirmation. | **Pass** | ![Delete event](assets/features/delete-event.png) ![Delete success](assets/features/delete-event-complete.png) |


### Booking and Defensive Testing

| Test | Expected Outcome | Result | Evidence |
| --- | --- | --- | --- |
| Book available event | Booking is created successfully. | **Pass** | ![Book event](assets/features/book-event.png) |
| View My Bookings | User sees their own bookings. | **Pass** | ![My Bookings](assets/features/my-bookings.png) |
| Cancel own booking | Booking is removed successfully. | **Pass** | ![Cancel booking](assets/features/cancel-booking.png) |
| Duplicate booking | A second booking is not offered once the user is already booked. | **Pass — UI prevention confirmed** | ![Duplicate booking protection](assets/features/duplicate-booking.png) |
| Sold-out event | Booking is unavailable when capacity has been reached. | **Pass — UI prevention confirmed** | ![Sold-out event](assets/features/sold-out.png) |
| Past event | Booking is unavailable for an event that has already passed. | **Pass — UI prevention confirmed** | ![Past event](assets/features/past-event.png) |


> **Defensive testing note:** duplicate-booking, sold-out and past-event checks confirm the behaviour presented through the user interface. Crafted POST requests, concurrent requests and another user's cancellation URL were not tested during this browser-based test pass.

### Navigation and Error Handling

| Test | Expected Outcome | Result | Evidence |
| --- | --- | --- | --- |
| Main navigation links | Main navigation routes to the correct pages for each user role. | **Pass** | ![Standard user navigation](assets/features/user-navbar.png) ![Staff navigation](assets/features/staff-navbar.png) |
| Invalid URL / 404 | User receives an appropriate 404 response/page. | **PASS** | ![404 page](assets/features/404.png) |
| Static files | Project styling loads correctly on the deployed site. | **Pass** | ![Home page](assets/features/home.png) |
| Post-deployment smoke test | Core pages load successfully on the deployed application. | **Pass** | ![Home](assets/features/home.png) ![Events](assets/features/events.png) ![Event detail](assets/features/event-detail.png) |


---

## Responsiveness

VenueNest was checked at three representative viewport sizes:

- **Mobile:** 375 × 812
- **Tablet:** 768 × 1024
- **Desktop:** 1440 × 900

The following screenshots demonstrate how the main pages adapt across those breakpoints.

### Home

| Mobile | Tablet | Desktop |
| --- | --- | --- |
| ![Mobile home](assets/responsiveness/mobile-home.png) | ![Tablet home](assets/responsiveness/tablet-home.png) | ![Desktop home](assets/responsiveness/desktop-home.png) |

### Events

| Mobile | Tablet | Desktop |
| --- | --- | --- |
| ![Mobile events](assets/responsiveness/mobile-events.png) | ![Tablet events](assets/responsiveness/tablet-events.png) | ![Desktop events](assets/responsiveness/desktop-events.png) |

### Event Detail

| Mobile | Tablet | Desktop |
| --- | --- | --- |
| ![Mobile event detail](assets/responsiveness/mobile-event-detail.png) | ![Tablet event detail](assets/responsiveness/tablet-event-detail.png) | ![Desktop event detail](assets/responsiveness/desktop-event-detail.png) |

### Register

| Mobile | Tablet | Desktop |
| --- | --- | --- |
| ![Mobile register](assets/responsiveness/mobile-register.png) | ![Tablet register](assets/responsiveness/tablet-register.png) | ![Desktop register](assets/responsiveness/desktop-register.png) |

### Login

| Mobile | Tablet | Desktop |
| --- | --- | --- |
| ![Mobile login](assets/responsiveness/mobile-login.png) | ![Tablet login](assets/responsiveness/tablet-login.png) | ![Desktop login](assets/responsiveness/desktop-login.png) |

### My Bookings

| Mobile | Tablet | Desktop |
| --- | --- | --- |
| ![Mobile My Bookings](assets/responsiveness/mobile-my-bookings.png) | ![Tablet My Bookings](assets/responsiveness/tablet-my-bookings.png) | ![Desktop My Bookings](assets/responsiveness/desktop-my-bookings.png) |


---

## Browser Compatibility

The deployed application should be checked in at least three browsers.

Recommended minimum:

- Google Chrome;
- Microsoft Edge;
- Mozilla Firefox.

| Browser | Core Navigation | Authentication | Booking | Layout | Result |
| --- | --- | --- | --- | --- | --- |
| Chrome | Test | Test | Test | Test | Add result |
| Edge | Test | Test | Test | Test | Add result |
| Firefox | Test | Test | Test | Test | Add result |

---

## Lighthouse Audit


The audits measured:

- **Performance**
- **Accessibility**
- **Best Practices**
- **SEO**


| Page | Device | Performance | Accessibility | Best Practices | SEO | Evidence |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| **Home** | Mobile | **98** | **92** | **100** | **90** | ![Mobile Home Lighthouse](assets/lighthouse/mobile-home.png) |
| **Events** | Mobile | **98** | **92** | **100** | **90** | ![Mobile Events Lighthouse](assets/lighthouse/mobile-events.png) |
| **Event Detail** | Mobile | **98** | **92** | **100** | **90** | ![Mobile Event Detail Lighthouse](assets/lighthouse/mobile-event-detail.png) |
| **Register** | Mobile | **98** | **94** | **100** | **90** | ![Mobile Register Lighthouse](assets/lighthouse/mobile-register.png) |
| **Login** | Mobile | **98** | **93** | **100** | **90** | ![Mobile Login Lighthouse](assets/lighthouse/mobile-login.png) |
| **Home** | Desktop | **100** | **85** | **100** | **90** | ![Desktop Home Lighthouse](assets/lighthouse/desktop-home.png) |
| **Events** | Desktop | **100** | **85** | **100** | **90** | ![Desktop Events Lighthouse](assets/lighthouse/desktop-events.png) |
| **Event Detail** | Desktop | **100** | **85** | **100** | **90** | ![Desktop Event Detail Lighthouse](assets/lighthouse/desktop-event-detail.png) |
| **Register** | Desktop | **100** | **94** | **100** | **90** | ![Desktop Register Lighthouse](assets/lighthouse/desktop-register.png) |
| **Login** | Desktop | **100** | **90** | **100** | **90** | ![Desktop Login Lighthouse](assets/lighthouse/desktop-login.png) |

Due to the limited timeframe of the hackathon, the team was unable to investigate and implement further improvements to the Lighthouse scores before submission. The results have therefore been documented as they were recorded during final testing. Areas such as accessibility and SEO could be reviewed and improved in future development iterations.

---

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) is used to validate final rendered HTML.

Because Django templates contain template syntax such as `{% url %}` and `{{ variable }}`, raw template files should not be pasted directly into the validator.

**Public pages:** validate the live deployed URL by URI.

**Authenticated pages:** open the deployed page while logged in, use **View Page Source**, copy the rendered HTML and validate using direct input.

| Page | Validation Method | Evidence | Result |
| --- | --- | --- | --- |
| Home | Live deployed URL | ![Home validation](assets/htmlhome.png) | PASS |
| Events | Live deployed URL | ![Events validation](assets/htmlevent.png) | PASS |
| Event Detail | URI / rendered source | ![view Events validation](assets/view-event-html.png) | PASS |
| Register | Live deployed URL | Add screenshot | Add result |
| Login | Live deployed URL | ![login ](assets/login-html.png) | PASS |
| My Bookings | Rendered source | ![my bookings ](assets/my-bookings-html.png) | PASS |
| Create / Edit / Delete | Rendered source while staff-authenticated | ![my bookings ](assets/admin-event-crud.png) | PASS |

---

## CSS Validation

The project's custom CSS is validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

Third-party Bootstrap CSS is not treated as project-authored code.

![CSS validation](assets/cssval.png)

**Result:** Add final validation result.

---

## Python Validation

Project-authored Python files are checked with Flake8 and/or the Code Institute Python Linter.

Example local command:

```bash
flake8 events venuenest manage.py --exclude=migrations,.venv,__pycache__ --max-line-length=88
```

Generated migration files and `__pycache__` files are excluded.

| File | Evidence | Result |
| --- | --- | --- |
| `events/admin.py` | ![admin.py](assets/adminpy.png) | PASS |
| `events/forms.py` | ![forms.py](assets/formspy.png) | PASS |
| `events/models.py` | ![models.py](assets/modelspy.png) | PASS |
| `events/urls.py` | ![urls.py](assets/urlspy.png) | PASS |
| `events/views.py` | ![views.py](assets/viewspy.png) | PASS |
| `venuenest/settings.py` | ![settings.py](assets/settingspy.png) | PASS |
| `venuenest/urls.py` | ![urls.py](assets/urlscipy.png) | PASS |
| `manage.py` | ![manage.py](assets/managepy.png) | PASS |


---

## Manual Accessibility Checks

Lighthouse provides automated accessibility checks, but a small amount of manual accessibility testing is also recommended.

Suggested checks:

- navigate key pages using only the keyboard;
- confirm focus indicators are visible;
- confirm form labels are associated with inputs;
- confirm buttons and links have meaningful text;
- confirm heading order is logical;
- confirm images have appropriate `alt` text.

Record the final outcome here before submission.

---

# Deployment & Local Development

## Heroku Deployment

The live application is deployed on [Heroku](https://venuenest-c59f0cde663d.herokuapp.com/).

VenueNest uses:

- PostgreSQL for the production database;
- Gunicorn as the production WSGI server;
- WhiteNoise for static files.

### Main Deployment Steps

1. Create a Heroku application.
2. Configure Heroku Config Vars:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `DEBUG=False`
3. Add production dependencies to `requirements.txt`:
   - `gunicorn`
   - `psycopg2-binary`
   - `whitenoise`
4. Add a root-level `Procfile`:

```text
web: gunicorn venuenest.wsgi
```

5. Add `.python-version`:

```text
3.14
```

6. Configure WhiteNoise and static files in `settings.py`.
7. Connect the Heroku app to the GitHub repository.
8. Deploy the `main` branch.
9. Run database migrations.
10. Verify application functionality and static files.

### Static Files

VenueNest uses Django's app-level static-file structure:

```text
events/
└── static/
    └── events/
        └── css/
            └── style.css
```

Production static files are collected and served by WhiteNoise.

### Local Development

Clone the repository:

```bash
git clone https://github.com/Azizr96/VenueNest.git
cd VenueNest
```

Create a virtual environment:

```bash
py -3.14 -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `env.py` beside `manage.py` with the required environment variables.

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Local development URL:

```text
http://127.0.0.1:8000/
```

---

## Credits

### Content

- **Django Documentation** — framework architecture, models, views, forms and routing.
- **Bootstrap Documentation** — responsive layout and reusable components.
- **Heroku Documentation** — deployment and environment configuration.
- **WhiteNoise Documentation** — production static-file configuration.
- **Code Institute** — course material, hackathon guidance and project-documentation structure.
- **ChatGPT** — debugging support, architectural explanation, development planning and documentation assistance.

### Media

Project screenshots, wireframes, validation evidence and Lighthouse results are stored in the project's documentation/assets folders.

### Acknowledgements

Special thanks to the entire VenueNest hackathon team for collaborating on development, Git/GitHub workflows, testing and integration.

Thanks also to the Code Institute team for their guidance and support throughout the hackathon.
