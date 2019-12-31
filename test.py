from database.models import db_session, Base, Department, Employee
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
Base.metadata.create_all(bind=engine)

# Fill the tables with some data
# engineering = Department(name='Engineering')
# db_session.add(engineering)
hr = Department(name='Human Resources')
# db_session.add(hr)
#
# peter = Employee(name='Peter', department=engineering)
# db_session.add(peter)
# roy = Employee(name='Roy', department=engineering)
# db_session.add(roy)
# tracy = Employee(name='Tracy', department=hr)
# db_session.add(tracy)

tracy = Employee(name='Srinivasa Modalavalasa', department=hr)
db_session.add(tracy)
tracy = Employee(name='Venkata Vangi Varapu', department=hr)
db_session.add(tracy)
tracy = Employee(name='Jagarlapudi Channamma', department=hr)
db_session.add(tracy)

db_session.commit()
