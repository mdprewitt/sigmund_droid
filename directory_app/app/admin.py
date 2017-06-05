from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from app.models import Person, Desk, Location


class PersonView(ModelView):
    """ custom Person view to show desk """
    column_list = ('sid', 'first', 'last', 'desk')

    def __init__(self, session, **kwargs):
        super(PersonView, self).__init__(Person, session, **kwargs)


admin = Admin(app)
admin.add_view(ModelView(Location, db.session))
admin.add_view(PersonView(db.session))
admin.add_view(ModelView(Desk, db.session))
