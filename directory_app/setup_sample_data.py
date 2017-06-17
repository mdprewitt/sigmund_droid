#!/usr/bin/env python3
from app import app, db
from app.models import Person, Desk, Location
import sqlalchemy.exc

db.create_all()


def get_person(sid, first, last):
    person = Person.query.filter_by(sid=sid).one_or_none() or Person()
    person.first = first
    person.last = last
    person.sid = sid
    return person


def get_desk(person, alias, location_x, location_y, floor, location):
    desk = Desk.query.filter_by(alias=alias).one_or_none() or Desk()
    desk.person = person
    desk.location = location
    desk.alias = alias
    desk.location_x = location_x
    desk.location_y = location_y
    desk.floor = floor
    return desk


loc = Location.query.filter_by(alias='XYZ1').one_or_none() or Location()
loc.alias = 'XYZ1'
loc.street_address = '123 Main Street'
loc.city = 'Centerville'
loc.state = 'NY'
loc.zip = '10000'
loc.country = 'US'

people = {
    '1':
        dict(
            first='Conference',
            last='Room A',
            sid='1',
            location=loc,
            alias='100W1',
            location_x=150,
            location_y=50,
            floor=21,
        ),
    '2':
        dict(
            first='Jane',
            last='Smith',
            sid='2',
            location=loc,
            alias='100W2',
            location_x=30,
            location_y=-20,
            floor=21,
        ),
    '3':
        dict(
            first='Your Private Client',
            last='Advisor',
            sid='3',
            location=loc,
            alias='100W3',
            location_x=85,
            location_y=-20,
            floor=21,
        ),
    '4':
        dict(
            first='Jose',
            last='Chavez',
            sid='4',
            location=loc,
            alias='100W4',
            location_x=30,
            location_y=-20,
            floor=21,
        ),
    '5':
        dict(
            first='Conswayla',
            last='Montoya',
            sid='5',
            location=loc,
            alias='100W5',
            location_x=85,
            location_y=50,
            floor=21,
        ),
    '6':
        dict(
            first='Kurt',
            last='Vonnegut',
            sid='6',
            location=loc,
            alias='100W6',
            location_x=30,
            location_y=-20,
            floor=21,
        ),
    '7':
        dict(
            first='Jane',
            last='Austin',
            sid='7',
            location=loc,
            alias='100W7',
            location_x=30,
            location_y=-20,
            floor=21,
        ),
}
for _, person in people.items():
    p_obj = get_person(person['sid'], person['first'], person['last'])
    desk_obj = get_desk(
        alias=person['alias'],
        person=p_obj,
        location=person['location'],
        location_x=person['location_x'],
        location_y=person['location_y'],
        floor=person['floor'],
    )
    db.session.add(desk_obj)
db.session.commit()
