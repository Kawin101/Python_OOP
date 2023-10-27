# Make The Class
class Employee:
    # Make The Method
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        self.nickname = nickname

    def displayData(self):
        print("\nName = {}".format(self.name))
        print("Salary = {}".format(self.salary))
        print("Department = {}\n".format(self.department))
        print("Nickname = {}\n".format(self.nickname))


# Make The Object
obj1 = Employee()
obj1.detail("Green", 50000, "GM", "The End")

obj2 = Employee()
obj2.detail("Mary", 98000, "CEO", "No.1")

obj3 = Employee()
obj3.detail("Baby", 25000, "Coder", "No.2")

obj4 = Employee()
obj3.detail("Call me, Lufy", 30000000, "Capt", "I gonna be King of the Pirates")

