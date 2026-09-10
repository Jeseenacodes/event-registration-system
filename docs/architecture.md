# Event Registration System Architecture

## 1. Overview

The Event Registration System allows participants to register for nonprofit events.

The basic flow is:

**Participant → Registration Form → API → Database → Integrations → Reporting**

GitHub is used by the team to manage the development work, code, documentation, and collaboration.

---

## 2. High-Level Architecture

```text
                    PARTICIPANT
                         |
                         v
                +------------------+
                | Registration Form|
                +--------+---------+
                         |
                         | API Request
                         v
                +------------------+
                |       API        |
                |     FastAPI      |
                +--------+---------+
                         |
                         v
                +------------------+
                |     DATABASE     |
                |                  |
                | Participants     |
                | Events           |
                | Registrations    |
                +--------+---------+
                         |
                 +-------+-------+
                 |               |
                 v               v
          +------------+   +------------+
          |   Email    |   | Reporting  |
          | Integration|   | / Analytics|
          +------------+   +------------+
```

---

## 3. What Each Component Does

### Registration Form

The participant enters their information:

* First name
* Last name
* Email
* Organization
* Event

The form sends this information to the API.

### API

The API receives the registration request.

It is responsible for:

* Receiving data
* Validating data
* Checking whether the event exists
* Checking for duplicate registrations
* Saving the registration
* Returning a response

### Database

The database stores the organization's structured information.

The initial database contains three main tables:

* Participants
* Events
* Registrations

### Integrations

The registration system can communicate with other systems.

For the MVP, we will demonstrate an email integration.

After a successful registration, the system triggers a confirmation email.

### Reporting

Registration data can eventually be used for reporting and analytics.

Examples:

* Number of registrations
* Registrations by event
* Registrations by organization
* Attendance trends

---

## 4. GitHub's Role

GitHub is part of the development and collaboration process.

It is not part of the participant's runtime data flow.

The team uses GitHub to manage:

```text
GitHub Issue
     |
     v
Development Task
     |
     v
Branch
     |
     v
Code Changes
     |
     v
Pull Request
     |
     v
Code Review
     |
     v
Merge
```

GitHub also stores project documentation such as the PRD, architecture documentation, database schema, and API specification.

---

## 5. Example Registration Flow

When a participant clicks **Register**:

1. The participant submits the form.
2. The frontend creates an API request.
3. The API receives the request.
4. The API validates the information.
5. The API checks whether the event exists.
6. The API checks whether the participant is already registered.
7. The database stores the registration.
8. The email integration is triggered.
9. The participant receives confirmation.
10. The registration becomes available for reporting.

---

## 6. Key Technical Concepts

This project demonstrates five foundational concepts:

**GitHub**
Where we manage and collaborate on the technical work.

**API**
How systems communicate with each other.

**Database**
Where structured organizational information is stored.

**Integration**
How different systems connect and exchange information.

**Architecture**
How all of these pieces fit together.

---

## 7. Future Improvements

A production version could eventually include:

* PostgreSQL instead of SQLite
* User authentication
* Role-based permissions
* A real email service
* Automated tests
* Monitoring and logging
* Data privacy and retention controls
* Automated deployment
* Analytics dashboards

These are intentionally outside the first version of the project.
