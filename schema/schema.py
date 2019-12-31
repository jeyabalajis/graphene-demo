import graphene
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import and_
from database.models import Department as DepartmentModel, Employee as EmployeeModel


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
    params = dict(limit=graphene.Int(), offset=graphene.Int())

    all_departments = graphene.List(lambda: Department, **params)

    all_employees = graphene.List(lambda: Employee, **params)

    def resolve_all_departments(self, info, **args):
        limit = args.get("limit")
        offset = args.get("offset")
        department_query = Department.get_query(info)

        departments = department_query.filter().limit(limit)

        return departments

    def resolve_all_employees(self, info, **args):
        limit = args.get("limit")
        offset = args.get("offset")
        employee_query = Employee.get_query(info)

        employees = employee_query.filter().limit(limit)

        return employees

    query_params_dict = dict()

    query_params_dict["id_gte"] = graphene.Int()
    query_params_dict["id_lte"] = graphene.Int()
    query_params_dict["id_gt"] = graphene.Int()
    query_params_dict["id_lt"] = graphene.Int()

    query_params_dict["name_in"] = graphene.List(graphene.String)
    query_params_dict["name_like"] = graphene.String()
    query_params_dict["name_eq"] = graphene.String()
    query_params_dict["name_neq"] = graphene.String()

    query_params_dict["limit"] = graphene.Int()
    search_departments = graphene.List(lambda: Department, **query_params_dict)

    def resolve_search_departments(self, info, **args):

        filter_criteria = []

        id_gte = args.get("id_gte")

        if id_gte:
            filter_criteria.append(DepartmentModel.id >= id_gte)

        id_lte = args.get("id_lte")

        if id_lte:
            filter_criteria.append(DepartmentModel.id <= id_lte)

        id_gt = args.get("id_gt")

        if id_gt:
            filter_criteria.append(DepartmentModel.id > id_gt)

        id_lt = args.get("id_lt")

        if id_lt:
            filter_criteria.append(DepartmentModel.id < id_lt)

        name_in = args.get("name_in")

        if name_in:
            filter_criteria.append(DepartmentModel.name.in_(name_in))

        name_like = args.get("name_like")

        if name_like:
            filter_criteria.append(DepartmentModel.name.contains(name_like))

        name_eq = args.get("name_eq")

        if name_eq:
            filter_criteria.append(DepartmentModel.name == name_eq)

        name_neq = args.get("name_neq")

        if name_neq:
            filter_criteria.append(DepartmentModel.name != name_neq)

        limit = args.get("limit")

        filter_rule = and_(*filter_criteria)

        department_query = Department.get_query(info)

        departments = department_query.filter(filter_rule).limit(limit)

        return departments

    query_params_dict = dict()

    query_params_dict["id_gte"] = graphene.Int()
    query_params_dict["id_lte"] = graphene.Int()
    query_params_dict["id_gt"] = graphene.Int()
    query_params_dict["id_lt"] = graphene.Int()

    query_params_dict["name_in"] = graphene.List(graphene.String)
    query_params_dict["name_like"] = graphene.String()
    query_params_dict["name_eq"] = graphene.String()
    query_params_dict["name_neq"] = graphene.String()

    query_params_dict["hiredOn_gte"] = graphene.DateTime()
    query_params_dict["hiredOn_lte"] = graphene.DateTime()
    query_params_dict["hiredOn_gt"] = graphene.DateTime()
    query_params_dict["hiredOn_lt"] = graphene.DateTime()

    query_params_dict["limit"] = graphene.Int()
    search_employees = graphene.List(lambda: Employee, **query_params_dict)

    def resolve_search_employees(self, info, **args):

        filter_criteria = []

        id_gte = args.get("id_gte")

        if id_gte:
            filter_criteria.append(EmployeeModel.id >= id_gte)

        id_lte = args.get("id_lte")

        if id_lte:
            filter_criteria.append(EmployeeModel.id <= id_lte)

        id_gt = args.get("id_gt")

        if id_gt:
            filter_criteria.append(EmployeeModel.id > id_gt)

        id_lt = args.get("id_lt")

        if id_lt:
            filter_criteria.append(EmployeeModel.id < id_lt)

        name_in = args.get("name_in")

        if name_in:
            filter_criteria.append(EmployeeModel.name.in_(name_in))

        name_like = args.get("name_like")

        if name_like:
            filter_criteria.append(EmployeeModel.name.contains(name_like))

        name_eq = args.get("name_eq")

        if name_eq:
            filter_criteria.append(EmployeeModel.name == name_eq)

        name_neq = args.get("name_neq")

        if name_neq:
            filter_criteria.append(EmployeeModel.name != name_neq)

        hiredOn_gte = args.get("hiredOn_gte")

        if hiredOn_gte:
            filter_criteria.append(EmployeeModel.hired_on >= hiredOn_gte)

        hiredOn_lte = args.get("hiredOn_lte")

        if hiredOn_lte:
            filter_criteria.append(EmployeeModel.hired_on <= hiredOn_lte)

        hiredOn_gt = args.get("hiredOn_gt")

        if hiredOn_gt:
            filter_criteria.append(EmployeeModel.hired_on > hiredOn_gt)

        hiredOn_lt = args.get("hiredOn_lt")

        if hiredOn_lt:
            filter_criteria.append(EmployeeModel.hired_on < hiredOn_lt)

        limit = args.get("limit")

        filter_rule = and_(*filter_criteria)

        employee_query = Employee.get_query(info)

        employees = employee_query.filter(filter_rule).limit(limit)

        return employees


schema = graphene.Schema(query=Query)
