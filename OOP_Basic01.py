# Make a Class
class Employee:
    # Make a Method
    def detail(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def displayData(self):
        print("\nName = {}".format(self.name))
        print("Salary = {}".format(self.salary))
        print("Department = {}\n".format(self.department))


# Object
obj1 = Employee()
obj1.detail("Green", 50000, "GM")

obj2 = Employee()
obj2.detail("Mary", 98000, "CEO")

obj3 = Employee()
obj3.detail("Baby", 25000, "Coder")

obj1.displayData()
obj2.displayData()
obj3.displayData()
