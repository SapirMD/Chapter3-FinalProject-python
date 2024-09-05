from Person import Person
import utilities as utils
import os

class Employee(Person):
    def __init__(self, name, age, field_of_work, salary):
        super().__init__(name, age)
        field_of_work = input("Field of work: ") 
        salary = input("Salary: ")
        if not utils.isNumber(salary, "Salary"):
            raise ValueError
    
        self._field_of_work = field_of_work
        self._salary = int(salary)


    def setFieldOfWork(self, field_of_work):
        self._field_of_work = field_of_work
    

    def getFieldOfWork(self):
        return self._field_of_work
    

    def setSalary(self, salary):
        self._salary = salary


    def getSalary(self):
        return self._salary
    

    def __repr__(self):
        employee_fields = [f"Field of work: {self.getFieldOfWork()}",
                           f"Salary: {self.getSalary()}"]
        # Using list comprehension to add an indent at the beginning of each line
        employee_fields = ["   " + line for line in employee_fields]
        return super().__repr__() + os.linesep.join(employee_fields) + os.linesep
                           
    
    def getAttributesDict(self):
        dict_all_attributes = super().getAttributesDict()
        dict_attributes_employee = {"field_of_work": self.getFieldOfWork(), 
                                   "salary": self.getSalary()}
        dict_all_attributes.update(dict_attributes_employee)
        return dict_all_attributes
    
    def getType(self):
        return __class__.__name__

if __name__ == "__main__":
    test_name = "test name"
    test_age = 33
    test_field_of_work = "Photography"
    test_salary = 15000
    employee_1 = Employee(test_name, test_age, test_field_of_work, test_salary)

    if employee_1.getName() != test_name:
        print("Error: Name should be " + test_name + " but is " + employee_1.getName())
    else:
        print("Passed name test")

    if employee_1.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but is " + str(employee_1.getAge()))
    else:
        print("Passed age test")

    if employee_1.getFieldOfWork() != test_field_of_work:
        print("Error: Field of work should be " + test_field_of_work + " but is " + employee_1.getFieldOfWork())
    else:
        print("Passed field of work test")

    if employee_1.getSalary() != test_salary:
        print("Error: Salary should be " + str(test_salary) + " but is " + str(employee_1.getSalary()))
    else:
        print("Passed salary of work test")
    
