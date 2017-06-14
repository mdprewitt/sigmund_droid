from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sid', String(length=7)),
    Column('last', String(length=120)),
    Column('first', String(length=120)),
    Column('color', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['color'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['color'].drop()
