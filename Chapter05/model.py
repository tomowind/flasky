from eralchemy import render_er
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

Table(
    'roles',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(64), unique=True),
)    
Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('username', String(64), unique=True, index=True),
    Column('role_id', ForeignKey('roles.id')),
)

render_er(metadata, 'mymodel.png')
