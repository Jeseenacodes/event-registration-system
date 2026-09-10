PRAGMA foreign_keys = ON;

CREATE TABLE participants (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    organization TEXT
);

CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    registration_date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'confirmed',

    FOREIGN KEY (participant_id) REFERENCES participants(participant_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id),

    UNIQUE(participant_id, event_id)
);

┌─────────────────┐
│   PARTICIPANTS  │
│                 │
│ participant_id  │
│ first_name      │
│ last_name       │
│ email           │
│ organization    │
└────────┬────────┘
         │
         │ 1
         │
         │ many
         ▼
┌─────────────────┐
│  REGISTRATIONS  │
│                 │
│ registration_id │
│ participant_id  │
│ event_id        │
│ date            │
│ status          │
└────────┬────────┘
         │
         │ many
         │
         │ 1
         ▼
┌─────────────────┐
│      EVENTS     │
│                 │
│ event_id        │
│ name            │
│ event_date      │
│ location        │
└─────────────────┘
