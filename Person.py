import utilities as utils
import os

class Person:
    def __init__(self, name, age):
        name = input("Name: ")
        age = input("Age: ")
        if not utils.isNumber(age, "Age"):
            raise ValueError
        
        self._name = name
        self._age = int(age)


    def setName(self, name):
        self._name = name
    

    def getName(self):
        return self._name


    def setAge(self, age):
        self._age = age
    

    def getAge(self):
        return self._age
    
    def __repr__(self):
        person_fields = [f"Name: {self.getName()}",
                         f"Age: {self.getAge()}"]
        # Using list comprehension to add an indent at the beginning of each line
        person_fields = ["   " + line for line in person_fields]
        return os.linesep.join(person_fields) + os.linesep
    

    def getAttributesDict(self):
        return {"name": self.getName(), "age": self.getAge()}


    def getType(self):
        return __class__.__name__
    

if __name__ == "__main__":
    test_name = "test name"
    test_age = 30
    person_1 = Person(test_name, test_age)
    
    if person_1.getName() != test_name:
        print("Error: Name should be " + test_name + " but is " + person_1.getName())
    else:
        print("Passed name test")

    if person_1.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but is " + str(person_1.getAge()))
    else:
        print("Passed age test")


