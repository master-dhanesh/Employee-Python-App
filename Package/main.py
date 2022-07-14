import json
from pathlib import Path
import random
import string


class Employee:
    __database = "Package/employee.json"
    __employee = []

    try:
        if not Path(__database).exists():
            with open(__database, 'w') as fw:
                fw.write(json.dumps(__employee))
        else:
            with open(__database, 'r') as fr:
                __employee = json.loads(fr.read())
    except Exception as err:
        print("ERROR >> ", err)

    @classmethod
    def UpdateData(cls):
        try:
            with open(cls.__database, 'r') as fr:
                cls.__employee = json.loads(fr.read())
        except Exception as err:
            print("ERROR >> ", err)

    def __str__(self):
        return "CAN NOT ACCESS DATA DIRECTLY."

    def RegisteredEmployees(self):
        return self.__employee

    def __generateid(self):
        seq1 = (random.choices(string.ascii_letters, k=5))
        seq2 = (random.choices(string.digits, k=2))
        seq3 = (random.choices(list('@#$*'), k=1))
        x = seq1 + seq2 + seq3
        random.shuffle(x)
        return ("".join(x))

    @classmethod
    def ShowAllEmployee(cls):
        return cls.__employee

    def CreateEmp(self):
        try:
            emp = {}
            emp["id"] = self.__generateid()
            emp["name"] = input("Enter Employe Name: ")
            emp["email"] = input("Enter Employe Email: ")
            emp["designation"] = input("Enter Employe Designation: ")
            Employee.__employee.append(emp)

            with open(Employee.__database, 'w') as fw:
                fw.write(json.dumps(Employee.__employee))

            Employee.UpdateData()
            return f"{emp['name']} WITH ID {emp['id']} REGIASTERED SUCCESSFULLY!"
        except Exception as err:
            print("ERROR >> ", err)

    def ReadSingleEmp(self):
        try:
            id = input("Enter Employe Id: ")
            for i, v in enumerate(Employee.__employee):
                if v['id'] == id:
                    return f"Employe Information >> {v}"
            return "EMPLOYEE NOT FOUND!"
        except Exception as err:
            print("ERROR >> ", err)

    def ReadAllEmp(self):
        try:
            return Employee.__employee
        except Exception as err:
            print("ERROR >> ", err)

    def DeleteEmp(self):
        try:
            id = input("Enter Employe Id: ")
            filteredemps = [
                emp for emp in Employee.__employee if emp['id'] != id]
            with open(Employee.__database, 'w') as fw:
                fw.write(json.dumps(filteredemps))

            Employee.UpdateData()
            return "Employee Deleted!"
        except Exception as err:
            print("ERROR >> ", err)

    def UpdateEmp(self):
        try:
            id = input("Enter Employe Id: ")
            for i, v in enumerate(Employee.__employee):
                if id == v["id"]:
                    print("SKIP BY PRESSING ENTER ")
                    updatedemp = {}
                    updatedemp['name'] = input("Enter Updated Employe Name: ")
                    updatedemp['email'] = input(
                        "Enter Updated Employe Email: ")
                    updatedemp['designation'] = input(
                        "Enter Updated Employe Designation: ")

                    if not updatedemp['name'].strip():
                        del updatedemp['name']
                    if not updatedemp['email'].strip():
                        del updatedemp['email']
                    if not updatedemp['designation'].strip():
                        del updatedemp['designation']

                    Employee.__employee[i] = {**v, **updatedemp}

                    with open(Employee.__database, 'w') as fw:
                        fw.write(json.dumps(Employee.__employee))

                    Employee.UpdateData()

                    return f"EMPLOYEE WITH ID {v['id']} HAS BEEN UPDATED SUCCESSFULLY!"
            return "EMPLOYEE NOT FOUND!"
        except Exception as err:
            print("ERROR >> ", err)


emp = Employee()
CreateEmp = emp.CreateEmp
UpdateEmp = emp.UpdateEmp
ReadSingleEmp = emp.ReadSingleEmp
DeleteEmp = emp.DeleteEmp
ReadAllEmp = emp.ReadAllEmp

while(True):
    print("1. Create Employee")
    print("2. Read Single Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("0. Exit Application")
    try:
        n = int(input("Enter Your Choice: "))
        if n == 1:
            print(CreateEmp())
        elif n == 2:
            print(ReadSingleEmp())
        elif n == 3:
            print(UpdateEmp())
        elif n == 4:
            print(DeleteEmp())
        elif n == 69:
            print(ReadAllEmp())
        elif n == 0:
            print("APPLICATION CLOSED!")
            exit(0)
    except Exception as err:
        print("ERROR >>", err)
