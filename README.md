# Event Registration System

A small learning project that demonstrates how a frontend, API, database, and GitHub work together to support nonprofit event registration.

## Project Overview

The Event Registration System allows participants to:

- View available events
- Register for an event
- Receive a registration confirmation
- Prevent duplicate registrations

The project is designed as a learning reference rather than a production application.

## Problem

A nonprofit organization needs a simple way to manage event registrations.

The system needs to answer:

- What events are available?
- Who registered?
- Which event did they register for?
- How do we prevent duplicate registrations?
- How does the frontend communicate with the backend?
- Where is registration data stored?

## Architecture

The system has three main layers:

```text
Frontend
    |
    | HTTP / JSON
    v
FastAPI Backend
    |
    | SQL
    v
SQLite Database
````

### Frontend

Location:

`frontend/index.html`

The frontend provides the registration form and communicates with the API using JavaScript `fetch()` requests.

### Backend

Location:

`backend/main.py`

The backend uses FastAPI to provide API endpoints and handle business logic.

### Database

Location:

`event_registration.db`

The application uses SQLite for local development.

The database contains three tables:

* `participants`
* `events`
* `registrations`

## Database Relationships

```text
participants
      |
      | participant_id
      v
registrations
      ^
      | event_id
      |
    events
```

A participant can register for multiple events.

An event can have multiple participants.

The `registrations` table connects participants and events.

A unique constraint prevents the same participant from registering for the same event more than once.

## API Endpoints

### Get Events

```text
GET /api/events
```

Returns the available events.

### Create Registration

```text
POST /api/registrations
```

Creates a participant registration.

Example request:

```json
{
  "first_name": "Jordan",
  "last_name": "Lee",
  "email": "jordan@example.com",
  "organization": "Community AI",
  "event_id": 1
}
```

### Get Event Registrations

```text
GET /api/events/{event_id}/registrations
```

Returns participants registered for a specific event.

Example:

```text
GET /api/events/1/registrations
```

## Technology Stack

* Python
* FastAPI
* SQLite
* HTML
* JavaScript
* Git
* GitHub

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd event-registration-system
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install fastapi uvicorn
```

### 5. Start the API

```powershell
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Testing the Application

### Test the events API

Open:

```text
http://127.0.0.1:8000/api/events
```

### Test the registration API

Use the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Test the frontend

Open:

```text
frontend/index.html
```

The frontend should load the available events from the API.

## Business Rules

The system currently includes these rules:

1. An event must exist before someone can register.
2. A participant is identified by their email address.
3. A participant cannot register for the same event twice.
4. Registration status defaults to `confirmed`.

## Git Workflow

The project uses a basic Git workflow:

```text
Make changes
     |
     v
git status
     |
     v
git add .
     |
     v
git commit
     |
     v
git push
     |
     v
GitHub
```

## Project Documentation

Additional project documentation is located in the `docs` directory.

* `PRD.md` - Product requirements
* `architecture.md` - System architecture
* `api.md` - API design
* `github-plan.md` - GitHub project plan
* `capstone.md` - Learning/capstone exercise

## Known Limitations

This project is intentionally simple and is not production-ready.

Current limitations include:

* SQLite is used for local development.
* Authentication is not implemented.
* Authorization is not implemented.
* Email notifications are not implemented.
* API error responses could be improved.
* The frontend is a simple HTML page.
* CORS is configured broadly for local learning.

## Future Improvements

Possible future features include:

* Participant login
* Admin dashboard
* Event creation and editing
* Registration cancellation
* Email confirmation
* Event capacity limits
* Registration reporting
* Production database
* Authentication and authorization
* Automated tests
* Deployment

## Learning Goals

This project demonstrates the relationship between:

```text
Requirements
     ↓
Architecture
     ↓
Database
     ↓
APIs
     ↓
Frontend
     ↓
Testing
     ↓
GitHub
```

The goal is to understand how the pieces of a technical ecosystem work together, not simply to write code.


