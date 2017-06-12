#!/usr/bin/env python3
from app import app, db
from app.models import Person, Desk, Location
import sqlalchemy.exc

db.create_all()

person1 = Person(
    first='Joe',
    last='Doe',
    sid='a123456',
)
person2 = Person(
    first='Jane',
    last='Smith',
    sid='b123456',
)
person3 = Person(
    first='Bob',
    last='Center',
    sid='c123456',
)
person4 = Person(
    first='Jose',
    last='Chavez',
    sid='d123456',
)
person5 = Person(
    first='Consuela',
    last='Montoya',
    sid='e123456',
)
person6 = Person(
    first='Kurt',
    last='Vonnegut',
    sid='f123456',
)
person7 = Person(
    first='Jane',
    last='Austin',
    sid='g123456',
)
main = Location(
    street_address='123 Main Street',
    city='Centerville',
    state='NY',
    zip='10000',
    country='US',
)
desk1 = Desk(
    location=main,
    alias='100W1',
    location_x=30,
    location_y=20,
    floor=21,
    person=person1,
)
desk2 = Desk(
    location=main,
    alias='100W2',
    location_x=30,
    location_y=-20,
    floor=21,
    person=person2,
)
desk3 = Desk(
    location=main,
    alias='100W2',
    location_x=30,
    location_y=-20,
    floor=21,
    person=person3,
)
desk4 = Desk(
    location=main,
    alias='100W2',
    location_x=30,
    location_y=-20,
    floor=21,
    person=person4,
)
desk5 = Desk(
    location=main,
    alias='100W2',
    location_x=30,
    location_y=-20,
    floor=21,
    person=person5,
)
desk6 = Desk(
    location=main,
    alias='100W2',
    location_x=30,
    location_y=-20,
    floor=21,
    person=person6,
)
desk7 = Desk(
    location=main,
    alias='100W2',
    location_x=30,
    location_y=-20,
    floor=21,
    person=person7,
)
for obj in [main,
            person1, person2, person3, person4, person5, person6, person7,
            desk1, desk2, desk3, desk4, desk5, desk6, desk7]:
    try:
        db.session.add(obj)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
