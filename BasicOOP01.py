# Make a Class
class Employee:
    # Make a Method
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
        print("Department = {}\n".format(self.department))

# Object
obj1 = Employee("Green", 50000, "GM")
obj1.name = "kawin101"
obj1.salary = 700000
obj1.showData()

obj2 = Employee("Mary", 98000, "CEO")
obj2.showData()

obj3 = Employee("Baby", 25000, "Coder")
obj3.showData()