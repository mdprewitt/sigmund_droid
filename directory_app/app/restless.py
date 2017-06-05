import flask_restless as restless
from app import app, db
from app.models import Location, Person, Desk
# Create the Flask-Restless API manager.
manager = restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Person, methods=['GET'])
manager.create_api(Desk, methods=['GET'])
manager.create_api(Location, methods=['GET'])
