import graphene
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

from models.models import Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node,)


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    # all_employees = SQLAlchemyConnectionField(EmployeeConnections)
    params = dict(limit=graphene.Int(), offset=graphene.Int())
    all_employees = graphene.List(lambda: Employee, **params)
    # Disable sorting over this field
    # all_departments = SQLAlchemyConnectionField(DepartmentConnection)
    all_departments = graphene.List(lambda: Department, limit=graphene.Int(), offset=graphene.Int())

    find_employee_by_name = graphene.List(lambda: Employee, name=graphene.String())

    def resolve_find_employee_by_name(self, info, **args):
        name = args.get("name")
        employee_query = Employee.get_query(info)

        employees = employee_query.filter(EmployeeModel.name.contains(name)).all()

        return employees

    def resolve_all_employees(self, info, **args):
        limit = args.get("limit")

        employee_query = Employee.get_query(info)

        employees = employee_query.filter().limit(limit)

        return employees

    def resolve_all_departments(self, info, **args):
        limit = args.get("limit")

        department_query = Department.get_query(info)

        departments = department_query.filter().limit(limit)

        return departments


schema = graphene.Schema(query=Query)
