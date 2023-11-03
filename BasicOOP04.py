# Encapsulation
class Employee:
    def __init__(self, name, salary, department):
        # Private Attribute
        self.__name = name 
        self.__salary = salary
        self.__department = department
    
    # Private Method
    def _showData(self):
        print("Name = "+self.getName())
        print("Salary = ",format(self.getSalary()))
        print("Department = "+self.getDepartment())

    # Setter Method
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, department):
        self.__department = department

    # Getter Method
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

# Object
obj1 = Employee("Green", 20000, "GM")
obj1._showData()
