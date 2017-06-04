from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from app.models import Person, Desk, Location


admin = Admin(app)
admin.add_view(ModelView(Location, db.session))
admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Desk, db.session))
