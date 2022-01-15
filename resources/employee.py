from flask_restful import Resource
from models.employee_model import EmployeeModel
from utilities import create_response, employee_post_parser
import hakuna_lib

class Employee(Resource):
    
    def get (self, param):
        employee = EmployeeModel.get(param)
        if employee:
            return create_response(employee.to_json(), 200)
        else:
            return create_response({"message": "Employee not found"}, 404)
        
    def post(self, param):
        employee = EmployeeModel.get(param)
        if not employee:
            return create_response({"message":f"Employee with id {param} does not exist"}, 404)
        parser = employee_post_parser()
        data = parser.parse_args()
        employee.monday = data["monday"]
        employee.tuesday = data["tuesday"]
        employee.wednesday = data["wednesday"]
        employee.thursday = data["thursday"]
        employee.friday = data["friday"]
        employee.save()
        return create_response({"message": "employee updated", "employee": employee.to_json()}, 200)
        
    
    
class Employees(Resource):
    
    def get(self):
        employees = EmployeeModel.get_all()
        body = {}
        for employee in employees:
            body[employee._id] = employee.to_json()
        return create_response(body, 200)
    
    def post (self):
        body = hakuna_lib.update_all()
        return create_response(body, 200)