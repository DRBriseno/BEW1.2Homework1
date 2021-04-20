"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref, create_session


# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    events_attending = db.relationship('event_attending', back_populates='event')

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_and_time = db.Column(db.String(80), nullable=False)
    guests = db.relationship('guest', back_populates='event')


# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)



guest_event_table = None
create_session TABLE guest_event_table (
   event_id INTEGER NOT NULL,
   guest_id  INTEGER NOT NULL,
   FOREIGN KEY (event_id) REFERENCES Event(id),
   FOREIGN KEY (guest_id) REFERENCES Guest(id)
);




