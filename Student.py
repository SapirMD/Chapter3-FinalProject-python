from Person import Person
import utilities as utils
import os

class Student(Person):
    def __init__(self, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(name, age)
        field_of_study = input("Field of study: ") 
        year_of_study = input("Year of study: ") 
        if not utils.isNumber(year_of_study, "year of study"):
            raise ValueError
        score_avg = input("Score avrage: ") 
        if not utils.isNumber(score_avg, "score avrage"):
            raise ValueError

        self._field_of_study = field_of_study
        self._year_of_study = int(year_of_study)
        self._score_avg = int(score_avg)
    

    def setFieldOfStudy(self, field_of_study):
        self._field_of_study = field_of_study
    

    def getFieldOfStudy(self):
        return self._field_of_study
    

    def setYearOfStudy(self, year_of_study):
        self._year_of_study = year_of_study
    

    def getYearOfStudy(self):
        return self._year_of_study
    

    def setScoreAvg(self, score_avg):
        self._score_avg = score_avg
    

    def getScoreAvg(self):
        return self._score_avg
    

    def __repr__(self):
        student_fields = [f"Field of study: {self.getFieldOfStudy()}",
                          f"Year of study: {self.getYearOfStudy()}", 
                          f"Score avrage: {self.getScoreAvg()}"]
        # Using list comprehension to add an indent at the beginning of each line
        student_fields = ["   " + line for line in student_fields]
        return super().__repr__() + os.linesep.join(student_fields) + os.linesep
               

    def getAttributesDict(self):
        dict_all_attributes = super().getAttributesDict()
        dict_attributes_student = {"field_of_study": self.getFieldOfStudy(), 
                                   "year_of_study": self.getYearOfStudy(), 
                                   "score_avg": self.getScoreAvg()}
        dict_all_attributes.update(dict_attributes_student)
        return dict_all_attributes
    

    def getType(self):
        return __class__.__name__


if __name__ == "__main__":
    test_name = "test name"
    test_age = 55
    test_field_of_study = "Economics" 
    test_year_of_study = 2021
    test_score_avg = 75
    student_1 = Student(test_name, test_age, test_field_of_study, test_year_of_study, test_score_avg)

    print(student_1)

    if student_1.getName() != test_name:
        print("Error: Name should be " + test_name + " but is " + student_1.getName())
    else:
        print("Passed name test")

    if student_1.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but is " + str(student_1.getAge()))
    else:
        print("Passed age test")

    if student_1.getFieldOfStudy() != test_field_of_study:
        print("Error: Field of study should be " + test_field_of_study + " but is " + student_1.getFieldOfStudy())
    else:
        print("Passed field of study test")

    if student_1.getYearOfStudy() != test_year_of_study:
        print("Error: Year of study should be " + str(test_year_of_study) + " but is " + str(student_1.getYearOfStudy()))
    else:
        print("Passed year of study test")

    if student_1.getScoreAvg() != test_score_avg:
        print("Error: Score avg should be " + str(test_score_avg) + " but is " + str(student_1.getScoreAvg()))
    else:
        print("Passed score avg test")


