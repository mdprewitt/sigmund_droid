from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(7), index=True, unique=True)
    last = db.Column(db.String(120))
    first = db.Column(db.String(120))

    def __repr__(self):
        return '<Person %r>' % self.sid


class Desk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location', backref=db.backref('desk', lazy='dynamic'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', backref=db.backref('desk', lazy='dynamic'))
    floor = db.Column(db.String(20))
    location_x = db.Column(db.Integer)
    location_y = db.Column(db.Integer)

    def __repr__(self):
        return '<Desk {f}-({x}, {y})>'.format(
            f=self.floor,
            x=self.location_x,
            y=self.location_y,
        )


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))
    zip = db.Column(db.String(120))

    def __repr__(self):
        return '<Building {s}-({c}, {st} {z}, {cn})>'.format(
            s=self.street_address,
            c=self.city,
            st=self.state,
            z=self.zip,
            cn=self.country,
        )
