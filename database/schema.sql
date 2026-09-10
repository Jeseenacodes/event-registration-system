PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS participants (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    organization TEXT
);

CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    registration_date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'confirmed',

    FOREIGN KEY (participant_id)
        REFERENCES participants(participant_id),

    FOREIGN KEY (event_id)
        REFERENCES events(event_id),

    UNIQUE(participant_id, event_id)
);
