from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
location = Table('location', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('alias', String(length=8)),
    Column('street_address', String(length=120)),
    Column('city', String(length=120)),
    Column('state', String(length=120)),
    Column('country', String(length=120)),
    Column('zip', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['location'].columns['alias'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['location'].columns['alias'].drop()
