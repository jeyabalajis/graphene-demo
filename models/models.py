from sqlalchemy import *
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
)
from sqlalchemy.ext.declarative import declarative_base
from db_utils.db_session_maker import get_db_session

db_session = get_db_session()

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer)
    name = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        {},
    )


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer)
    name = Column(String)
    hired_on = Column(DateTime)
    department_id = Column(Integer)

    department = relationship(
        Department,
        backref=backref('employee',
                        uselist=True,
                        cascade='delete,all'))

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        ForeignKeyConstraint(
            (department_id,),
            [Department.id]
        ),
        {},
    )
