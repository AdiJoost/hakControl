import os
import requests
from models.employee_model import EmployeeModel

user = os.environ.get("HAKUSER")
personell_auth_token = os.environ.get("PERSHAKAUTH")
organisation_auth_token = os.environ.get("ORGHAKAUTH") 

def update_all ():
    hdr = {
        "X-Auth-Token": personell_auth_token,
        "Host": user
        }
    request = requests.get(f"https://{user}/api/v1/users", headers=hdr)
    employees = get_employees(request.json())
    for employee in employees:
        update_employee(employees[employee])
        
    return(employees)

def get_employees (data):
    return_dict = {}
    for element in data:
        return_dict[element["id"]] = {"_id": element["id"],
                                      "name": element["name"],
                                      "email": element["email"]}
    return return_dict

def update_employee(employee):
    new_employee = EmployeeModel.get(employee["_id"])
    if not new_employee:
        new_employee = EmployeeModel(**employee)
        new_employee.save()
        return True
    
    new_employee.name = employee["name"]
    new_employee.email = employee["email"]
    new_employee.save()
    
    return True