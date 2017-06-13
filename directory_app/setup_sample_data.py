#!/usr/bin/env python3
from app import app, db
from app.models import *
import sqlalchemy.exc

db.create_all()

person1 = Person(
    first='Joe',
    last='Doe',
    sid='a123456',
    color='Red'
)
person2 = Person(
    first='Jane',
    last='Smith',
    sid='b123456',
    color='Red'
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
for obj in [main, person1, person2, desk1, desk2]:
    try:
        db.session.add(obj)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
