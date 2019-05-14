from eralchemy import render_er
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Boolean

metadata = MetaData()

Table(
    'roles',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(64), unique=True),
    Column('default', Boolean, default=False, index=True),
    Column('permissions', Integer())
)    
Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('email', String(64), unique=True, index=True),
    Column('username', String(64), unique=True, index=True),
    Column('password_hash', String(128)),
    Column('role_id', ForeignKey('roles.id')),
)

render_er(metadata, 'mymodel.png')

