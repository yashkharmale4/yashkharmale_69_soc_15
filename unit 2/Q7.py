class person :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def show_employee(self):
        print("Employee Id:",self.emp_id)
        print("Salary:",self.salary) 

class manager(person,Employee):
    def __init__(self,name,age,emp_id,salary,departnment):
     person.__init__(self,name,age)
     Employee.__init__(self,emp_id,salary)
     self.departnment=departnment
    def show_manager(self):
        print("Deparment:",self.departnment)

m1=manager("Rahul",25,123,75000,"IT")
m1.show_person()
m1.show_employee()
m1.show_manager()