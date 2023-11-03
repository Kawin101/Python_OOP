# Encapsulation
class Employee:
    def __init__(self, name, salary, department):
        # Private Attribute
        self._name = name # Protected
        self.__salary = salary
        self.__department = department
        self.__showData()
    
    # Private Method
    def __showData(self):
        print("Name = {}".format(self._name))
        print("Salary = {}".format(self.__salary))
        print("Department = {}\n".format(self.__department))

# Object
obj1 = Employee("Green", 20000, "GM")
obj1._name = "Mary"
obj1.__salary = 120000
obj1.__department = "CEO"
