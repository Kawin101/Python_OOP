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
obj2 = Employee("Mary", 98000, "CEO")
obj3 = Employee("Baby", 25000, "Coder")

# Is obj1 of class Employee?
# print(isinstance(obj1, Employee))
# print(dir(obj1))
print(obj1.__class__)
