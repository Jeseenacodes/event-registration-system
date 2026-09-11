from pathlib import Path
import sqlite3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Event Registration API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Location of our database
DATABASE = BASE_DIR / "event_registration.db"

# Location of our database schema
SCHEMA = BASE_DIR / "database" / "schema.sql"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_db()

    schema = SCHEMA.read_text(encoding="utf-8")
    connection.executescript(schema)

    # Add demo events if the database is empty
    event_count = connection.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    if event_count == 0:
        connection.execute(
            """
            INSERT INTO events (name, event_date, location)
            VALUES (?, ?, ?)
            """,
            (
                "AI for Community Organizations",
                "2026-10-15",
                "Seattle"
            )
        )

        connection.execute(
            """
            INSERT INTO events (name, event_date, location)
            VALUES (?, ?, ?)
            """,
            (
                "Responsible AI Workshop",
                "2026-11-05",
                "Virtual"
            )
        )

    connection.commit()
    connection.close()


initialize_database()


class RegistrationRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    organization: str | None = None
    event_id: int


@app.get("/")
def home():
    return {"message": "Event Registration API is running"}


@app.get("/api/events")
def get_events():

    connection = get_db()

    events = connection.execute(
        """
        SELECT event_id, name, event_date, location
        FROM events
        ORDER BY event_date
        """
    ).fetchall()

    connection.close()

    return [dict(event) for event in events]


@app.post("/api/registrations")
def create_registration(request: RegistrationRequest):

    connection = get_db()

    # Check that the event exists
    event = connection.execute(
        """
        SELECT event_id
        FROM events
        WHERE event_id = ?
        """,
        (request.event_id,)
    ).fetchone()

    if event is None:
        connection.close()
        return {"error": "Event not found"}

    # Add participant
    connection.execute(
        """
        INSERT OR IGNORE INTO participants
        (first_name, last_name, email, organization)
        VALUES (?, ?, ?, ?)
        """,
        (
            request.first_name,
            request.last_name,
            request.email,
            request.organization
        )
    )

    # Find participant ID
    participant = connection.execute(
        """
        SELECT participant_id
        FROM participants
        WHERE email = ?
        """,
        (request.email,)
    ).fetchone()

    # Create registration
        # Create registration
    try:
        cursor = connection.execute(
            """
            INSERT INTO registrations
            (participant_id, event_id, registration_date, status)
            VALUES (?, ?, datetime('now'), 'confirmed')
            """,
            (
                participant["participant_id"],
                request.event_id
            )
        )

    except sqlite3.IntegrityError:
        connection.close()

        return {
            "error": "You are already registered for this event."
        }

    connection.commit()

    registration_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Registration successful",
        "registration_id": registration_id
    }


@app.get("/api/events/{event_id}/registrations")
def get_event_registrations(event_id: int):

    connection = get_db()

    registrations = connection.execute(
        """
        SELECT
            registrations.registration_id,
            participants.first_name,
            participants.last_name,
            participants.email,
            participants.organization,
            registrations.registration_date,
            registrations.status
        FROM registrations
        JOIN participants
            ON registrations.participant_id = participants.participant_id
        JOIN events
            ON registrations.event_id = events.event_id
        WHERE registrations.event_id = ?
        ORDER BY registrations.registration_date
        """,
        (event_id,)
    ).fetchall()

    connection.close()

    return [dict(registration) for registration in registrations]